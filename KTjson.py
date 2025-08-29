import requests
url = "https://dummyjson.com/recipes"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    recipes = data["recipes"]
    
    try:
        id_input = int(input("Palun sisestage ID (1–30): "))
        data = response.json()
        found_recipe = None
        for recipe in recipes:
            if recipe["id"] == id_input:
                found_recipe = recipe

        if found_recipe:
            print("Recipe info:")
            print(f"ID: {found_recipe['id']}")
            print(f"Nimi: {found_recipe['name']}")
            print(f"Valmistusaeg: {found_recipe['prepTimeMinutes']} min")
            print(f"Küpsetusaeg: {found_recipe['cookTimeMinutes']} min")
            print(f"Juhised: {found_recipe['instructions']}")
        else:
            print("Sisestatud ID ei sobi.")
    except ValueError:
        print("Sellist ID ei ole.")
else:
    print("Andmete laadimisel tekkis viga", response.status_code)