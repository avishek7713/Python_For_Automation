inputFile = open("inputFile.txt", "r") # reading the file 
passFile = open("passFile.txt", "w") # writing into file
failFile = open("failFile.txt", "w")

for line in inputFile:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)
    else:
        failFile.write(line)

inputFile.close()
passFile.close()
failFile.close()