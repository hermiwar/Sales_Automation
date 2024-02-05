#!/usr/bin/env python
# coding: utf-8

# Ayodeji Temitope Amigun

# In[ ]:


# Function to calculate total sales for the day
def calculate_total_sales(shift_sales):
    return sum(shift_sales)

# Function to calculate worker's salary based on hourly rate and hours worked
def calculate_worker_salary(hourly_rate, hours_worked):
    return hourly_rate * hours_worked

# Function to calculate profit (or loss if negative) based on total sales and total cost
def calculate_profit(total_sales, total_cost):
    return total_sales - total_cost

# Function to calculate tips for a shift (2% of shift sales)
def calculate_tips(shift_sales):
    return sum(shift_sales) * 0.02

# Function to calculate total tips for the day (sum of tips from both shifts)
def calculate_total_tips(morning_sales, evening_sales):
    return calculate_tips(morning_sales) + calculate_tips(evening_sales)

# Main program loop
def main():
    print("Welcome to the Retail Business Accounting System!")

    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Calculate Total Sales for the Day")
        print("2. Calculate Worker's Salary")
        print("3. Calculate Profit")
        print("4. Calculate Tips for a Shift")
        print("5. Calculate Total Tips for the Day")
        print("6. Exit")

        # Get user choice
        choice = input("Enter your choice (1-6): ")

        # Perform the selected operation based on user input
        if choice == '1':
            morning_sales = float(input("Enter morning shift sales: "))
            evening_sales = float(input("Enter evening shift sales: "))
            total_sales = calculate_total_sales([morning_sales, evening_sales])
            print(f"Total Sales for the Day: {total_sales}")

        elif choice == '2':
            hourly_rate = float(input("Enter hourly rate: "))
            hours_worked = float(input("Enter hours worked: "))
            worker_salary = calculate_worker_salary(hourly_rate, hours_worked)
            print(f"Worker's Salary: {worker_salary}")

        elif choice == '3':
            total_sales = float(input("Enter total sales: "))
            total_cost = float(input("Enter total cost: "))
            profit = calculate_profit(total_sales, total_cost)
            print(f"Profit: {profit}")

        elif choice == '4':
            shift_sales = float(input("Enter shift sales: "))
            tips = calculate_tips([shift_sales])
            print(f"Tips for the Shift: {tips}")

        elif choice == '5':
            morning_sales = float(input("Enter morning shift sales: "))
            evening_sales = float(input("Enter evening shift sales: "))
            total_tips = calculate_total_tips([morning_sales], [evening_sales])
            print(f"Total Tips for the Day: {total_tips}")

        elif choice == '6':
            print("Exiting the program. Thanks for using Automation application, Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

# Entry point for the program
if __name__ == "__main__":
    main()


# CHALLENGES I ENCOUNTERED
# 
# 1. I could not work with the value I got from the input because I forgot to typecast.
# 2. I wanted to design an interface that is intuitive and beautiful, but there was no idea on how to go about it.
# 3. I spent time on trials and errors to get the best out of the code.
# 4. I mistakenly entered ',' in wrong part of the code and it gave a serious problem because I did not notice it in time.
