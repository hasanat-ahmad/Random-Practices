# Number of rows and columns
rows = 3
cols = 3

# Loop through each row
for i in range(rows):
    # Loop through each column
    for j in range(cols):
        # Check if it's the 2nd row and 2nd column
        if i == 1 and j == 1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    # Move to the next line after each row
    print()

