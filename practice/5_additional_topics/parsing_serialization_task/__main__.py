import json, os, pprint
from statistics import mean
from lxml import etree

data = dict()
city_list = os.listdir("source_data")
if ".DS_Store" in city_list:
    city_list.remove(".DS_Store")
for city in city_list:
    data[city] = {}

    # open source file for every city
    with open('source_data/'+city+'/2021_09_25.json', 'r') as file:
        entire_dict = json.load(file)["hourly"]
        temperatures = []
        wind_speeds=[]

        # get list of temperatures and wind speeds
        for dict in entire_dict:
            temperatures.append(dict['temp'])
            wind_speeds.append(dict['wind_speed'])
        
        # calculate the statistics for every city
        data[city]["mean_temp"] = round(mean(temperatures), 2)
        data[city]["min_temp"] = min(temperatures)
        data[city]["max_temp"] = max(temperatures)
        data[city]["mean_wind_speed"] = round(mean(wind_speeds), 2)
        data[city]["min_wind_speed"] = min(wind_speeds)
        data[city]["max_wind_speed"] = max(wind_speeds)

# calculate the statistics for entire Spain
mean_temps = [data[city]["mean_temp"] for city in city_list]
mean_wind_speeds = [data[city]["mean_wind_speed"] for city in city_list]
spain_data = {
    "mean_temp" : round(mean(mean_temps), 2),
    "mean_wind_speed" : round(mean(mean_wind_speeds), 2),
    "coldest_place" : list(data.keys())[mean_temps.index(min(mean_temps))],
    "warmest_place" : list(data.keys())[mean_temps.index(max(mean_temps))],
    "windiest_place" : list(data.keys())[mean_wind_speeds.index(max(mean_wind_speeds))]
}

# convert floats to str
for city in city_list:
    for key in data[city]:
        data[city][key] = str(data[city][key])

# convert to xml
root = etree.Element("weather", country="Spain", date="2021-09-25")
summary = etree.SubElement(root, "summary")
for key in spain_data:
    summary.set(key, str(spain_data[key]))

cities = etree.SubElement(root, "cities")
for city in city_list:
    a = etree.SubElement(cities, city.replace(' ', '_'), **data[city])

# save as results.xml
et = etree.ElementTree(root)
et.write('results.xml', pretty_print=True)




    