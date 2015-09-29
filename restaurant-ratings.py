# your code goes here
# ratings = {}

# separate by :
# name = index[0] 
# score index 1

# ratings[name] = score

from random import randint


def print_sorted_ratings(ratings_dict):
    for name, score in sorted(ratings_dict.items()):
        print "{} is rated at {}.".format(name, score)

def get_rating(filename):
    """Get restaurant ratings from file and organize in alphabetical order"""

    open_file = open(filename)

    ratings = {}

    for item in open_file:
        item = item.strip()
        restaurant_data = item.split(':')

        name = restaurant_data[0]
        score = restaurant_data[1]

        ratings[name] = score

    print_sorted_ratings(ratings)

    open_file.close()

    name = raw_input('Enter the name of a restaurant: ')
    score = int(raw_input('Enter your rating of the restaurant from 1 to 5: '))

    ratings[name] = score

    print_sorted_ratings(ratings)



# def update_ratings(ratings_dict):

    username = raw_input("What's your name?: ")
    
    restaurant_names = ratings.keys()

    random_restaurant_index = randint(0, len(restaurant_names)-1)

    # print restaurant_names
    # print random_restaurant_index

    restaurant_to_update = restaurant_names[random_restaurant_index]

    print restaurant_to_update



    new_rating = int(raw_input(('{} is currently rated at {}. On a scale of 1 to 5, '
                                'how would you rate it?: ').format(restaurant_to_update, ratings[restaurant_to_update])))

    ratings[restaurant_to_update] = new_rating

    print_sorted_ratings(ratings)


get_rating('scores.txt')




