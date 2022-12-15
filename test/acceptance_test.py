import sys

sys.path.append('../fridge_app')

from build_set_food_names import build_set_name
from ingredients_list import list_foods

for_test_food_list = 'test_csv.csv'

# test build_set_name outputs correct set given a test csv file 
def test_build_set_name_elements():     
    result = build_set_name(for_test_food_list)
    assert ("capsicum" in result) & ("sausages" in result)

# test build_set_name outputs set with the correct lenght
def test_build_set_name_lenght():     
    result = build_set_name(for_test_food_list)
    assert len(result) == 2


#https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print
#test list_foods by asserting output 
def test_list_foods(capsys):
    list_foods(for_test_food_list)
    captured = capsys.readouterr()
    assert captured.out == 'capsicum 500\nsausages 100\n'
