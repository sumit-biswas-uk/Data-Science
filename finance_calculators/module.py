# GROUP OF FUNCTIONS
# Following group of functions will be used later for error validation.

def is_not_integer_not_aplha(x):
    """
    This function will return true if user input 
    is a non integer and does not have any
    alphabets in it. Therefore only
    numbers with fractional parts.
    """
    try:
        value = float(x)

        if not value.is_integer():
            return True
        
        else:
            return False
        
    except:
        return False
    



def is_negative(y):
    """
    This function will try to convert user input
    into a float and if successful, will return True if
    it's a negative integer.
    """
    try:
        value = float(y)

        if value < 0:
            return True
        
        else:
            return False
        
    except:
        return False




def has_special_char(z):
    """
    This function will return True if user input has
    any special characters.
    """
    special_characters = "!@#£$%^&*()[]\\{\\}:;-+?_=,\"\'\\<>/"

    
    for i in z:
        for c in special_characters:
            if i == c:
                return True
                


def is_alphanumeric(j):
    """
    This function will return True if user input is
    alphanumeric.
    """
    
    if j.isalnum() and not j.isalpha() and not j.isdigit():
        return True
        
    else:
        return False
        




def is_only_numbers(l):
    """
    This function tries to convert the user input to a float and
    if successful, will return True if it is
    a number without a fractional part.
    """
    try:

        if float(l).is_integer():
            return True
        
        else:
            return False
                
    except:
        return False
    
    
    
     
def is_not_float(m):
    """
    Checks if the given value is not a valid floating-point number.
    Returns True if conversion to float is not possible.

    Note: This function is intended for use with correct positioning in a series of 
    error-handling conditions. It specifically identifies cases where the input contains
    alphabets with decimals, assuming such cases are not caught earlier in
    conditions for alphabets or special characters like dots.
    """
    
    try: 

        m = float(m)
        return False
        
    except:
        return True

    
    



# ERROR VALIDATION
#
# The following functions takes two string choices as arguments and present it to the user.
# It then helps the user to enter the correct choice by informing the user what is wrong with
# The entry (i.e. if the user enters an incorrect value).
#
# In the end this function returns the user input, once the user has correctly entered a given choice.


def get_two_str_choices(choice_1, choice_2):
    """
    This function asks the user to input one of two choices provided as arguments,
    removes spaces from input, coverts it to lower case and does error handling 
    to help the user enter the correct choice.
    """

    while True:

        user_input = input(f"Please enter either \"{choice_1}\" or \"{choice_2}\" to proceed: ")


        try:

            user_input = user_input.replace(" ", "")
            user_input = user_input.lower()

            # Following first if statement is redundant code and is only kept here in future cases 
            # Where user entry is space sensitive. In that case the above code 
            # User_input = user_input.replace(" ", "") will have to be deleted.
            #
            #if " " in user_input:
                #raise Exception("There cannot be any spaces in your choice. Please try again.") 
            
            if user_input == "":
                raise Exception("Opps! Looks like you have not entered anything. Please try again")
            
            if is_not_integer_not_aplha(user_input):
                raise Exception("Opps! Thats a number with a decimal. Please try again")
            
            if is_negative(user_input):
                raise Exception("Opps! That's a negative number. Please try again")
                     
            if is_only_numbers(user_input):
                raise Exception("Opps! That's a number. Please try again")
            
            if has_special_char(user_input):
                        raise Exception("Oops! Special character your entry. Please try again.")
            
            if is_alphanumeric(user_input):
                    raise Exception("Opps! The choice cannot be alphanumeric. Please try again.")
                               
            if user_input != choice_1 and user_input != choice_2:
                raise Exception("Sorry, choice does not exists. Please check your spelling and try again")

                                    
            return user_input
        
            
        except Exception as e:
            print(e)




# The following functions takes argument as time and user input message (to enter the number of 
# Years or months they want to perform a particular calculation for).
# It then helps the user to enter the correct time by informing the user what is wrong with
# The entry, (i.e. if the user enters an incorrect value).
#
# In the end this function returns the time user wants to perform the calculation for.


