"""Restaurant rating lister."""

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
        

read_ratings('scores.txt')