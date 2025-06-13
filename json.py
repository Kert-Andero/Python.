#Kert-Andero Põldmaa
import requests

url = f"https://www.metshein.com/kordamine/json/autod.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    cars = data
    leitud = False

    id_sisestus = int(input("Palun sisestage ID(1-10): "))

    try:
        cars = cars[id_sisestus -1]
        print(f"Role ID: {cars['id']}")
        print(f"Mark: {cars['name']}")
        print(f"Mudel: {cars['model']}")
        print(f"Väljalaskeaasta: {cars['release year']}")
        print(f"Läbisõit_km: {cars['mileage']}")
        print(f"Värv: {cars['color']}")
        print(f"Hind: {cars['Price']}")
        leitud = True

    except IndexError:
        print("ID pole õige")
else:
    print("Laadimise viga", response.status_code)