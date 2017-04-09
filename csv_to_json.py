import csv
import json

def clean(word):
        if not word:
		return ''	
	return ''.join([i if ord(i) < 128 else '' for i in word])
        

def csv_to_list_of_dicts(csv_file_name):
	entries=[]
	with open(csv_file_name,'rb') as f:
		reader=csv.reader(f)
		headers=[]
		for row_num,row in enumerate(reader):
			if row_num==0:
				headers=row
				continue
			entry={}
			for col_num,col in enumerate(row):
				val=None
				try:
					val=float(col)
				except:
					val=''.join([i if ord(i) < 128 else ' ' for i in col])
				entry[headers[col_num]]=val
			entries.append(entry)

	return entries

def list_of_dicts_to_csv(list_of_dicts,csv_file_name):
	with open(csv_file_name,'wb') as f:
		writer=csv.writer(f)
		headers=list_of_dicts[0].keys()
		writer.writerow(headers)
		for row in list_of_dicts:
		    row = [clean(value) for value in row.values()]
		    writer.writerow(row)			

def json_to_dict(json_file_name):
	dictionary={}
	with open(json_file_name,'r') as f:
		data=f.read()
		dictionary=json.loads(data)
	return dictionary

def csv_to_json(csv_file_name):
	entries=csv_to_rows_of_dicts(csv_file_name)
	return json.dumps(entries)