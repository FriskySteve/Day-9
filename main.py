from art import logo
from replit import  clear

# # Start od fay 9 - dictionaries
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
#
# # Retrieving itmes from dictionary
# print(programming_dictionary["Function"])
#
# # Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)
#
# # Create an empty dictionary
# empty_dictionary = {}
#
# # Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)
#
# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "Its not a bug"
# print(programming_dictionary)
#
# # Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
#
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# # TODO-1: Create an empty dictionary called student_grades.
#
# student_grades = {}
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
#
# for key in student_scores:
#     if 100 >= student_scores[key] >= 91:
#         student_grades[key] = "Outstanding"
#     elif 90 >= student_scores[key] >= 81:
#         student_grades[key] = "Exceeds Exoectations"
#     elif 80 >= student_scores[key] >= 71:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
#
# # 🚨 Don't change the code below 👇
# print(student_grades)

# # Nestingca List in a Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Poland": ["Lodz", "Warszawa", "Breslav"],
# }

# Nesting Dictionary in a Dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Poland": {"cities_visited": ["Lodz", "Warszawa", "Breslav"], "total_visits": 5},
# }

# # Nesting Dictionary in a List
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Poland",
#         "cities_visited": ["Lodz", "Warszawa", "Breslav"],
#         "total_visits": 5
#     },
# ]
#
# # Exercise
# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
#
#
# # 🚨 Do NOT change the code above
#
# # TODO: Write the function that will allow new countries
# # to be added to the travel_log. 👇
# def add_new_country(country, visits, cities):
#     new_entry = {}
#     new_entry["country"] = country
#     new_entry["visits"] = visits
#     new_entry["cities"] = cities
#     travel_log.append(new_entry)
#
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# Final project of a day - The Secret Auction

print(logo)
auction = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_ammount = bidding_record[bidder]
        if bid_ammount > highest_bid:
            highest_bid = bid_ammount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


def secret_auction():
    name = input("What is your name?")
    bid_price = int(input("What is you bid price? $"))
    auction[name] = bid_price
    x = (input("Is there any other bidders? Type 'Yes' or 'No'")).lower()
    if x == "yes":
        clear()
        secret_auction()
    else:
        find_highest_bidder(auction)


secret_auction()