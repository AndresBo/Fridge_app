# Fridge_app


## Fridge app:
- Lists current food with quantity
- Enters new foods 
- Removes individual food items
- Updates food quantity


Link to [repository](https://github.com/AndresBo/Fridge_app)

Link to [presentation video](https://youtu.be/C-oEePfZsnI)

Styling guide used was [PEP 8](https://peps.python.org/pep-0008/)

## How to run Fridge
In the terminal type: ```./run_fridge.sh```. If it does not work follow the steps below:

1. On the terminal type: ```python3 --version```
- If you get ```python3: command not found```, install python for Mac [here](https://wsvincent.com/install-python/#install-python-on-macos) or for WSl [here](https://wsvincent.com/install-python/#install-python-on-linux)
- If you have python you will get something like this: ```Python 3.8.10```. 
- If your python version does not start with a ```3```. Update python by following the links above.

2. Once you have python type: ```./run_fridge.sh``` to run the application


## References:
Source of how to [delete one row from a csv file in python](https://stackoverflow.com/questions/56987312/how-to-delete-only-one-row-in-csv-with-python)

Source of how to [test terminal output of list_foods function](https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print)


## Overview of app logic:

![fridge_app drawio](https://user-images.githubusercontent.com/85352176/208214781-e26fac12-a1ad-44b5-9d2c-fada5c4570ea.png)


## Inplementation plan:
<img width="831" alt="implement" src="https://user-images.githubusercontent.com/85352176/208222559-c6f80999-d87e-4b97-aa44-de75d381fc9f.png">

## Additional notes about my learning process/project development:
- Initially the project was using OOP Classes. Due to time restrains I ended refactoring the code to normal functions. Frankly, I still don't understand OOP implementation.
- Breaking down code into smaller functions is very helpful. Makes debugging easier and the code more readable. 
- Still trying to wrap my head around TDD, I get the basic premise but the implementation still eludes me. 
- Favorite part was learning to handle external files like csv. This is the first time I code something that actually stores data.
- Wanted to add an extra function that would provide recepies based on available foods but time was a problem.


