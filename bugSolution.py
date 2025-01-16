def function_with_uncommon_error(data):
    try:
        result = data['key'] * 2
        return result
    except KeyError as e:
        print(f"KeyError encountered: {e}")
        return None # Explicit handling for the error condition

data = {}
result = function_with_uncommon_error(data)
print(result) # This will print None and also inform about the KeyError