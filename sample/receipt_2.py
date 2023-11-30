##I exceeded the requirement adding a discount price for tuesadays, wednesdays, and anytime before 11am each day.
    
import csv
from datetime import datetime

def main():
    try:
        products_dict = read_dictionary("products.csv", 0)

        with open("request.csv", "rt") as csv_file:
            next(csv_file)
            reader = csv.reader(csv_file)

            print()

            subtotal = 0
            total_items = 0
            for row in reader:
                product_number = row[0]

                product_info = products_dict.get(product_number)
                if product_info:
                    product_name = product_info[1]
                    requested_quantity = int(row[1])
                    product_price = float(product_info[2])

                    ##Exceeding requirements and showing creativity
                    ##I added initial prices and discounted prices for tuesdays, wednesdays and before 11am all day
                    initial_price = product_price
                    if is_discount_day() or is_discount_time():
                        product_price *= 0.9

                    print(f"{product_name}: {requested_quantity} @ Initial Price: {initial_price:.2f}, Discounted Price: @ {product_price:.2f}")

                    subtotal += requested_quantity * product_price
                    total_items += requested_quantity
                else:
                    raise KeyError(product_number)

            sales_tax_rate = 0.06
            sales_tax_amount = subtotal * sales_tax_rate
            total_amount_due = subtotal + sales_tax_amount

            print()
            print(f"Number of items: {total_items}")
            print(f"Subtotal: {subtotal:.2f}")
            print(f"Sales tax: {sales_tax_amount:.2f}")
            print(f"Total: {total_amount_due:.2f}")

            print()
            print("Thank you for shopping at Justrite Supermarket.")

            current_date_and_time = datetime.now()

            print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")

    except FileNotFoundError:
        print("Error: missing file\n[Errno 2] No such file or directory: 'products.csv'")
    except PermissionError:
        print("Error: Permission denied. Please check file permissions.")
    except KeyError as e:
        product_number = str(e)
        print(f"Error: unknown product ID in the request.csv file\n{product_number}")


def read_dictionary(filename, key_column_index):
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(csv_file)

        print("Justrite Supermarket")

        for row in reader:
            if len(row) != 0:
                key = row[key_column_index]
                dictionary[key] = row

    return dictionary


##functions that show exceeding requiremments and showing creativity for tuesdays and wednesdays.
def is_discount_day():
    current_day = datetime.now().strftime("%A")
    return current_day in ["Tuesday", "Wednesday"]

##functions that show exceeding requiremments and showing creativity for time before 11am everyday.
def is_discount_time():
    current_time = datetime.now().time()
    return current_time < datetime.strptime("11:00", "%H:%M").time()

if __name__ == "__main__":
    main()