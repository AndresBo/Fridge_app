import csv

def remove_food():
    lines = list()
    update_food = ["capsicum",500]
    # write contents of csv file to list and remove + add updated [food,quantity]
    with open('food_list.csv', 'r') as readFile:
        reader = csv.reader(readFile)            #reader object that iterates over lines in csv file.
        for row in reader:                       #iterates through every row
            lines.append(row)                    #append each row into list "lines"
            for field in row:                    #iterates through every field in row
                if field == "capsicum":          #
                    lines.remove(row)
                    lines.append(update_food)
    #return lines
    #rewrite updated list back to csv file
    with open('food_list.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)


remove_food()
