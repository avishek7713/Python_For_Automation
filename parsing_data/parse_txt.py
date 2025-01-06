file_path = "groceries.txt"

with open(file_path, "r") as file:
    data = file.read()

print("data:", data)
parsed_data = data.split(", ")
print("Parsed data: ", parsed_data)
print("Item at index 2: ", parsed_data[2])