
def get_excel_data(sheet):
    headers = ["StrId", "ProjId", "TweetText", "Label"]
    excel_data = []#list of dictionaries ##NAME OF LIST of dict
    for row_num, row in enumerate(sheet):
        if row_num is 0: # skip the first row (don't want headers)
            continue
        row_data = {}  #open a dictionary ##NAME OF DICTIONARY OF VALUES IN EACH ROW
        for col_num, cell in enumerate(row): # populating the dictionary with header names as keys and cell content as values# populating the dictionary with header names as keys and cell content as values
            if col_num > len(headers)-2: #ask Max what this is
                continue
            key = headers[col_num]
            value = cell.value
            row_data[key] = value
        excel_data.append(row_data) # adding each key-value pair to the excel_data list
    return excel_data