print("*** Welcome to brand name generator. ***")
city_name = input("What is your city name?.\n").strip()
pet_name = input("What is your favorite pet name.\n").strip()

brand_name = city_name.capitalize() + " " + pet_name.capitalize()
print(f"Your Brand name could be- {brand_name}")