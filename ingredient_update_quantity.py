import csv

def update_food_quantity(food):
    lines = list()
    
    # write contents of csv file to list. Remove previous food/quantity and add updated food/quantity to lines(list):
    with open('food_list.csv', 'r') as readFile:
        reader = csv.reader(readFile)            #reader object that iterates over lines in csv file.
        for row in reader:                       #iterates through every row
            lines.append(row)                    #append each row into list "lines"
            for field in row:                    #iterates through every field in row
                if field == food[0]:             #if field string matches name we wish to update
                    lines.remove(row)            #remove that row from lines(list)
                    lines.append(food)           #add updated row to lines(list)
    
    # rewrite updated list(lines) back to csv file:
    with open('food_list.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
