import csv

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

    #rewrite whole list back to csv file
    with open('food_list.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
