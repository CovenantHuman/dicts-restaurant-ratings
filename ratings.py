"""Restaurant rating lister."""

def read_ratings(filename):
    ratings = open(filename)
    ratings_dict = {}
    for line in ratings:
        restaurant, rating = line.split(":")
        ratings_dict[restaurant] = rating 

    alphabetical_list = sorted(ratings_dict.items())
    
    for item in alphabetical_list:
        print(item[0] + " is rated at " + item[1])

read_ratings('scores.txt')