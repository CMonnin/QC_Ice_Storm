import pandas as pd
import time
import csv


url = 'https://poweroutages.hydroquebec.com/poweroutages/service-interruption-report/index.html'




# def scraper():
#     full_page = pd.read_html(url)
#     df = full_page[0]
#     df.insert(0,'Time',time.ctime())
    
#     dic = df.iloc[17].to_dict()
#     field_names = dic.keys()

#     with open('event.csv', 'a') as csv_file:
#         dict_object = csv.DictWriter(csv_file, fieldnames=field_names) 
#         dict_object.writerow(dic)
#     print(time.ctime())
#     time.sleep(1)


for i in range (1000):
    full_page = pd.read_html(url)
    df = full_page[0]
    df.insert(0,'Time',time.ctime())
    
    dic = df.to_dict()
    field_names = dic.keys()

    with open('event.csv', 'a') as csv_file:
        dict_object = csv.DictWriter(csv_file, fieldnames=field_names) 
        dict_object.writerow(dic)
    print(time.ctime())
    time.sleep(900) 