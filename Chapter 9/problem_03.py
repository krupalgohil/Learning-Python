def generatetable(n):
    # Create an empty string to store the table
    table = ""
    
    # Generate multiplication table from 1 to 10
    for i in range(1, 11):
        table += f"{n} * {i} = {n*i}\n"
    
    # Save the table in a file with dynamic name using f-string
    with open(f"chapter 9\\tables\\table_{n}.txt", "w") as f:
        f.write(table)

# Generate tables from 2 to 21
for i in range(2, 22):
    generatetable(i)
