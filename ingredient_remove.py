import csv
from return_lower_case_string import get_string
from build_set_food_names import build_set_name
# https://stackoverflow.com/questions/56987312/how-to-delete-only-one-row-in-csv-with-python
def remove_food_ask():
    food_to_remove = get_string()
    if food_to_remove is None:                #option to get back to start menu
        return
        
    set_of_food_in_list = build_set_name

def remove_food():
    
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
