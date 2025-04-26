favorite_foods = ["Pizza", "Burger", "Ice Cream"]

food_ratings = []

def get_rating(food):
    while True: 
        print("Rate", food, "on a scale of 1 (being the worst), to 5 (being the best):")
        rating = input()
        if rating in ["1", "2", "3", "4", "5"]:
            if rating == "5":
                print("Wow, you really like", food, "!")
            return rating
        else:
            print("Please enter a number from 1 to 5.")

for food in favorite_foods:
    rating = get_rating(food)
    food_ratings.append(rating)

print("Here are your ratings:")
for i in range(len(favorite_foods)):
    print(favorite_foods[i], ":", food_ratings[i])
