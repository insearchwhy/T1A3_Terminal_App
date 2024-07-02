from fpdf import FPDF
PDF = FPDF()
import pyinputplus as pyip
from datetime import datetime
import os



# For user input define errors
def get_float_input(prompt):
    while True:
        try:
            value = pyip.inputFloat(prompt, min=0)
            return value
        except pyip.RetryLimitException:
            print("Too many retries. Exiting.")
            exit(1)
        except pyip.TimeoutException:
            print("Timeout. Exiting.")
            exit(1)
        except ValueError:
            print("Invalid input. Please enter a number.")

# User welcome message and input fields
def main():
    print("Welcome to the Restaurant/Cafe Cost-Profit Analyzer")
    print("Please enter the following weekly costs:")

    turnover = get_float_input("Weekly turnover: $")
    cost_of_goods = get_float_input("Cost of goods sold: $")
    cost_of_staffing = get_float_input("Cost of staffing: $")
    cost_of_rent = get_float_input("Cost of rent: $")
    cost_of_utilities = get_float_input("Cost of utilities: $")

# User warnings if costs exceed industry predefined standards
    if cost_of_goods > 0.3 * turnover:
        print("Warning: Cost of goods sold exceeds 30% of turnover. Industry standard is 30% or below!.")
    if cost_of_staffing > 0.3 * turnover:
        print("Warning: Cost of staffing exceeds 30% of turnover. Industry standard is 30% or below.")
    if cost_of_rent > 0.1 * turnover:
        print("Warning: Cost of rent exceeds 10% of turnover. Industry standard is 10% or below!")
    if cost_of_utilities > turnover:
        print("Warning: Cost of utilities exceeds turnover. Industry standard is 10% or below!")

    total_costs = cost_of_goods + cost_of_staffing + cost_of_rent + cost_of_utilities
    gross_profit = turnover - total_costs

 # user financial summary
    print("\nFinancial Summary:")
    print(f"Weekly Turnover: ${turnover:.2f}")
    print(f"Total Costs: ${total_costs:.2f}")
    print(f"Gross Profit: ${gross_profit:.2f}")


