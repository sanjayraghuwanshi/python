# Code to produce an error -> NameError: name 'a_variable' is not defined

def a_function(a_parameter):
    a_variable = 15
    return a_parameter
a_function(10)
print (a_variable)