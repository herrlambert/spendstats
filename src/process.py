from os import listdir
from os.path import isfile, join
import csv
import categorymap as cm

category_map = cm.category_map()
mypath = 'datafiles/'

def get_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

def get_filedata(files, mypath):
    file_data = []
    for file in files:
        file_info = {'file_name': None, 'file_lines': None}
        with open(join(mypath, file)) as file:
            file_info['file_lines'] = [line.rstrip() for line in file]
    
        file_name = file.name[10:17]
        if file_name[-1:] == '-':
            file_info['file_name'] = file_name[:-1]
        
        file_data.append(file_info)
    return file_data

def process_lines(file_name, file_lines):
    lines = file_lines[1:]
    new_lines = []
    for line in lines:
        line = line.split(',')
        line[0] = file_name
        if len(line) > 6:
            description = line[2] + line[3]
            line[2] = description
            del line[3]
        
        # remove double-quotes surrounding description string
        line[2] = line[2][1:-1]
        
        # calculate total and assign to position 3
        total = line[3] + line[4]
        line[3] = total
        del line[4]
        
        new_lines.append(line)
        
    return new_lines
    
def categorize(description):
    description = description.lstrip().lower()
    for key, value in category_map.items():
        if description.find(key) > -1:
            return (key, value)
    return None
    
def categorize_lines(lines):
    categorized_lines = []
    for line in lines:
        categories = categorize(line[2])
        if categories:
            line.append(categories[1])
            line.append(categories[0])
        else:
            line.append(None)
            line.append(None)
        categorized_lines.append(line)
    return categorized_lines
    
def get_updated_data(file_data):
    updated_data = [['statement', 'transdate', 'description', 'amount', 'who', 'category', 'subcategory']]
    for item in file_data:
        lines = process_lines(item['file_name'], item['file_lines'])
        categorized_lines = categorize_lines(lines)
        for line in categorized_lines:
            updated_data.append(line)
    return updated_data
    
# files = get_files(mypath)
# file_data = get_filedata(files, mypath)
# updated_data = get_updated_data(file_data)
'''
with open("all_transactions.csv", "w+") as my_csv:
    csv_writer = csv.writer(my_csv, delimiter=',')
    csv_writer.writerows(updated_data)
'''