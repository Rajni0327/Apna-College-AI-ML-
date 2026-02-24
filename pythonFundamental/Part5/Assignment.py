# # Answer 1 --------------------------------------------
# with open("names.txt","w") as f :
#     print("enter 5 names :")

#     for i in range(5):
#         name = input(f"enter {i+1} :")
#         f.write(name +"\n") #each name in new line

# with open("names.txt", "r") as f :
#     print("names are :")

#     for line in f :
#         print(line.strip()) #removes extra newline while printing


# # Amswer 2 -------------------------------------------

# with open("log.txt","a") as f :
#     f.write("Program run successfully!")

# with open("log.txt","r") as f:
#     logs = f.read()
#     print("logs")



# # Answer 3------------------------------------------------

# lst = [5, 10, 15, 20, 25]

# new_list = [num for num in lst if num > 15]

# print(new_list)


# answer 4 -------------------------------------------------

import json

cities = {
    "New York": 8419600,
    "Tokyo": 13929286,
    "Delhi": 30291000
}

with open("cities.json", "w") as file:
    json.dump(cities, file)

with open("cities.json", "r") as file:
    loaded_cities = json.load(file)

print("Current Cities and Populations:")
for city, population in loaded_cities.items():
    print(f"{city}: {population}")

new_city = input("Enter a new city name: ")
new_population = int(input(f"Enter the population of {new_city}: "))

loaded_cities[new_city] = new_population

with open("cities.json", "w") as file:
    json.dump(loaded_cities, file)

print("\nUpdated Cities and Populations:")
for city, population in loaded_cities.items():
    print(f"{city}: {population}")
