import csv

list = []

# def enter_ingredient():
with open('food_list.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(list)
    f.close()
