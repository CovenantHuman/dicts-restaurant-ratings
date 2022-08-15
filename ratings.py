"""Restaurant rating lister."""

def read_ratings(filename):
    ratings = open(filename)


    ratings_dict = {}
    for line in ratings:
        line = line.rstrip()
        restaurant, rating = line.split(":")
        ratings_dict[restaurant] = rating 

    user_restaurant = input("Please enter a restaurant: ")
    user_rating = input("Please give your rating: ")

    ratings_dict[user_restaurant] = user_rating

    alphabetical_list = sorted(ratings_dict.items())
    
    for item in alphabetical_list:
        print(item[0] + " is rated at " + item[1])

read_ratings('scores.txt')