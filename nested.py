# Define the height of the pyramid
rows = 5

# Initialize the row counter for the outer loop
current_row = 1

# Outer loop: controls the number of rows
while current_row <= rows:
    # Print leading spaces
    spaces = rows - current_row
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    
    # Print asterisks
    stars = 2 * current_row - 1
    while stars > 0:
        print("*", end="")
        stars -= 1
    
    # Move to the next line after finishing a row
    print()
    
    # Increment the row counter
    current_row += 1