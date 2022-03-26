import requests
import csv

rajesthan_data = "https://thinkhazard.org/en/report/1506/UF.geojson?resolution=4891.96981025128"

response = requests.get(rajesthan_data)
data = response.json()
f = open('csv_file', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['name', 'hazardLevelMnemonic', 'hazardLevelTitle', 'url'])
for item in data['features']:
    line = []
    line.append(item['properties']['name'])
    line.append(item['properties']['hazardLevelMnemonic'])
    line.append(item['properties']['hazardLevelTitle'])
    line.append(item['properties']['url'])

    writer.writerow(line)

f.close()
