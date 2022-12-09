import pytest
from return_integer import get_int
# class TestingIngredients:
#     def test_ingredients_count():
#         items = {
#           "bananas":1,
#           "pears":4,
#         }             
#     items_count

def test_get_int():
    with pytest.raises(ValueError):
        get_int()
