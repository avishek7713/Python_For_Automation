try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("The result is: ", result)
except ValueError:
    print("You must enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")


#### USING ASSERT STATEMENT

# years = [1925, 1943, 1968, 1934, 1952]
# years.reverse()
# print(years)
# assert years[0] <= years[-1], "First element is greater than the last element."

# Fixing the error using sort() instead of reverse()
years = [1925, 1943, 1968, 1934, 1952]
years.sort()
print(years)
assert years[0] <= years[-1], "First element is greater than the last element."