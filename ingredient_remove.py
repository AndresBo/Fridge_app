import csv
# https://stackoverflow.com/questions/56987312/how-to-delete-only-one-row-in-csv-with-python
def remove_food(foodRemove):
    lines = list()
    
    # write contents of csv file to list, ommiting row we wish to delete
    with open('food_list.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == foodRemove:
                    lines.remove(row)

    #rewrite updated list back to csv file
    with open('food_list.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)