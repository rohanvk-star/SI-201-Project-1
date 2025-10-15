# SI 201 HW4
# Your name: Rohan Karunakaran 
# Your student id: 80717574
# Your email: rohanvk@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): ChatGPT
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code

import csv
import unittest

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
                if column_name == "Sales":
                    column_value = float(current_row[i])
                else:
                    column_value = current_row[i]
                row_dict[column_name] = column_value
            data.append(row_dict)

    return data

def calculate_percent_furniture(sales_list):
    # takes a list of sales where each element is a dictionary 
    # returns percentage of furniture sales 

    # Handle corner case
    if len(sales_list) == 0:
        return 0
    
    furniture_count = 0
    for i in range(len(sales_list)):
        item = sales_list[i]
        category = item["Category"]
        if category == "Furniture":
            furniture_count += 1
    percentage = (furniture_count / len(sales_list)) * 100
    return percentage

def calculate_percent_sales_in_region_over_threshold(sales_list, region, threshold):
    # takes a list of sales where each element is a dictionary
    # calculates total sales where region is the specified region and sales value is over the threshold
    # returns percentage of count of sales over threshold within specified region

    # Handle corner case
    if len(sales_list) == 0:
        return 0
    
    over_hundred_count = 0
    for i in range(len(sales_list)):
        current_item = sales_list[i]
        sales_region = current_item["Region"]
        if sales_region == region:
            sales_amount = current_item["Sales"]
            if sales_amount >= threshold:
                over_hundred_count += 1
    sales_percent = (over_hundred_count / len(sales_list)) * 100
    return sales_percent

def generate_report(percent_furniture, percent_sales_in_region_over_threshold):
    # creates a text file containing the calculated values 
    # Open a new text file in write mode
    with open('result.txt', 'w') as file:
        file.write(f"Percent of furniture categories: {percent_furniture:.2f}%\n")
        file.write(f"Percent of count of sales in the West over 100: {percent_sales_in_region_over_threshold:.2f}%\n")

def main():
    sales_list = load_sales('SampleSuperstore.csv')
    first_row = sales_list[0]
    print("List of variables = ", first_row.keys())
    print("First row = ", first_row)
    print("Number of rows = ", len(sales_list))
    percent_furniture = calculate_percent_furniture(sales_list)
    print(f"Percent of furniture categories: {percent_furniture:.2f}%")
    sales_percent = calculate_percent_sales_in_region_over_threshold(sales_list, "West", 100)
    print(f"Percent of count of sales in the West over 100: {sales_percent:.2f}%")
    generate_report(percent_furniture, sales_percent)

# Unit tests

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.sales_list = load_sales('SampleSuperstore.csv')

    def test_percent_calculation(self):
        percent_furniture = calculate_percent_furniture(self.sales_list)
        self.assertAlmostEqual(percent_furniture, 21.222733640)

    def test_percent_calculation_threshold(self):
        sales_percent = calculate_percent_sales_in_region_over_threshold(self.sales_list, "West", 100)
        self.assertAlmostEqual(sales_percent, 12.6375825495)

    # Test edge case - pass an empty list 
    def test_percent_calculation_edge_case(self):
        sales_percent = calculate_percent_furniture([])
        self.assertAlmostEqual(sales_percent, 0)

    # Test edge case - unusually large threshold
    def test_percent_calculation_edge_case_two(self):
        sales_percent = calculate_percent_sales_in_region_over_threshold(self.sales_list, "West", 1000000)
        self.assertAlmostEqual(sales_percent, 0)

if __name__ == '__main__':
    unittest.main(exit=False)
    main()