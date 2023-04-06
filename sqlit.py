"""
Author:         Nick N

Description:    Prompt for multi line data (assumes data pasted in is 
                from excel ie. tab-delimited), and output sql query
                with CREATE and INSERT statments

"""
import re


def sqlit(text):

    # set some variables for later
    sql = ""
    firstrow = True

    if isinstance(text, str):
        lines = text.splitlines()
    else:
        lines = text

    # loop through rows of pasted data
    for line in lines:
        # split  by tabs
        row = re.split("\t", line)
        
        # build out first part of sql statement
        if firstrow:
            sql += f"CREATE TABLE #tt (\n"
        else:
            sql += f"INSERT INTO #tt VALUES("
        
        # continue sql statment looping through each item in the row
        for val in row:
            if firstrow:
                sql += f"\t[{val}] NVARCHAR(255) NULL,\n"
            else:
                sql += f"'{val}',"
        
        # finish off sql statment
        if firstrow:
            # remove last character (extra comma) and finish off sql stmt
            sql = sql[:-2] + f")\nGO\n\n"
            # no longer dealing with firstrow
            firstrow = False
        else:
            # remove last character (extra comma) and finish off sql stmt
            sql = sql[:-1] + f")\n"

    return sql


def multiline_input(prompt = "Enter input:"):
    '''Get multiline input from user'''
    
    print(prompt)
    lines = []

    while True:
        user_input = input()
        # if user pressed Enter without a value, break out of loop
        if user_input == '':
            break
        else:
            lines.append(user_input)
    
    return lines


if __name__ == "__main__":
    
    # prompt for input
    lines = multiline_input("Paste in excel data and then press enter:")
 
    # Output sql string
    print(f"\n\n\n\n{sqlit(lines)}")
