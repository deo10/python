# work with CSV files in python

import csv

# write to a csv file
with open('data.csv', 'w') as file:
    # create a csv writer object
    writer = csv.writer(file, delimiter=';')
    # write a row
    writer.writerow(['user_id', 'user_name', 'comments_qty'])
    writer.writerow([12056, 'vlad', 102])
    writer.writerow([12057, 'mike', 102])
    writer.writerow([12058, 'petr', 102])

# open the file
with open('data.csv', 'r') as file:
    # create a csv reader object
    reader = csv.reader(file, delimiter=';')
    # iterate over the rows
    for row in reader:
        print(row)
        
# delete the file
import os
os.remove('data.csv')
        

    