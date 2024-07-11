# Function to print pyramid pattern of numbers
def print_number_pyramid(rows):
    # Outer loop for number of rows
    for i in range(1, rows + 1):
        # Inner loop for printing numbers
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Example usage: printing a pyramid with 5 rows
print_number_pyramid(5)
