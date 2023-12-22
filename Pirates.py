# Pirates_information = {}
# while True:
#     command,*params=input().split("||")
#     if command=="Sail":
#         break
#         while True:
#             action,*param=input().split("=>")
#             if action=="End":
#                 break
#             elif action=="Plunder":
#                 pass
#     city = command
#     population = int(params[0])
#     gold = int(params[1])
#     if city not in Pirates_information.keys():
#         Pirates_information[city] = {"Population": population, "Gold": gold}
#
#
#     else:
#         Pirates_information[city] = {"Population": population + int(params[0]), "Gold": gold + (int(params[1]))}
#
#
#
#
# print(Pirates_information)









# pirates={}
# while True:
#     command,*params=input().split("||")
#     if command=="Sail":
#         break
#
#     city=command
#     population=int(params[0])
#     gold=int(params[1])
#     if city not in pirates.keys():
#         pirates[city]={"Population":population,"Gold":gold}
#     else:
#         pirates[city]["Population"]+=population
#         pirates[city]["Gold"]+=gold
#
#
#  while True:
#     action,*params=input().split("=>")
#     if action=="End":
#         break
#     elif action=="Plunder":
#         name_of_city=params[0]
#         people=int(params[1])
#         money=int(params[2])
#         pirates[name_of_city]["Population"]-=people
#         pirates[name_of_city]["Gold"] -= money
#         if pirates[name_of_city]["Population"]==0:
#             del pirates[name_of_city]["Population"]
#             print(f"{name_of_city} has been wiped off the map!")
#         if pirates[name_of_city]["Gold"]==0:
#             del pirates[name_of_city]["Gold"]
#             print(f"{name_of_city} has been wiped off the map!")
#         print(f"{name_of_city} plundered! {money} gold stolen, {people} citizens killed.")
#
#
#     elif action=="Prosper":
#         name_of_city=params[0]
#         money=int(params[1])
#         if money<0:
#             print("Gold added cannot be a negative number!")
#         else:
#             pirates[name_of_city]["Gold"] += money
#             print(f'{money} gold added to the city treasury. {name_of_city} now has {pirates[name_of_city]["Gold"]} gold.')





# pirates = {}
#
# while True:
#     command, *params = input().split("||")
#     if command == "Sail":
#         break
#
#     city = command
#     population = int(params[0])
#     gold = int(params[1])
#     if city not in pirates.keys():
#         pirates[city] = {"Population": population, "Gold": gold}
#     else:
#         pirates[city]["Population"] += population
#         pirates[city]["Gold"] += gold
#
# while True:
#     action, *params = input().split("=>")
#     if action == "End":
#         print("Ahoy, Captain! There are {count} wealthy settlements to go to:")
#         for k,v in pirates.items():
#             print(k,end=" ")
#             for k1,v1 in v.items():
#                 print(k1,v1, end=" ")
#             print()
#
#
#
#         break
#     elif action == "Plunder":
#         name_of_city = params[0]
#         people = int(params[1])
#         money = int(params[2])
#         pirates[name_of_city]["Population"] -= people
#         pirates[name_of_city]["Gold"] -= money
#         if pirates[name_of_city]["Population"] <= 0 or pirates[name_of_city]["Gold"] <= 0:
#             del pirates[name_of_city]
#             print(f"{name_of_city} has been wiped off the map!")
#         else:
#             print(f"{name_of_city} plundered! {money} gold stolen, {people} citizens killed.")
#     elif action == "Prosper":
#         name_of_city = params[0]
#         money = int(params[1])
#         if money < 0:
#             print("Gold added cannot be a negative number!")
#         else:
#             pirates[name_of_city]["Gold"] += money
#             print(f'{money} gold added to the city treasury. {name_of_city} now has {pirates[name_of_city]["Gold"]} gold.')


# pirates = {}
#
# while True:
#     command, *params = input().split("||")
#     if command == "Sail":
#         break
#
#     city = command
#     population = int(params[0])
#     gold = int(params[1])
#     if city not in pirates.keys():
#         pirates[city] = {"Population": population, "Gold": gold}
#     else:
#         pirates[city]["Population"] += population
#         pirates[city]["Gold"] += gold
#
# while True:
#     action, *params = input().split("=>")
#     if action == "End":
#         print("Ahoy, Captain! There are {count} wealthy settlements to go to:")
#         for k,v in pirates.items():
#             print(k,end=" ")
#             for k1,v1 in v.items():
#                 print(k1,v1, end=" ")
#             print()
#         break
#     elif action == "Plunder":
#         name_of_city = params[0]
#         people = int(params[1])
#         money = int(params[2])
#         pirates[name_of_city]["Population"] -= people
#         pirates[name_of_city]["Gold"] -= money
#         print(f"{name_of_city} plundered! {money} gold stolen, {people} citizens killed.")
#
#         if pirates[name_of_city]["Population"] <= 0 or pirates[name_of_city]["Gold"] <= 0:
#             del pirates[name_of_city]
#             print(f"{name_of_city} has been wiped off the map!")
#     elif action == "Prosper":
#         name_of_city = params[0]
#         money = int(params[1])
#         if money < 0:
#             print("Gold added cannot be a negative number!")
#         else:
#             pirates[name_of_city]["Gold"] += money
#             print(
#                 f'{money} gold added to the city treasury. {name_of_city} now has {pirates[name_of_city]["Gold"]} gold.')
#
# pirates={}
# def Populate_dict_of_pirates(pirates_dict):
#     while True:
#         command, *params = input().split("||")
#         if command == "Sail":
#             break
#
#         city = command
#         population = int(params[0])
#         gold = int(params[1])
#         if city not in pirates.keys():
#             pirates[city] = {"Population": population, "Gold": gold}
#         else:
#             pirates[city]["Population"] += population
#             pirates[city]["Gold"] += gold
#         return pirates_dict
#
# pirates_dict=Populate_dict_of_pirates(pirates)
#
# def Plunder(pirates_dict,city_target,people,money_for_taken):
#     pirates[city_target]["Population"] -= people
#     pirates[city_target]["Gold"] -= money
#     print(f"{city_target} plundered! {money_for_taken} gold stolen, {people} citizens killed.")
#
#     if pirates[city_target]["Population"] <= 0 or pirates[name_of_city]["Gold"] <= 0:
#         del pirates[name_of_city]
#         print(f"{name_of_city} has been wiped off the map!")
#     return pirates_dict
#
#
#
#
#
# def Prosper(pirates_dict,city_targer,money_for_taken):
#     if money < 0:
#         print("Gold added cannot be a negative number!")
#     else:
#         pirates[city_targer]["Gold"] += money_for_taken
#         print(f'{money_for_taken} gold added to the city treasury. {city_targer} now has {pirates[city_targer]["Gold"]} gold.')
#     return pirates_dict
#
# while True:
#     action, *params = input().split("=>")
#     if action == "End":
#         print(f"Ahoy, Captain! There are {len(pirates)} wealthy settlements to go to:")
#         for city, stats in pirates.items():
#             print(f"{city} -> Population: {stats['Population']} citizens, Gold: {stats['Gold']} kg")
#         break
#     elif action == "Plunder":
#             name_of_city = params[0]
#             people = int(params[1])
#             money = int(params[2])
#             pirates_dict=Plunder(pirates_dict,name_of_city,people,money)
#
#     elif action == "Prosper":
#         name_of_city = params[0]
#         money = int(params[1])
#         pirates_dict=Prosper(pirates_dict,name_of_city,money)




# pirates = {}
#
# def Populate_dict_of_pirates(pirates_dict):
#     while True:
#         command, *params = input().split("||")
#         if command == "Sail":
#             break
#
#         city = command
#         population = int(params[0])
#         gold = int(params[1])
#         if city not in pirates.keys():
#             pirates[city] = {"Population": population, "Gold": gold}
#         else:
#             pirates[city]["Population"] += population
#             pirates[city]["Gold"] += gold
#     return pirates_dict
#
# def Plunder(pirates_dict, city_target, people, money_for_taken):
#     pirates_dict[city_target]["Population"] -= people
#     pirates_dict[city_target]["Gold"] -= money_for_taken  # Fix variable name here
#     print(f"{city_target} plundered! {money_for_taken} gold stolen, {people} citizens killed.")
#
#     if pirates_dict[city_target]["Population"] <= 0 or pirates_dict[city_target]["Gold"] <= 0:
#         del pirates_dict[city_target]
#         print(f"{city_target} has been wiped off the map!")
#     return pirates_dict
#
# def Prosper(pirates_dict, city_target, money_for_taken):
#     if money_for_taken < 0:  # Fix variable name here
#         print("Gold added cannot be a negative number!")
#     else:
#         pirates_dict[city_target]["Gold"] += money_for_taken  # Fix variable name here
#         print(f'{money_for_taken} gold added to the city treasury. {city_target} now has {pirates_dict[city_target]["Gold"]} gold.')
#     return pirates_dict
#
#
# def main():
#     pirates_dict = Populate_dict_of_pirates(pirates)
#
#     while True:
#         action, *params = input().split("=>")
#         if action == "End":
#             if len(pirates)>0:
#                 print(f"Ahoy, Captain! There are {len(pirates_dict)} wealthy settlements to go to:")
#                 for city, stats in pirates_dict.items():
#                     print(f"{city} -> Population: {stats['Population']} citizens, Gold: {stats['Gold']} kg")
#             else:
#                 print("Ahoy, Captain! All targets have been plundered and destroyed!")
#             break
#         elif action == "Plunder":
#             name_of_city = params[0]
#             people = int(params[1])
#             money = int(params[2])
#             pirates_dict = Plunder(pirates_dict, name_of_city, people, money)
#         elif action == "Prosper":
#             name_of_city = params[0]
#             money_for_taken = int(params[1])  # Fix variable name here
#             pirates_dict = Prosper(pirates_dict, name_of_city, money_for_taken)
#
#
# main()
cities = {}

command = input()

while command != "Sail":
    tokens = command.split("||")
    town = tokens[0]
    people = int(tokens[1])
    gold = int(tokens[2])

    if town not in cities.keys():  # town not in cities (същото е)
        cities[town] = [people, gold]
    else:
        cities[town][0] += people
        cities[town][1] += gold
    command = input()

command = input()
while command != "End":
    tokens = command.split("=>")
    cmd = tokens[0]

    if cmd == "Plunder":
        town = tokens[1]
        people = int(tokens[2])
        gold = int(tokens[3])




        cities[town][0] -= people
        cities[town][1] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')

        if cities[town][0] <= 0 or cities[town][1] <= 0:
            cities.pop(town)
            print(f'{town} has been wiped off the map!')

    elif cmd == "Prosper":
        town = tokens[1]
        gold = int(tokens[2])

        if gold < 0:
            print(f'Gold added cannot be a negative number!')
        else:
            cities[town][1] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.')
    command = input()

if len(cities) > 0:


    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')



    for key, value in sorted(cities.items(), key=lambda x: (-x[1][1], -x[1][0])):
        print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')

else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')





