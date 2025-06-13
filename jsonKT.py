import requests

url = f"https://www.metshein.com/kordamine/json/autod.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    autod = data
    leitud = False

    id_sisestus = input("Palun sisestage ID (501-515): ")

    try:
        auto = autod[id_sisestus]
        print(f"Role ID: {auto['id']}")
        print(f"Mark: {auto['mark']}")
        print(f"Mudel: {auto['model']}")
        print(f"V2ljalaskeaasta: {auto['release year']}")
        print(f"L2bis6it: {auto['l2bis6it']}")
        print(f"V2rv: {auto['v2rv']}")
        print(f"Hind: {auto['hind']}")
        leitud = True
    except IndexError:
        print("id pole õige")
else:
    print("Laadimisel tekkis viga", response.status_code)