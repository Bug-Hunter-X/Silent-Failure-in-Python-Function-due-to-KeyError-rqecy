def function_with_uncommon_error(data):
    try:
        result = data['key'] * 2  # potential KeyError
        return result
except KeyError:
    return 0

data = {}
result = function_with_uncommon_error(data)
print(result) # This will print 0, but a less experienced programmer might expect an error.