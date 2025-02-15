def function(a, b):
    try:
        return a + b
    except TypeError:
        print("Cannot add integer and string. Please provide only integers or strings.")
        return None

result = function(1, '2')
result = function(1,2) 