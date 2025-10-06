# SI 201 HW4
# Your name: Rohan Karunakaran 
# Your student id: 80717574
# Your email: rohanvk@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): ChatGPT
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code

import csv

def main():
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

        # calculate percent of sales over 100
        column_name_sales = 'Sales'
        col_index_sales = header.index(column_name_sales)

        over_hundred_count = 0
        for i in range(len(rows)):
            current_row = rows[i]
            sales_amount = float(current_row[col_index_sales])
            if sales_amount >= 100:
                over_hundred_count += 1
        sales_percent = (over_hundred_count / row_count) * 100
        print(f"Percent of sales over 100: {sales_percent:.2f}%")

main()

