import csv
import json


with open("JSON.json") as json_file:
    data = json.load(json_file)
    print(data)
    employee_data = data["emp_details"]
    data_file = open("data_file.csv" , "w")

    csv_writer = csv.writer(data_file)

    counter = 0
    for emp in employee_data:
        if counter == 0:
            header = emp.keys()
            csv_writer.writerow(header)
            counter+=1

        csv_writer.writerow(emp.values())
    data_file.close()