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

# This function references the following fields: Sales, Category, and Ship Mode
def calculate_percent_category(sales_list, category, ship_mode):
    # takes a list of sales where each element is a dictionary 
    # returns percentage of sales in supplied category by ship_mode

    # Handle corner case
    if len(sales_list) == 0:
        return 0
    
    matching_count = 0
    for item in sales_list:
        if item["Category"] == category and item["Ship Mode"] == ship_mode:
            matching_count += 1
    percentage = (matching_count / len(sales_list)) * 100
    return percentage

# This function references the following fields: Sales, Region, and Segment
def calculate_percent_sales_in_region_over_threshold(sales_list, region, segment, threshold):
    # takes a list of sales where each element is a dictionary
    # calculates total sales where region is the specified region, segment is consumer, and sales value is over the threshold
    # returns percentage of count of sales over threshold within specified region

    # Handle corner case
    if len(sales_list) == 0:
        return 0
    
    qualified_count = 0
    over_threshold_count = 0

    for item in sales_list:
        if item["Region"] == region and item["Segment"] == segment:
            qualified_count += 1
            if item["Sales"] >= threshold:
                over_threshold_count += 1
    if qualified_count == 0:
        return 0

    sales_percent = (over_threshold_count / qualified_count) * 100
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
    percent_furniture = calculate_percent_category(sales_list, "Furniture", "Standard Class")
    print(f"Percent of furniture categories: {percent_furniture:.2f}%")
    sales_percent = calculate_percent_sales_in_region_over_threshold(sales_list, "West", "Consumer", 100)
    print(f"Percent of count of sales in the West over 100: {sales_percent:.2f}%")
    generate_report(percent_furniture, sales_percent)

# Unit tests

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.mock_sales_list = []
        self.mock_sales_list.append({
            "Category": "Furniture",
            "Region": "West",
            "Sales": 200,
            "Segment": "Consumer",
            "Ship Mode": "Standard Class"
        })
        self.mock_sales_list.append({
            "Category": "Technology",
            "Region": "East",
            "Sales": 200,
            "Segment": "Corporate",
            "Ship Mode": "Standard Class"
        })
        self.mock_sales_list.append({
            "Category": "Furniture",
            "Region": "East",
            "Sales": 50,
            "Segment": "Corporate",
            "Ship Mode": "Second Class"
        })
        self.mock_sales_list.append({
            "Category": "Technology",
            "Region": "West",
            "Sales": 75,
            "Segment": "Consumer",
            "Ship Mode": "Second Class"
        })

    # Test cases for percent furniture function

    def test_percent_calculation(self):
        percent_furniture = calculate_percent_category(self.mock_sales_list, "Furniture", "Standard Class")
        self.assertAlmostEqual(percent_furniture, 25.0)

    def test_percent_calculation_category(self):
        percent_technology = calculate_percent_category(self.mock_sales_list, "Technology", "Standard Class")
        self.assertAlmostEqual(percent_technology, 25.0)

    # Test edge case - pass an empty list 
    def test_percent_calculation_edge_case(self):
        sales_percent = calculate_percent_category([], "Furniture", "Second Class")
        self.assertAlmostEqual(sales_percent, 0)

    # Test edge case - pass a nonexisting category 
    def test_percent_calculation_edge_case_bad_category(self):
        sales_percent = calculate_percent_category(self.mock_sales_list, "ABCD", "Standard Class")
        self.assertAlmostEqual(sales_percent, 0)

    # Test cases for percent sales function 

    def test_percent_calculation_threshold(self):
        sales_percent = calculate_percent_sales_in_region_over_threshold(self.mock_sales_list, "West", "Consumer", 100)
        self.assertAlmostEqual(sales_percent, 50.0)

    def test_percent_calculation_threshold_another_region(self):
        sales_percent = calculate_percent_sales_in_region_over_threshold(self.mock_sales_list, "East", "Consumer", 100)
        self.assertAlmostEqual(sales_percent, 0)

    # Test edge case - unusually large threshold
    def test_percent_calculation_sales_edge_case(self):
        sales_percent = calculate_percent_sales_in_region_over_threshold(self.mock_sales_list, "West", "Corporate", 1000000)
        self.assertAlmostEqual(sales_percent, 0)

    # Test edge case - bad region
    def test_percent_calculation_sales_edge_case_bad_region(self):
        sales_percent = calculate_percent_sales_in_region_over_threshold(self.mock_sales_list, "ABCD", "Corporate", 100)
        self.assertAlmostEqual(sales_percent, 0)

if __name__ == '__main__':
    unittest.main(exit=False)
    main()