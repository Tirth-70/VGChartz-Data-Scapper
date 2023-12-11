# import numpy as np
# from functools import reduce
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# from concurrent.futures import ThreadPoolExecutor
# tm = time.time()
# print('Program Starting:)')
# def convert_date(data):
#     from datetime import datetime
#     current_year = 23

#     temp = data.split()
#     temp[0] = temp[0][:2]

#     if int(temp[2]) > current_year:
#         temp[2] = '19'+temp[2]
#     else:
#         temp[2] = '20'+temp[2]


#     date_string = '-'.join(temp)
#     datetime = datetime.strptime(date_string, '%d-%b-%Y').date()
#     return datetime

# def getdata(i):
#     x = time.time()
#     print('Getting page->',i)
#     url = 'https://www.vgchartz.com/games/games.php?page='
#     url_conti = '&results=7856&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=1&showpalsales=1&showjapansales=1&showothersales=1&showpublisher=1&showdeveloper=1&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=1'
#     head = url + str(i) + url_conti
#     dat = requests.get(head)
#     print("Total->",i,":",time.time()-x)
#     return dat


# def opti(web):
#     x = time.time()
#     print("Sorting things out...")
#     soup = BeautifulSoup(web.content, 'lxml')
#     result = soup.find(id='generalBody')
#     head = result.find_all('tr')[2].find_all('th')
#     columns = []

#     for col in head:
#         columns.append(col.text.strip())
#     columns.insert(1, 'Image')
    
#     df1 = pd.DataFrame(columns=columns)

#     def process_data(data):
#         row = data.find_all('td')
#         data_row = []
#         for r in row:
#             data_row.append(r.text.strip())
#         data_row[1] = 'https://www.vgchartz.com' + row[1].find('img')['src']
#         data_row[3] = row[3].find('img')['alt']
#         data_row = reduce(lambda a, b: a + [np.nan] if b == 'N/A' else a + [b], data_row, [])
#         if not pd.isna(data_row[15]):
#             data_row[15] = convert_date(data_row[15])
#         if not pd.isna(data_row[16]):
#             data_row[16] = convert_date(data_row[16])
#         return pd.DataFrame([data_row], columns=columns)

#     def convert_date(data):
#         from datetime import datetime
#         current_year = 23
    
#         temp = data.split()
#         temp[0] = temp[0][:2]
    
#         if int(temp[2]) > current_year:
#             temp[2] = '19'+temp[2]
#         else:
#             temp[2] = '20'+temp[2]
    
    
#         date_string = '-'.join(temp)
#         datetime = datetime.strptime(date_string, '%d-%b-%Y').date()
#         return datetime
    
#     def scrape_rows():
#         return result.find_all('tr')[3:7859]

#     with ThreadPoolExecutor() as executor:
#         rows = scrape_rows()
#         dfs = executor.map(process_data, rows)

#     df1 = pd.concat(list(dfs), ignore_index=True)
#     print("Total:", time.time()-x)
#     return df1


# t = time.time()
# print(t)
# with ThreadPoolExecutor(max_workers=4) as executor:
#         data_list = executor.map(getdata, range(1,9))
# print("End",time.time()-t)

# c = 1
# for data in data_list:
#     if c==1: 
#         x1 = data
#     elif c==2:
#         x2 = data
#     elif c==3:
#         x3 = data
#     elif c==4:
#         x4 = data
#     elif c==5:
#         x5 = data
#     elif c==6:
#         x6 = data
#     elif c==7:
#         x7 = data
#     elif c==8:
#         x8 = data
#     c+=1

# lis = [x1,x2,x3,x4,x5,x6,x7,x8]
# e = time.time()
# with ThreadPoolExecutor(max_workers=8) as executor:
#     result_map = executor.map(opti,(i for i in lis))
# f = time.time()
# print("End:",f-e)
# outdf = pd.concat(j for j in result_map)
# print("Concat Time:", time.time()-f)
# outdf.to_csv('game_data.csv')

# print('Program Over:)')
# print('Time Taken:',time.time()-tm)

# Import necessary libraries
import numpy as np
from functools import reduce
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor

