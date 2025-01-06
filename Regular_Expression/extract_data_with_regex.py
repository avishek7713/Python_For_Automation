import re 

phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

example = "The number is 123-456-7890."

result = phoneRegex.search(example)

if result:
    print("Phone number found: ", result.group())
    print("Area Code: ", result.group()[0:3])