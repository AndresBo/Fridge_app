import csv
# https://stackoverflow.com/questions/56987312/how-to-delete-only-one-row-in-csv-with-python

def remove_food():
    food_remove = input("Enter name of food you wish to remove or 'quit' to head back to main menu: ").lower().strip()

    lines = list()
    
    # write contents of csv file to list, ommiting row we wish to delete
    with open('food_list.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == food_remove:
                    lines.remove(row)

    #rewrite whole list back to csv file
    with open('food_list.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)


remove_food()
