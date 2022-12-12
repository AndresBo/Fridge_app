import csv

new_food = ["banana",6]

# def enter_ingredient():
def add_new_ingredient():
    with open('food_list.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(new_food)
        f.close()

add_new_ingredient()
