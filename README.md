# T1A3_Terminal_App

working ideas

- create input for user
- export report/summary
- error handling 
- create weekly report
- If user goes over industry standards for cost to turnover ratio warn user


# Documentation

## Git Hub Link
https://github.com/insearchwhy/T1A3_Terminal_App

## Code Style 
Pep 8 was used with features like comments proper class and function naming along with error handling

## 3 Features

Feature 1: Financial Summary Generation and Export Description: The app takes weekly financial costs from users, figures out total costs and gross profit. It then makes a neat financial summary and saves it as a text file. 

User Input: The app asks users to type in weekly money info like turnover, cost of goods sold, staffing costs, rent, and utilities. It uses the get_float_input function for this. Data Validation: The app checks user inputs to make sure they're positive numbers. Benchmark Check: The app uses IndustryBenchmark.check_against_benchmarks to see if any costs are too high compared to industry norms. Financial Calculation: The app adds up all costs and figures out gross profit from what users typed in. File Export: The app uses the PDFGenerator class to create a structured financial summary. It saves this as a text file with the current date and time in the name. 


The main function stores user inputs and mid-way figures in different variables like turnover and cost_of_goods. This showcases variables and their scope. The get_float_input function has a while loop for dealing with errors. If-else statements decide whether to show warnings based on industry standards. This shows loops and decision-making structures. The get_float_input function catches ValueError exceptions for wrong input types with a try-except block. This demonstrates error handling.


Feature 2: Industry Benchmark Warning System Description: This system checks financial data against industry standards. It flags costs that go beyond set limits. Users get alerts when their numbers surpass these benchmarks. 

Benchmark Definitions: The IndustryBenchmark class sets cost standards for industries. It caps goods and staffing at 30%, rent and utilities at 10%. Comparison: The system uses if statements to match user costs with these benchmarks. Warning Generation: It builds alert messages for each overrun benchmark. These alerts go into a warnings list. 

The console shows these alerts. It points out areas where costs top recommended levels. Implementation Details: Variables and Variable Scope: The check_against_benchmarks method uses a local variable called warnings to store alerts. Conditional Control Structures: The code uses if statements to check if costs go over benchmarks. It then adds relevant alerts to the warnings list. Error Handling: This feature doesn't deal with errors . It compares values and creates alerts based on set rules.

Feature 3: User Feedback and Summary Display Description: This feature gives friendly feedback and shows a full money breakdown. It covers sales, expenses, and profits. It also tells users if their costs match what's normal for their industry. 


Feedback Message: A welcome note pops up. It asks users to put in their weekly money info. Benchmark Check: The system looks at the numbers. It warns users if anything's too high compared to industry norms. Financial Calculation: The system crunches the numbers. It figures out total costs and profit from what users typed in. Summary Display: A neat money summary appears on screen. It shows sales, costs, and profit. Completion Message: Users get a heads-up. It says if their costs are okay or if they're spending too much. 


The main function employs local variables like turnover and cost_of_goods. These store and crunch user inputs and calculations. A while loop in get_float_input checks input. If-else statements print warnings or success messages based on benchmarks. Get_float_input boasts a try-except block. It catches input errors - those pesky non-numeric values that can trip up the system.

# Restaurant/Cafe Cost-Profit Analyzer Documentation &  Install guide

Introduction
Welcome to the Restaurant/Cafe Cost-Profit Analyzer! This application helps you analyze your weekly financial performance based on input costs and provides insights into industry benchmarks.

Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-repository.git
cd your-repository
Install Python 3:
Ensure Python 3 is installed on your system. You can download it from python.org and follow the installation instructions for your operating system.

Install Required Packages:
This application requires no external packages beyond the standard library.

Dependencies
Python 3.x
System/Hardware Requirements
Operating System: Windows, macOS, Linux
Disk Space: Minimal
Usage
Run the Application:
Open a terminal or command prompt and navigate to the directory containing cost_profit_analyzer.py.

Copy code
python3 cost_profit_analyzer.py
Input Weekly Costs:
Follow the prompts to enter the following weekly costs:

Weekly turnover
Cost of goods sold
Cost of staffing
Cost of rent
Cost of utilities
View Analysis:

The application will analyze your costs against industry benchmarks.
It will display any warnings if your costs exceed industry standards.
It will show a financial summary including turnover, total costs, and gross profit.
Export Results:

A financial summary will be exported to a text file (financial_summary_<timestamp>.txt) in the current directory.