


# For user input define errors
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

# User welcome message and input fields
def main():
    print("Welcome to the Restraunant/Cafe Cost-Profit Analyzer")
    print("Please enter the following weekly costs:")

    turnover = get_float_input("Weekly turnover: $")
    cost_of_goods = get_float_input("Cost of goods sold: $")
    cost_of_staffing = get_float_input("Cost of staffing: $")
    cost_of_rent = get_float_input("Cost of rent: $")
    cost_of_utilities = get_float_input("Cost of utilities: $")

    total_costs = cost_of_goods + cost_of_staffing + cost_of_rent + cost_of_utilities
    gross_profit = turnover - total_costs

 # user financial summary
    print("\nFinancial Summary:")
    print(f"Weekly Turnover: ${turnover:.2f}")
    print(f"Total Costs: ${total_costs:.2f}")
    print(f"Gross Profit: ${gross_profit:.2f}")

if __name__ == "__main__":
    main()
