# SI 201 HW4
# Your name: Rohan Karunakaran 
# Your student id: 80717574
# Your email: rohanvk@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): ChatGPT
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code

import csv

def load_sales(csv_filename):
    # load csv file into a list where each element in the list is a dictionary 
    # of the fields and their values of a single row
    with open(csv_filename, newline='') as file:
        reader = csv.reader(file)
        header = next(reader)     # first row has the column names

        data = []                 # empty list to hold dictionaries
        for current_row in reader:
            row_dict = {}
            for i in range(len(header)):
                column_name = header[i]
                column_value = current_row[i]
                row_dict[column_name] = column_value
            data.append(row_dict)

    return data

def calculate_percent_furniture(sales_list):
    # takes a list of sales where each element is a dictionary 
    # returns percentage of furniture sales 
    pass

def calculate_percent_sales_in_region_over_threshold(sales_list, region, threshold):
    # takes a list of sales where each element is a dictionary
    # calculates total sales where region is the specified region and sales value is over the threshold
    # returns percentage of count of sales over threshold within specified region
    pass

def generate_report(percent_furniture, percent_sales_in_region_over_threshold):
    # creates a text file containing the calculated values 
    pass

def main():
    sales_list = load_sales('SampleSuperstore.csv')
    first_row = sales_list[0]
    print(first_row)

def old_main():
    filename = 'SampleSuperstore.csv'

    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        # read and print names of columns 
        header = next(reader)
        print("Column names:", header)

        # print the number of rows
        rows = list(reader)
        print("Number of rows:", len(rows))

        # read and print first row
        first_row = rows[0]
        print("First row:", first_row)

        # calculate percent of furniture 
        column_name = 'Category'
        col_index = header.index(column_name)

        row_count = len(rows)
        furniture_count = 0
        for i in range(len(rows)):
            row = rows[i]
            category = row[col_index]
            if category == 'Furniture':
                furniture_count += 1
        furniture_percent = (furniture_count / row_count) * 100
        print(f"Percent of furniture categories: {furniture_percent:.2f}%")

        # calculate percent of count of sales over 100 in the west
        column_name_sales = 'Sales'
        col_index_sales = header.index(column_name_sales)

        column_name_region = 'Region'
        col_index_region = header.index(column_name_region)

        over_hundred_count = 0
        for i in range(len(rows)):
            current_row = rows[i]
            sales_region = current_row[col_index_region]
            if sales_region == 'West':
                sales_amount = float(current_row[col_index_sales])
                if sales_amount >= 100:
                    over_hundred_count += 1
        sales_percent = (over_hundred_count / row_count) * 100
        print(f"Percent of count of sales in the West over 100: {sales_percent:.2f}%")

        # Open a new text file in write mode
        with open('result.txt', 'w') as file:
            file.write(f"Percent of furniture categories: {furniture_percent:.2f}%\n")
            file.write(f"Percent of count of sales in the West over 100: {sales_percent:.2f}%\n")

main()