# Record the start time of the program
tm = time.time()
print('Program Starting:)')

# Function to convert date format
def convert_date(data):
    from datetime import datetime
    current_year = 23

    temp = data.split()
    temp[0] = temp[0][:2]

    # Adjust the year based on a threshold
    if int(temp[2]) > current_year:
        temp[2] = '19'+temp[2]
    else:
        temp[2] = '20'+temp[2]

    # Join and convert the date string to a datetime object
    date_string = '-'.join(temp)
    datetime_obj = datetime.strptime(date_string, '%d-%b-%Y').date()
    return datetime_obj

# Function to get data from a specific page
def getdata(i):
    x = time.time()
    print('Getting page->', i)
    url = 'https://www.vgchartz.com/games/games.php?page='
    url_conti = '&results=7856&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=1&showpalsales=1&showjapansales=1&showothersales=1&showpublisher=1&showdeveloper=1&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=1'
    head = url + str(i) + url_conti
    dat = requests.get(head)
    print("Total->", i, ":", time.time()-x)
    return dat

# Function to process web content and extract data
def opti(web):
    x = time.time()
    print("Sorting things out...")
    soup = BeautifulSoup(web.content, 'lxml')
    result = soup.find(id='generalBody')
    head = result.find_all('tr')[2].find_all('th')
    columns = []

    # Extract column names from the table header
    for col in head:
        columns.append(col.text.strip())
    columns.insert(1, 'Image')
    
    df1 = pd.DataFrame(columns=columns)

    # Function to process each row and extract data
    def process_data(data):
        row = data.find_all('td')
        data_row = []
        for r in row:
            data_row.append(r.text.strip())
        data_row[1] = 'https://www.vgchartz.com' + row[1].find('img')['src']
        data_row[3] = row[3].find('img')['alt']
        
        # Convert 'N/A' values to NaN and handle date conversion
        data_row = reduce(lambda a, b: a + [np.nan] if b == 'N/A' else a + [b], data_row, [])
        if not pd.isna(data_row[15]):
            data_row[15] = convert_date(data_row[15])
        if not pd.isna(data_row[16]):
            data_row[16] = convert_date(data_row[16])
        return pd.DataFrame([data_row], columns=columns)

    # Function to scrape rows from the web content
    def scrape_rows():
        return result.find_all('tr')[3:7859]

    # Use ThreadPoolExecutor for parallel processing of rows
    with ThreadPoolExecutor() as executor:
        rows = scrape_rows()
        dfs = executor.map(process_data, rows)

    # Concatenate the DataFrames obtained from parallel processing
    df1 = pd.concat(list(dfs), ignore_index=True)
    print("Total:", time.time()-x)
    return df1

# Record the start time of data retrieval
t = time.time()
print(t)

# Use ThreadPoolExecutor to retrieve data from multiple pages concurrently
with ThreadPoolExecutor(max_workers=4) as executor:
    data_list = executor.map(getdata, range(1, 9))

print("End", time.time()-t)

# Assign retrieved data to variables
c = 1
for data in data_list:
    if c == 1: 
        x1 = data
    elif c == 2:
        x2 = data
    elif c == 3:
        x3 = data
    elif c == 4:
        x4 = data
    elif c == 5:
        x5 = data
    elif c == 6:
        x6 = data
    elif c == 7:
        x7 = data
    elif c == 8:
        x8 = data
    c += 1

# Store the data in a list
lis = [x1, x2, x3, x4, x5, x6, x7, x8]

# Record the start time of data processing
e = time.time()

# Use ThreadPoolExecutor for parallel processing of data optimization
with ThreadPoolExecutor(max_workers=8) as executor:
    result_map = executor.map(opti, (i for i in lis))

# Record the end time of data processing
f = time.time()
print("End:", f-e)

# Concatenate the optimized DataFrames
outdf = pd.concat(j for j in result_map)

# Record the time taken for concatenation
print("Concat Time:", time.time()-f)

# Save the final DataFrame to a CSV file
outdf.to_csv('Game_Data1.csv')

# Print the program completion message and total time taken
print('Program Over:)')
print('Time Taken:', time.time()-tm)
