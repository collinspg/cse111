
import csv

def read_dictionary(filename):
    """
    Read the contents of a CSV file into a dictionary and return the dictionary.

    Parameters:
        filename (str): The name of the CSV file to read.

    Returns:
        dict: A dictionary that contains the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            i_number, name = row
            i_number = i_number.replace('-', '')  # Remove dashes from I-Numbers
            dictionary[i_number] = name
    return dictionary

def main():
    
    filename = 'students.csv'
    dictionary = read_dictionary(filename)

    i_number = input("Please enter an I-Number (xxxxxxxxx): ")
    name = dictionary.get(i_number)
    if name is not None:
        print(name)
    else:
        print("No such student")

if __name__ == '__main__':
    main()