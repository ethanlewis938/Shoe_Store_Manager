from tabulate import tabulate
import os

# Color and style codes for terminal output
END_COLOR = "\033[0m"
RED_COLOR = "\033[31m"
UNDERLINE_STYLE = "\033[4m"
GREEN_COLOR = "\033[32m"

# Paths to the script and inventory file
script_directory = os.path.dirname(os.path.abspath(__file__))
relative_path = "inventory.txt"
absolute_file_path = os.path.join(script_directory, relative_path)

# Define the Shoe class
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country} {self.code} - {self.product}: ${self.cost}, Quantity: {self.quantity}"

# List to store shoe objects
shoes_list = []

# Function to read data from the inventory file
def read_shoes_data():
    try:
        with open(absolute_file_path, "r") as file:
            next(file)  # Skip the first line (header)
            for line in file:
                if line.strip():  # Ensure it's not an empty line
                    country, code, product, cost, quantity = line.strip().split(",")
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoes_list.append(shoe)

    except FileNotFoundError:
        print("The 'inventory.txt' file does not exist.")

# Function to capture new shoe data
def capture_shoes():
    try:
        while True:
            # Get input from user and validate it
            user_country = input("Please enter the country of where the shoe is from: ")
            if not user_country.isalpha():
                print(f"{RED_COLOR}[INVALID INPUT]{END_COLOR} Country must contain only letters!")
            else:
                user_shoe_code = input("Please enter the shoe code: ")
                if not user_shoe_code.isdigit():
                    print(f"{RED_COLOR}[INVALID INPUT]{END_COLOR} Shoe code must contain only digits!")
                else:
                    user_product_name = input("Please enter the product name: ")
                    user_shoe_cost = input("Please enter the cost of the shoe: ")
                    if not user_shoe_cost.replace('.', '', 1).isdigit():
                        print(f"{RED_COLOR}[INVALID INPUT]{END_COLOR} Cost must be a numeric value!")
                    else:
                        user_shoe_quantity = input("Please enter the quantity of the shoe: ")
                        if not user_shoe_quantity.isdigit():
                            print(f"{RED_COLOR}[INVALID INPUT]{END_COLOR} Quantity must be a whole number!")
                        else:
                            # Write new shoe data to file and append to list
                            with open("inventory.txt", "a") as file:
                                shoe = Shoe(user_country, user_shoe_code, user_product_name, user_shoe_cost, user_shoe_quantity)
                                file.write(f"\n{user_country},{user_shoe_code},{user_product_name},{user_shoe_cost},{user_shoe_quantity}")
                                shoes_list.append(shoe)
                                print("Data written successfully.")
                                break
    except ValueError:
        print("ERROR")

# Function to view all shoes
def view_all():
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    shoe_data = []
    # Collect shoe data for display
    for shoe in shoes_list:
        shoe_data.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
    # Display shoe data in table format
    print(tabulate(shoe_data, headers=headers))

# Function to restock shoes
def re_stock():
    lowest_quantity_shoe = None
    lowest_quantity = float('inf')

    # Read all lines from the file
    with open("inventory.txt", "r") as file:
        lines = file.readlines()

    # Find the shoe with the lowest quantity
    for line in lines[1:]:  # Skip the header line
        country, code, product, cost, quantity = line.strip().split(",")
        quantity = int(quantity)
        if quantity < lowest_quantity:
            lowest_quantity = quantity
            lowest_quantity_shoe = [country, code, product, cost, quantity]

    if lowest_quantity_shoe is not None:
        print(f"{RED_COLOR}{UNDERLINE_STYLE}Item needs restocking{END_COLOR}\n")
        print(f"Shoe Name: {lowest_quantity_shoe[2]} | Quantity: {lowest_quantity_shoe[4]}")
        
        new_quantity = input("Please enter the shoe quantity that you want to update: ")
        lowest_quantity_shoe[4] = new_quantity  # Update the quantity
        
        # Construct the updated line
        updated_line = f"{lowest_quantity_shoe[0]}, {lowest_quantity_shoe[1]}, {lowest_quantity_shoe[2]}, {lowest_quantity_shoe[3]}, {lowest_quantity_shoe[4]}\n"
        
        # Find the index of the line that needs to be updated
        index = lines.index([line for line in lines if line.startswith(lowest_quantity_shoe[0])][0])
        
        # Update the line in the list of lines
        lines[index] = updated_line
        
        # Write the updated lines back to the file
        with open("inventory.txt", "w") as file:
            file.writelines(lines)
        
        print("Quantity updated successfully.")
    else:
        print("No shoes in the inventory.")

# Function to search for a shoe by code
def search_shoe():
    search_code = input("Please enter a shoe code to search: ")
    found = False
    for shoe in shoes_list:
        if shoe.code == search_code:
            print("Shoe Found:")
            print(shoe)
            found = True
            break

    if not found:
        print("Shoe not found.")

# Function to calculate the value per item
def value_per_item():
    data = []
    # Read all lines from the files
    with open("inventory.txt", "r") as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip the header line
            country, code, product, cost, quantity = line.strip().split(",")
            item_value = int(cost) * int(quantity)
            data.append([product, item_value])

    headers = ["Item Name", "Item Amount"]
    print(tabulate(data, headers=headers))

# Function to find the shoe with the highest quantity
def highest_qty():
    most_stocked_shoe = None
    highest_quantity = float('-inf')

    # Read all lines from the file
    with open("inventory.txt", "r") as file:
        lines = file.readlines()

    # Find the shoe with the highest quantity
    for line in lines[1:]:  # Skip the header line
        country, code, product, cost, quantity = line.strip().split(",")
        quantity = int(quantity)
        if quantity > highest_quantity:
            highest_quantity = quantity
            most_stocked_shoe = [country, code, product, cost, quantity]

    print(f"Shoe: {most_stocked_shoe[2]} is for sale for ${most_stocked_shoe[3]}")

# Function to display the main menu
def main_menu():
    read_shoes_data()
    while True:
        print("===== Main Menu =====")
        print("1. Capture Shoes")
        print("2. View All Shoes")
        print("3. Re-Stock")
        print("4. Search Shoe")
        print("5. Value Per Item")
        print("6. Highest Quantity Shoe")
        print("7. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            capture_shoes()
        elif choice == "2":
            view_all()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Example usage:
main_menu()