import requests
import csv
session = requests.Session()
passapi="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"
shop="pythonify"
apikey="f34e1a8e47f7c04fda419e223aa438e0"
url="https://"+apikey+":"+passapi+"@"+shop+".myshopify.com/admin/api/2020-10/customers.json"
resp = session.get(url)

csv_columns = []
for i in resp.json()['customers'][0].keys():
    if i != "addresses":
        csv_columns.append(i)
 
dict_data = resp.json()['customers']
for i in dict_data:
    i.pop('addresses')
csv_file = "C:/Users/DELL/python/names.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")
