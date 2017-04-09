#!/usr/bin/python
# -*- coding: utf-8 -*-

# This program contains functions to save and load from databases in CouchDB
#   They connect to CouchDB running on port 5984, the default

import sys
import couchdb
import json
from twitter_login import oauth_login
from twitter_search import twitterSearch

# This function either starts or adds to an existing database in CouchDB
# Parameters:  
#   data - this should be a list of json objects, where each will be a DB element
#      stored under a unique ID key created by the DB
#   DBname - the name of the database, either new or existing

def save_to_DB (DBname, data):
    # connect to database server and create db if needed
    # open CouchDB befor running or it'll give a socket 61 error
    server = couchdb.Server('http://localhost:5984')
    # if you can't create a db of that name, assume that it already exists
    try:
        db = server.create(DBname)
        print "created new DB named", DBname
    except couchdb.http.PreconditionFailed, e:
        db = server[DBname]
        print "connected to existing DB named", DBname
    except ValueError, e:
        print "Invalid DB name" 
        sys.exit(0)
        
    # add the data to the database
    db.update(data, all_or_nothing=True)


# This function either gets data from an existing DB
# Parameter:  
#   DBname - the name of the database, either new or existing
# Result:
#   data - returns all the data in the DB as a list of JSON objects

def load_from_DB (DBname):
    # connect to database on couchdb server
    server = couchdb.Server('http://localhost:5984')
    try:
        db = server[DBname]
        print "Connected to DB named", DBname
    except couchdb.http.PreconditionFailed, e:
        db = server[DB]
        print "Could not find DB named", DBname
        return []
    except ValueError, e:
        print "Invalid DB name"
        return []
    
    
    # get list of documents from database, stored under the unique ID keys
    doclist = [db[key] for key in db] 
    return doclist

# the main program gets a twitter search, saves the results and reloads it
if __name__ == '__main__':
    twitter_api = oauth_login()
    print "Twitter OAuthorization: ", twitter_api
    # define the topic query
    query = '#elecciones2015'
    #query = '#eleccionesargentinas'"
    #query = 'SOTU'
    #query = 'Pete Seegar'
    
    # access Twitter search
    result_tweets = twitterSearch(twitter_api, query, max_results=1000)
    print 'Number of result tweets: ', len(result_tweets)
    
    # save the results in a database named search followed by the query
    #   couchDB names have to be in lowercase letters
    #   and also cannot contain special characters like hashtags and spaces
    DBname = 'search-' + query.lower()
    DBname = DBname.replace('#', '')
    DBname = DBname.replace(' ', '')
    
    # use the save and load functions in this program
    save_to_DB(DBname, result_tweets)
    # reload the results into a new variable
    search_results = load_from_DB(DBname)
    print 'number loaded', len(search_results)
    
    # display all text from the search 
    textList = [doc['text'] for doc in search_results]
    for text in textList:
        try:
            line = text.encode('utf-8')
            print line
        except UnicodeDecodeError:
            print "skipping non-utf-8 string"
        except UnicodeEncodeError:
            print "skipping non-utf-8 string"
