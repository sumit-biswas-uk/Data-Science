import math
from module import get_two_str_choices, get_length_of_time, get_amount, get_percentage

# Following is a program to access two different financial calculators: investment and home loan.
# The Investment calculator allows the user to calculate the total amount after interest is applied to 
# The investment for a number of years.
# The Bond calculator allows the user the calculate the amount of repayment on home loan each month.

# Pseudo code:
# While the user keeps choosing to continue, we would give access to both calculators.
    # Welcome the user to financial calculator.
    # Inform the user of choices of calculation they can do. Investment and Bond
    #   
        # Ask user to input one of two choices.

        # If user choice == Investment
            # Welcome the user to the Investment calculator.
            # Ask the user for the amount they want to invest.
            # Ask the user for the interest rate on the investment.
            # Divide interest rate by 100.
            # Ask the user for the number of years they want to invest for.
            # Ask the user to choose between simple and compound interest.

            # If user choice == simple 
                # Calculate simple interest based on user inputs
                # Print the result of the calculation with a summary message.

            # Else:
                # Calculate compound interest based on user input.
                # Print the result of the calculation with a summary message.

        # else:
            # Welcome the user to Home Loan Repayment calculator.
            # Ask the user for the value of the property.
            # Ask the user for the annual interest rate.
            # Divide the annual interest by 100 and then divide it by 12 to get monthly interest percentage.
            # Ask the user for the number of months over which the bond will be repaid.
            # Calculate monthly repayment based on user input.
            # Print the result of the calculation with a summary message.

        # Ask the user if they want to perform another calculation.
        # If user choice == yes
            # Continue

        # Else: 
            # Thank the user for using the calculator with a goodbye message.
            # Break


while True:

    # Welcome message and explanation of choices.

    print("Welcome to Capstone Financial Calculator.")
    print("Investment - to calculate the amount of interest you'll earn on your investment.")
    print("Bond - to calculate the amount you'll have to pay on a home loan.")

    # Initialising variables for choices and input messages which will be used as arguments
    # In functions later.
    
    calc_1 = "investment"
    calc_2 = "bond"
    amount_message = "Please enter the amount of money you want to deposit (only digits): "
    interest_rate_message = "Please enter the interest rate percentage (only digits): "
    year_message = "Please enter the number of years you are investing for (only digits): "
    interest_method_1 = "simple"
    interest_method_2 = "compound"
    month_message = "Please enter the number of months over which the bond will be repaid (only digits): "
    value_message = "Please enter the present value of the property (only digits): "


    # Getting calculator choice through error handling.

    print("")
    calc_choice = get_two_str_choices(calc_1, calc_2)

    # If calc choice is investment. We will print a welcome message and
    # Ask for amount, interest rate, years, and type of interest calc, all through error handling.
    # Depending on type of interest calc they choose, we will feed user input to the appropriate calc
    # And print out the output with a summary message.

    if calc_choice == "investment":

        print("")
        print("Welcome to the Investment calculator")


        amount = float(get_amount(0, amount_message))
        user_interest_rate = float(get_percentage(0, interest_rate_message))
        interest_rate = user_interest_rate / 100
        years = float(get_length_of_time(0, year_message))
        interest = get_two_str_choices(interest_method_1, interest_method_2)


        if interest == "simple":
            total_amount = amount * (1 + interest_rate*years)

            print("")
            print(f"You are calculating {interest} interest at {user_interest_rate:.2f}% for £{amount:.2f} over {years:.2f} years.")
            print(f"Your total amount at the end of this period will be £{total_amount:.2f}.")
            print(f"Your interest earned during this period will be £{(total_amount-amount):.2f}.")
      
        
        else:
            total_amount = amount * math.pow((1 + interest_rate), years)

            print("")
            print(f"You are calculating {interest} interest at {user_interest_rate:.2f}% for £{amount:.2f} over {years:.2f} years.")
            print(f"Your total amount at the end of this period will be £{total_amount:.2f}.")
            print(f"Your interest earned during this period will be £{(total_amount-amount):.2f}.")

    
    # if the calc choice is bond. We will print a welcome message and ask for the value
    # Of the property, interest rate and months, all through error handling. 
    # Then we will take user inputs and calculate the monthly repayment.
    # Lastly we will show the result of calculation with a summary message.

    else:
        print("")
        print("Welcome to Home Loan Repayment calculator")


        value = float(get_amount(0, value_message))
        property_interest_rate = float(get_percentage(0, interest_rate_message))
        interest_rate = (property_interest_rate / 100) / 12
        months = float(get_length_of_time(0, month_message))

        
        repayment = (interest_rate * value) / (1 - (1 + interest_rate) ** (-months))

        print("")
        print(f"You are calculating monthly repayment of property valued at £{value:.2f} on a yearly interest rate of {property_interest_rate:.2f}% over {months:.2f} months.")
        print(f"Your monthly repayment for this period will be £{repayment:.2f}.")
        
    
    
    # We will ask the customer if they want to perform another calculation (through error handling)
    # And continue the loops if the answer is "yes".
    # If the answer is "no", will print a Thank You message and break.

    print("")    
    print("Do you want to perform another calculation? (\"y\" for \"yes\" or \"n\" for \"no\")" )

    another_calc = get_two_str_choices("y", "n")


    if another_calc == "y":
        print("")
        continue

    else:
        print("")
        print("Thank you for using our calculator. Hope to see you again!")
        break

            




