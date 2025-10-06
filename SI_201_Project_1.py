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

        # read and print first row
        first_row = next(reader)
        print("First row:", first_row)

        # print the number of rows
        rows = list(reader)
        print("Number of rows:", len(rows))

main()
