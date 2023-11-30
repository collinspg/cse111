import csv
from datetime import datetime
def main():
    products_dict = read_dictionary("products.csv", 0)
    print(products_dict)
    
    with open("request.csv", "rt") as csv_file:
        next(csv_file)
        reader = csv.reader(csv_file)
        
        print()
        print("Requested Items")
        
        
        for row in reader:
            product_number = row[0]
            product_info = products_dict.get(product_number)
            if product_info:
                product_name = product_info[1]
                requested_quantity = int(row[1])
                product_price = float(product_info[2])

                print(f"{product_name}: {requested_quantity} @ {product_price}")
              
        
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(csv_file)
        
        print("All Products")
        for row in reader:
            if len(row) != 0:
                key = row[key_column_index]
                dictionary[key] = row
                

    return dictionary


if __name__ == "__main__":
    main()
        
        
