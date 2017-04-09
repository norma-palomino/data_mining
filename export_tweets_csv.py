import csv


def export_tweets(tweets, file_name):
    with open(file_name, 'wb') as f:
        writer = csv.writer(f)
        
        # write headers
        writer.writerow(['serial_id', 'text', 'tweet_id'])
        for counter, tweet in enumerate(tweets):
            
            # adding 1, so the Ids start at 1 instead of 0
            serial_id = counter + 1

            # This is so we don't get the infamous
            # "ordinal not in range" error
            encoded_text = tweet['text'].encode('utf-8')
            tweet_id = tweet['id_str']
            writer.writerow([serial_id, encoded_text, tweet_id])
