import csv
import sys
import datetime
import os

DATA_DIR = 'data'
CSV_FILENAME = 'data.csv'
filename = DATA_DIR + '/' + CSV_FILENAME

def csv_write_iterator(data_r_list):
    print(sys._getframe().f_code.co_name)
    with open(filename, mode='a', newline='') as f:
        write_iter = csv.writer(f)
        for row in data_r_list:
            water_temp = row.get("water-temperature")
            co2 = row.get("CO2")
            temp = row.get("temperature")
            hum = row.get("humidity")
            ec25 = row.get("EC25")
            time = row.get("created")
            write_iter.writerow([water_temp, co2, temp, hum, ec25, time])

def csv_read_one_file():
    print(sys._getframe().f_code.co_name)
    with open(filename) as f:
        all_data = f.read()
        print(all_data)

def csv_read_iterator():
    print(sys._getframe().f_code.co_name)
    with open(filename, newline='', encoding='utf-8') as f:
        data_list = []
        reader = csv.reader(f)
        return [[float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4]), row[5]]for row in reader]
    
def csv_delete():
    print(sys._getframe().f_code.co_name)

    
if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    csv_read_iterator()
    csv_read_one_file()
    data_r_list = [
        {"water-temperature":24.0, "CO2":1000, "temperature": 25.0, "humidity": 60.0, "EC25":0.0, "created": '2025-08-25T10:45:16.685Z'},
        {"water-temperature":24.0, "CO2":1000, "temperature": 26.5, "humidity": 65.0, "EC25":0.0, "created": '2025-08-25T10:45:16.685Z'},
        {"water-temperature":24.0, "CO2":1000, "temperature": 27.0, "humidity": 70.0, "EC25":0.0, "created": '2025-08-25T10:45:16.685Z'}
    ]
    csv_write_iterator(data_r_list)