def get_length_of_time(time, message):
    """
    This function takes arguments as time  
    (Initialise with 0[or default time]
     while using), (set to take infinity [see last if statement]) and 
    user input message (user input: length of time text). 
    It then takes the input(time) and does error handling to 
    assist the user input a valid entry.
    """

    while True:
        
        time = input(message)

        try:

            time = time.replace(" ", "")
            time = time.lower()
            time = time.replace("years", "")
            time = time.replace("months", "")


            if time == "":
                raise Exception("Opps! Looks like you have not entered anything. Please try again")
            
            # Following if statement can be uncommented if the years cannot be in decimal
            # However we will have to deal with the float accordingly in our main program.

            # if is_not_integer_not_aplha(time):
            #     raise Exception("Opps! Thats a number with a decimal. Please try again")
                
            if is_negative(time):
                raise Exception("Opps! That's a negative number. Please try again")
            
            if has_special_char(time):
                raise Exception("Oops! Special character in your entry. Please try again.")
                
            if is_alphanumeric(time):
                    raise Exception("Opps! The choice cannot be alphanumeric. Please try again.")
            
            if time.isalpha():
                raise Exception("Looks like you are trying to enter alphabets. Please only enter digits")
            
            if is_not_float(time):
                raise Exception("Looks like you are trying to enter alphabets with dots. Please only enter digits")
            
            if float(time) == 0:
                raise Exception("Length of time cannot be  equal to 0. Please try again.")
            
            # Specify maximum years of calculation in input message, uncomment the following 
            # If statement and assign a max number to max_years variable if the calculation
            # Cannot be done beyond certain a number of years.
            #
            #
            #if int(float(time)) > max_years:
                #raise Exception(f"We cannot perform calculation over {max_years} years. Please select less than {max_years} years")


            return time
            
                
        except Exception as d:
            print(d)




# The following functions takes arguments as percent and message (to asks the user to enter a 
# Percentage for calculation). It then helps the user to enter percentage in correct data type 
# By informing the user what is wrong with the entry (if the user enters an incorrect value).
#
# In the end this function returns the percentage user wants to perform the calculation with.

def get_percentage(percent, message):
    """
    This function takes argument as percent (initialise with 0 while using)
    and message (user input: percent text). 
    It then takes the input (percent) and does error handling to 
    assist the user input a valid entry. 
    """

    while True:
        
        percent = input(message)

        try:

            percent = percent.replace(" ", "")
            percent = percent.lower()
            percent = percent.replace("%", "")
            percent = percent.replace("percent", "")
            
            
            if percent == "":
                raise Exception("Opps! Looks like you have not entered anything. Please try again")
                          
            if is_negative(percent):
                raise Exception("Opps! That's a negative number. Please try again")
            
            if has_special_char(percent):
                raise Exception("Oops! Special character in your entry. Please only enter digits.")
                
            if is_alphanumeric(percent):
                    raise Exception("Opps! The choice cannot be alphanumeric. Please try again.")
            
            if percent.isalpha():
                raise Exception("Looks like you are trying to enter alphabets. Please only enter digits")
            
            if is_not_float(percent):
                raise Exception("Looks like you are trying to enter alphabets with dots. Please only enter digits")
                                   
            if float(percent) > 100 or float(percent) == 0:
                raise Exception("Percentage cannot be  equal to 0 or more than 100. Please try again.")
            

            return percent
            
                
        except Exception as f:
            print(f)




# The following function takes argument as amount and message (to ask user to input an amount).
# It then helps the user to enter an amount in correct data type by informing the user what is wrong with
# the entry, if the user enters an incorrect value.
#
# In the end this function also returns the amount user wants to perform the calculation with.

def get_amount(amount, message):
    """
    This function takes argument as amount (initialise with 0 while using)
    and message (user input: amount text). 
    It then takes the input(amount) and does error handling to 
    assist the user input a valid entry.
    """

    while True:
        
        amount = input(message)

        try:

            amount = amount.replace(" ", "")
            amount = amount.lower()
            amount = amount.replace("£", "")
            amount = amount.replace("$", "") # This program is not designed to convert $ in £ value. As this project does not have that requirement. This line only removes the $ symbol.
            amount = amount.replace("pounds", "")
            amount = amount.replace("dollars", "") # This program is not designed to convert Dollars in Pound value. As this project does not have that requirement. This line only removes the word "Dollar".

            if amount == "":
                raise Exception("Opps! Looks like you have not entered anything. Please try again")
            
            if is_negative(amount):
                raise Exception("Opps! That's a negative number. Please try again")
            
            if has_special_char(amount):
                raise Exception("Oops! Special character in your entry. Please only enter digits.")
                
            if is_alphanumeric(amount):
                raise Exception("Opps! The choice cannot be alphanumeric. Please try again.")
            
            if amount.isalpha():
                raise Exception("Looks like you are trying to enter alphabets. Please only enter digits")
                                  
            if is_not_float(amount):
                raise Exception("Looks like you are trying to enter alphabets with dots. Please only enter digits")

            if float(amount) == 0:
                raise Exception("Amount cannot be  equal to 0. Please try again.")
            
            return amount
            
                
        except Exception as g:
            print(g)






        