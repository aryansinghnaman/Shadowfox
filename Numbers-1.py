def format_number(num, specifier):
    formatted = format(num, specifier)
    return formatted

# Call the function with 145 and 'o'
result = format_number(145, 'o')
print("Formatted Result:", result)
