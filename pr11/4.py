import csv
import json
import xml.etree.ElementTree as ET

class WeatherCSVData:
    def __init__(self, file_path):
        self.data = []
        self.load_data(file_path)

    def load_data(self, file_path):
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            for row in csv_reader:
                self.data.append(row)

    def save_as_json(self, output_path):
        with open(output_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def save_as_xml(self, output_path):
        root = ET.Element('WeatherData')
        for entry in self.data:
            record = ET.SubElement(root, 'Record')
            for key, value in entry.items():
                ET.SubElement(record, key).text = value
        tree = ET.ElementTree(root)
        tree.write(output_path)

    def get_max_temperature(self):
        temperatures = [float(entry['Temperature  [2 m above gnd]']) for entry in self.data]
        return max(temperatures)

    def get_min_temperature(self):
        temperatures = [float(entry['Temperature  [2 m above gnd]']) for entry in self.data]
        return min(temperatures)

    def get_avg_temperature(self):
        temperatures = [float(entry['Temperature  [2 m above gnd]']) for entry in self.data]
        return sum(temperatures) / len(temperatures)

# Припустимо, у вас є файл weather.csv у поточному каталозі
csv_data = WeatherCSVData('weather.csv')
csv_data.save_as_json('weather.json')
csv_data.save_as_xml('weather.xml')

max_temp = csv_data.get_max_temperature()
min_temp = csv_data.get_min_temperature()
avg_temp = csv_data.get_avg_temperature()

print(f"Max Temperature: {max_temp}°C")
print(f"Min Temperature: {min_temp}°C")
print(f"Avg Temperature: {avg_temp}°C")
