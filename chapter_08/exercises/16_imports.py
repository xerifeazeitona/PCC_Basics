"""
8-16. Imports
Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program
file, and call the function using each of these approaches:

import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""
print('\n# import module_name')
import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
printing_functions.print_models(unprinted_designs, completed_models)

print('\n# from module_name import function_name')
from printing_functions import print_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)

print('\n# from module_name import function_name as fn')
from printing_functions import print_models as pm

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
pm(unprinted_designs, completed_models)

print('\n# import module_name as mn')
import printing_functions as pf

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
pf.print_models(unprinted_designs, completed_models)

print('\n# from module_name import *')
from printing_functions import *

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
