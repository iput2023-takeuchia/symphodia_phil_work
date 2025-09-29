import csv
import sys

DATA_DIR = 'data'
CSV_FILENAME = 'data.csv'
filename = DATA_DIR + '/' + CSV_FILENAME

def csv_write_iterator(data_r_list):
    print(sys._getframe().f_code.co_name)
    with open(filename, mode='a', newline='') as f:
        write_iter = csv.writer(f)
        for row in data_r_list:
            water_temp = row.get("water-temperature", row.get("temp_dht_1"))
            co2 = row.get("CO2", row.get("humid_dht_1"))
            temp = row.get("temperature", row.get("humid_dht_1"))
            hum = row.get("humidity", row.get("humid_dht_1"))
            ec25 = row.get("EC25", row.get("humid_dht_1"))
            write_iter.writerow([water_temp, co2, temp, hum,ec25])

def csv_read_one_file():
    print(sys._getframe().f_code.co_name)
    with open(filename) as f:
        all_data = f.read()
        print(all_data)

def csv_read_iterator():
    print(sys._getframe().f_code.co_name)
    with open(filename) as f:
        all_data_iter = csv.reader(f)
        for row in all_data_iter:
            print(row)

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    csv_read_iterator()
    csv_read_one_file()
    data_r_list = [
        {"water-temperature":24.0, "CO2":1000, "temperature": 25.0, "humidity": 60.0, "EC25":0.0},
        {"water-temperature":24.0, "CO2":1000, "temperature": 26.5, "humidity": 65.0, "EC25":0.0},
        {"water-temperature":24.0, "CO2":1000, "temperature": 27.0, "humidity": 70.0, "EC25":0.0}
    ]
    csv_write_iterator(data_r_list)