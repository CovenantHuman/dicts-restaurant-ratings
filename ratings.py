"""Restaurant rating lister."""
import random

def read_ratings(filename):
    """Alphabetize and print restaurant ratings

    Arguments: a file with restaurant ratings
    Return: None """
    ratings = open(filename)


    ratings_dict = {}
    for line in ratings:
        line = line.rstrip()
        restaurant, rating = line.split(":")
        ratings_dict[restaurant] = rating 

    user_choice = 0
    while user_choice != "q":
        print("""
        If you want to:
            see a list of all the restaurants and ratings ENTER 1
            add a rating of your own ENTER 2
            change the rating of a random restaurant ENTER 3
            change the rating of a specific restaurant ENTER 4
            quit ENTER q
        """)
        user_choice = input("-> ")
        if user_choice == "2":
            user_restaurant = input("Please enter a restaurant: ")
            user_rating = input("Please give your rating: ")

            while True: 
                try:
                    if int(user_rating) > 5 or int(user_rating) < 1:
                        user_rating = input("Please give a rating between 1 and 5: ")
                    else:
                        break
                except ValueError:
                    user_rating = input("Please enter a number between 1 and 5: ")

            ratings_dict[user_restaurant] = user_rating
        elif user_choice == "1":
            alphabetical_list = sorted(ratings_dict.items())
            
            for item in alphabetical_list:
                print(item[0] + " is rated at " + item[1])
        elif user_choice == "3":
            restaurant_list = list(ratings_dict.keys())
            random_restaurant = random.choice(restaurant_list)
            print("The restaurant is", random_restaurant)
            print(random_restaurant + "'s current rating is " 
            + ratings_dict[random_restaurant])
            user_rating = input("What would you like to rate it: ")
            while True: 
                try:
                    if int(user_rating) > 5 or int(user_rating) < 1:
                        user_rating = input("Please give a rating between 1 and 5: ")
                    else:
                        break
                except ValueError:
                    user_rating = input("Please enter a number between 1 and 5: ")
            ratings_dict[random_restaurant] = user_rating
        elif user_choice == "4":
            pass
        

read_ratings('scores.txt')