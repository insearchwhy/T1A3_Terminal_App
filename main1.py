from datetime import datetime
import os
import logging

# Pdf generation code
class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, turnover, total_costs, gross_profit, warnings):
        with open(self.filename, 'w') as f:
            f.write(f"Financial Summary\n\n")
            f.write(f"Weekly Turnover: ${turnover:.2f}\n")
            f.write(f"Total Costs: ${total_costs:.2f}\n")
            f.write(f"Gross Profit: ${gross_profit:.2f}\n\n")
            f.write("Warnings:\n")
            for warning in warnings:
                f.write(f"- {warning}\n")

        print(f"\nFinancial summary has been exported to {self.filename}")
        
# Warnings for user if exceeds industry standards       
class IndustryBenchmark:
    @staticmethod
    def check_against_benchmarks(turnover, cost_of_goods, cost_of_staffing, cost_of_rent, cost_of_utilities):
        warnings = []
        if cost_of_goods > 0.3 * turnover:
            warnings.append("Cost of goods sold exceeds 30% of turnover. Industry standard is 30% or below!.")
        if cost_of_staffing > 0.3 * turnover:
            warnings.append("Cost of staffing exceeds 30% of turnover. Industry standard is 30% or below.")
        if cost_of_rent > 0.1 * turnover:
            warnings.append("Cost of rent exceeds 10% of turnover. Industry standard is 10% or below!")
        if cost_of_utilities > 0.1 * turnover:
            warnings.append("Cost of utilities exceeds turnover. Industry standard is 10% or below!")
        
        return warnings
       
        
# For user input define errors
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
# User welcome message 
def main():
    print("Welcome to the Restaurant/Cafe Cost-Profit Analyzer")
    print("Please enter the following weekly costs:")

    # User Input field
    turnover = get_float_input("Weekly turnover: $")
    cost_of_goods = get_float_input("Cost of goods sold: $")
    cost_of_staffing = get_float_input("Cost of staffing: $")
    cost_of_rent = get_float_input("Cost of rent: $")
    cost_of_utilities = get_float_input("Cost of utilities: $")

    # Check against industry benchmarks
    warnings = IndustryBenchmark.check_against_benchmarks(turnover, cost_of_goods, cost_of_staffing, cost_of_rent, cost_of_utilities)

    # User financial summary and warnings
    total_costs = cost_of_goods + cost_of_staffing + cost_of_rent + cost_of_utilities
    gross_profit = turnover - total_costs

    print("\nFinancial Summary:")
    print(f"Weekly Turnover: ${turnover:.2f}")
    print(f"Total Costs: ${total_costs:.2f}")
    print(f"Gross Profit: ${gross_profit:.2f}")

    # Export the financial summary to a text file
    filename = f"financial_summary_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    pdf = PDFGenerator(filename)
    pdf.generate_pdf(turnover, total_costs, gross_profit, )

if __name__ == "__main__":
    main()



