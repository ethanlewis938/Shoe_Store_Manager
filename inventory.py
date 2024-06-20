from tabulate import tabulate 
import os

END_COLOR = "\033[0m"
RED_COLOR = "\033[31m"
UNDERLINE_STYLE = "\033[4m"
GREEN_COLOR = "\033[32m"

script_dir = os.path.dirname(os.path.abspath(__file__))
rel_path = "inventory.txt"
abs_file_path = os.path.join(script_dir, rel_path)

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
shoe_list = []

# Function to read data from the inventory file
def read_shoes_data():
    try:
        with open(abs_file_path, "r") as file:
            next(file)  # Skip the first line
            for line in file:
                if line.strip():  # Ensure it's not an empty line
                    country, code, product, cost, quantity = line.strip().split(",")
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)

    except FileNotFoundError:
        print("The 'inventory.txt' file does not exist.")

'''
This function will open the file inventory.txt
and read the data from this file, then create a shoes object with this data
and append this object into the shoes list. One line in this file represents
data to create one object of shoes. You must use the try-except in this function
for error handling. Remember to skip the first line using your code.
'''

# Function to capture new shoe data
def capture_shoes():
    try:
        while True:
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
                            with open("inventory.txt", "a") as file:
                                shoe = Shoe(user_country, user_shoe_code, user_product_name, user_shoe_cost, user_shoe_quantity)
                                file.write(f"\n{user_country},{user_shoe_code},{user_product_name},{user_shoe_cost},{user_shoe_quantity}")
                                shoe_list.append(shoe)
                                print("Data written successfully.")
                                break
    except ValueError:
        print("ERROR")

'''
This function will allow a user to capture data
about a shoe and use this data to create a shoe object
and append this object inside the shoe list.
'''

# Function to view all shoes
def view_all():
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    shoe_data = []
    for shoe in shoe_list:
        shoe_data.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
    print(tabulate(shoe_data, headers=headers))

'''
This function will iterate over the shoes list and
print the details of the shoes returned from the __str__
function. Optional: you can organize your data in a table format
by using Python’s tabulate module.
'''

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
        
        user_quantity_amount = input("Please enter the shoe quantity that you want to update: ")
        lowest_quantity_shoe[4] = user_quantity_amount  # Update the quantity
        
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

'''
This function will find the shoe object with the lowest quantity,
which is the shoes that need to be re-stocked. Ask the user if they
want to add this quantity of shoes and then update it.
This quantity should be updated on the file for this shoe.
'''

# Function to search for a shoe by code
def search_shoe():
    user_shoe_search = input("Please enter a shoe code to search: ")
    found = False
    for shoe in shoe_list:
        if shoe.code == user_shoe_search:
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
            calculation = int(cost) * int(quantity)
            data.append([product, calculation])

    headers = ["Item Name", "Item Amount"]
    print(tabulate(data, headers=headers))

'''
This function will calculate the total value for each item.
Please keep the formula for value in mind: value = cost * quantity.
Print this information on the console for all the shoes.
'''

# Function to find the shoe with the highest quantity
def highest_qty():
    highest_quantity_shoe = None
    highest_quantity = float('-inf')

    with open("inventory.txt", "r") as file:
        lines = file.readlines()

    for line in lines[1:]:  # Skip the header line
        country, code, product, cost, quantity = line.strip().split(",")
        quantity = int(quantity)
        if quantity > highest_quantity:
            highest_quantity = quantity
            highest_quantity_shoe = [country, code, product, cost, quantity]

    print(f"Shoe:{highest_quantity_shoe[2]} is for sale for ${highest_quantity_shoe[3]}")

'''
Write code to determine the product with the highest quantity and
print this shoe as being for sale.
'''

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

'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
