import csv, json

csvFilePath = "file.csv"
jsonFilePath = "file.json"

#read the csv and add the data to a dictionary

data = {}
with open (csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows["name"]

        data[id] = rows

print(data)

with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent = 4))




"""import csv , json

csvFilePath = "file.csv"
jsonFilePath = "file.json"
arr = []
#read the csv and add the arr to a arrayn

with open (csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    print(csvReader)
    for csvRow in csvReader:
        arr.append(csvRow)

print(arr) """