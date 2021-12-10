# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <Slai>,<2021-12-08>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Slai>,<2021-12-08>,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to the Product class
    def add_to_product(self, product_name, product_price):
        ls_append = [product_name, product_price]
        lstOfProductObjects.append(ls_append)
        return lstOfProductObjects
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Slai>,<2021-12-08>,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to process data from a file
    # TODO: Add Code to process data to a file
    def save_data_to_file(self, file_name, list_of_data):
        objFile = open(file_name,"w")
        for row in list_of_data:
            objFile.write(str(row[0]) + "," + str(row[1]) + "\n")
        objFile.close()
        print("Data Saved")

    def read_data_from_file(self, file_name):
        list_of_rows=[]
        objFile = open(file_name, "r")
        for line in objFile:
            list_of_rows.append(line.split(','))
        return list_of_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """Processes data to allow menu choice, show data, or add data
        output_menu_tasks(): -> return nothing
        input_menu_choices(): -> show menu choices
        print_products_in_list(list_of_rows): -> return nothing
        add_data(): -> returns product inputs
    changelog: (When,Who,What)
        Slai,12.8.2021, Wrote functions
    """
    pass
    # TODO: Add code to show menu to user ## show menu
    def output_menu_tasks(self):
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show Current Data in file
        2) Add Data
        3) Show staged data    
        4) Save Data to File and Exit     
        ''')
        print()  # Add an extra line for looks
    # TODO: Add code to get user's choice ## Show specific item
    def input_menu_choice(self):
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice
    # TODO: Add code to show the current data from the file to user ## Show current data
    def print_products_in_list(self, list_of_rows):
        for row in list_of_rows:
            print(row)

    # TODO: Add code to get product data from user ## Add data
    def add_data(self):
        strProductInput = input("\tPlease enter a product:").lower()
        strPriceInput = input("\tPlease enter a price:").lower()
        ls_append = [strProductInput, strPriceInput]
        print(ls_append)
        return [strProductInput, strPriceInput]

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

while(True):
    # Load data from file into a list of product objects when script starts
    fProcessor = FileProcessor()
    lstOfProductObjects=fProcessor.read_data_from_file(file_name='test_file.txt')
    # Show user a menu of options
    Input = IO()
    Input.output_menu_tasks()
    pProduct = Product()
    # Get user's menu option choice
    print("Please enter your choice.")
    choice_str = Input.input_menu_choice()

    if choice_str == '1':
        Input.print_products_in_list(list_of_rows=lstOfProductObjects)
    elif choice_str == '2':
        new_data=Input.add_data()
        staged_data=pProduct.add_to_product(new_data[0], new_data[1])
    elif choice_str == '3':
        Input.print_products_in_list(list_of_rows=staged_data)
    elif choice_str == '4':
        fProcessor.save_data_to_file(file_name='test_file.txt', list_of_data=staged_data)
        break

# Show user current data in the list of product objects
# Let user add data to the list of product objects
# let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #

