import csv

# csv -> set
# build a set of current names in food_list.csv
def build_set_name():
    names_set = set()
    with open('food_list.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            names_set.add(f"{row['food']}")
    return names_set
