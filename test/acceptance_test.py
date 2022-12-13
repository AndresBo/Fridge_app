import sys
sys.path.append('../fridge_app')

from build_set_food_names import build_set_name

for_test_food_list = 'test_csv.csv'

# test build_set_name outputs correct set give a test csv file with known rows. 
def test_build_set_name_elements():     
    result = build_set_name(for_test_food_list)
    assert ("capsicum" in result) & ("sausages" in result)

# test build_set_name outputs set with the correct lenght
def test_build_set_name_lenght():     
    result = build_set_name(for_test_food_list)
    assert len(result) == 2

    
