import requests
import json


city = "Cityname"

def getStreet(street):
    with open('result.txt', 'a') as f:
        for i in range(1, 300):
            building = str(i)
            url = f'https://nominatim.openstreetmap.org/search.php?q={street}+{building}+{city}&format=json'    # Формируем url
            r = requests.get(url)                                                                               # Выполняем get
            data = r.json()
            if data[0]['class']=='building':
                f.write(street + ", " + building + ": " + data[0]['lat'] + " " + data[0]['lon']+'\n')

def main():
    with open("targets.txt", 'r') as f:
        for line in f:
            try:
                getStreet(line.replace("\n", ""))
                print(line)
            except:
                continue


if __name__ == "__main__":
    main()
