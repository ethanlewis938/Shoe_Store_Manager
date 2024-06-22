# Shoe Store Stock Panel 👟

## Table of Contents

- [Description and Content](#description-and-content)
- [Installation](#installation)
- [Usage](#usage)
  - [Example Interaction](#example-interaction)
- [Installation](#Repository-Link)
- [Credits](#credits)

## Description and Content

This Python program is designed for a shoe store manager to efficiently manage inventory and sales operations. It includes several functionalities such as reading shoe data from a file, capturing new shoe data, viewing all shoe details, and identifying shoes that need restocking. The program can also search for shoes by code, calculate the total value of each shoe based on cost and quantity, and highlight shoes with the highest quantity for sale. Additionally, the program provides a user-friendly menu to execute these functions, ensuring smooth and effective management of the shoe store’s inventory.

## Installation

To install and run this project locally, follow these steps:

1. **Clone the repository in your terminal/command prompt**:

    - Make sure you have created a temporary folder for this repository.

   ```sh
   git clone https://github.com/ethanlewis938/Shoe_Store_Manager
   ```
2. **Navigate to the project directory**:

   ```sh
   cd temporyFile/Shoe_Store_Manager/
   ```
3. **Run the program**:

   - On Windows:
     ```sh
     python inventory.py
     ```
   - On Mac:
     ```sh
     python3 inventory.py
     ```

## Usage

After installing the project, you can use it by following these steps:

1. **Run the program**:

   - On Windows:
     ```sh
     python inventory.py
     ```
   - On Mac:
     ```sh
     python3 inventory.py
     ```
**2. Interact with the program**

  Firstly, the program will give you a list of prompts to enter.

  1. Capture Shoes: Enter new shoe details (country, code, product, cost, quantity) to add to the inventory.
  2. View All Shoes: Display all shoe details in a table format.
  3. Re-Stock: Find the shoe with the lowest quantity and update its stock.
  4. Search Shoe: Search for a shoe by its code and display its details.
  5. Value Per Item: Calculate and display the total value of each shoe (cost × quantity).
  6. Highest Quantity Shoe: Identify and display the shoe with the highest quantity.
  7. Exit: Exit the program.

### Example Interaction


**- Main User Prompt**

![Program Screenshot](images/menuPrompt.png)
<br>

**- Option One Test**

![Program Screenshot](images/optionOnePrompt.png)
<br>

**- Error Handling**
![Program Screenshot](images/ErrorHandling.png)

## Credits

Lead Programmer

- Ethan Lewis [GitHub Profile](https://github.com/ethanlewis938/)

## Repository Link

[View the Repository](https://github.com/ethanlewis938/Shoe_Store_Manager)
