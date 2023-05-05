option_text = "\nif you want to calculate enter 'y' with this calculater\nif you want to choose another calculater type 'a'\ntype 'q' to quit the program:\n" 

def choices():
    while True: 
        calculator_choice = input("\nchoices:\n('v' - vat),\n('pl' - profit and loss),\n('si' - simple interest),\n('cp' - compound interest),\n('bap' - base, amount, percent).\nif you want to quit the program type 'q'\n") 
        if calculator_choice == 'v':
            vat_cal()
        elif calculator_choice == 'pl':
            profit_and_loss_calculator() 
        elif calculator_choice == 'si':
            s_interest_calculator()
        elif calculator_choice == 'cp':
            cp_interest_calculator()
        elif calculator_choice == 'bap':
            bap_calculator()
        elif calculator_choice == 'q':
            break
        else:
            print('you have typed an invalid word!')

######################

def vat_cal():
    while True:
        option = input(option_text)
        if option == "y":
            cost = input('\nenter the cost number only no letters: ')
            if cost.isdigit():
                cost = int(cost)
                vat_rate = 15 / 100
                vat = cost * vat_rate
                rounded_value = round(vat)
                print(f'\nthe vat of {cost} is: {rounded_value}')
            else:
                print('\nenter number only\n')
        elif option == 'a':
            choices()
        elif option == 'q':
            break
        else:
            print('\nyou have typed an invalid word\n')

###########################

def profit_and_loss_calculator():
    while True:
        option = input(option_text)
        if option == "y":
            cost_price = input('\nenter the cost price number only no letters: ')
            selling_price = input('enter the selling price number only no letters: ')
            if cost_price.isdigit() and selling_price.isdigit():
                cost_price = int(cost_price)
                selling_price = int(selling_price)
                if cost_price > selling_price:
                    print('\nyour get a loss')
                    loss = cost_price - selling_price
                    print(f'your loss amount is: {loss}')
                    loss_percent = loss * 100 / cost_price
                    print(f'your loss percent is: {loss_percent}% \n')
                elif cost_price < selling_price:
                    print('\nyour get a profit')
                    profit = selling_price - cost_price
                    print(f'your profit amount is: {profit}')
                    profit_percent = profit * 100 / cost_price
                    rounded = round(profit_percent)
                    print(f'your profit percent is: {rounded}% ')
            else:
                print('\nenter number only\n')
        elif option == 'a':
            choices()
        elif option == 'q':
            break
        else:
            print('\nyou have typed an invalid word\n')

#####################3

def s_interest_calculator():
    while True:
        option = input(option_text)
        if option == "y":
            principal = input('enter principal number only no letters: ')
            time = input('enter the number of years number only no letters: ')
            rate = input('enter rate with out the percent symbol number only no letters: ')
            if principal and time and rate.isdigit():
                principal = int(principal)
                time = int(time)
                rate = int(rate)
                rate = rate / 100 
                interst = principal * rate * time
                rounded = round(interst)
                print(f'\n{rounded} is the amount of interest')
                amount = interst + principal
                rounded_amount = round(amount)
                print(f'{rounded_amount} is the amount of money after {time} years')
            else:
                print('\nenter number only\n')
        elif option == 'a':
            choices()
        elif option == 'q':
            break      
        else:
            print('\nyou have typed an invalid word\n')

###########################3333

def cp_interest_calculator():
    while True:
        option = input(option_text)
        if option == "y":
            principal = input('enter principal number only no letters: ')
            time = input('enter the number of years number only no letters: ')
            rate = input('enter rate with out the percent symbol number only no letters: ')
            if principal and time and rate.isdigit():
                principal = int(principal)
                time = int(time)
                rate = int(rate)
                rate /= 100
                rate += 1
                rate = rate ** time
                cp_interest = principal * rate
                rounded = round(cp_interest)
                print(f'\nyour compound interest is {rounded}')
                interest = rounded - principal
                print(f'the simple interest is {interest}')
            else:
                print('\nenter number only\n')
        elif option == 'a':
            choices()
        elif option == 'q':
            break      
        else:
            print('\nyou have typed an invalid word\n')

#############################

def bap_calculator():
    while True:
        option = input(option_text)
        if option == "y": 
            def amount():
                base = input('\nenter the base number only no letters: ')
                percent = input('enter the percent without the percent symbol number only no letters: ')
                if base and percent.isdigit():
                    base = int(base)
                    percent = int(percent)
                    base *= percent
                    amount = base / 100
                    rounded = round(amount)
                    print(f'\nthe amount is {amount}\n')
                else:
                    print('\nenter number only\n')

            def percent():
                base = input('\nenter the base number only no letters: ')
                amount = input('enter the amount number only no letters: ')
                if base and amount.isdigit():
                    base = int(base)
                    amount = int(amount)
                    percent = 100 * amount / base
                    print(f'\nthe percent is {percent}% \n')
                else:
                    print('\nenter number only\n')
            
            def base():
                amount = input('\nenter the amount number only no letters: ')
                percent = input('enter the percent without the percent symbol number only no letters: ')
                if amount and percent.isdigit():
                    amount = int(amount)
                    percent = int(percent)
                    base = amount * 100 / percent
                    rounded = round(base)
                    print(f'\nthe base is {rounded}\n')
                else:
                    print('\nenter number only\n')

            choice = input('\nif you want to get the amount type "a".\nif you want to get the percent type "p".\nif you want to get the base type "b":')
            if choice == "a":
                amount()
            elif choice == "p":
                percent()
            elif choice == "b":
                base()
            else:
                print('you have typed an invalid word')
        elif option == 'a':
            choices()
        elif option == 'q':
            break      
        else: 
            print('\nyou have typed an invalid word\n')


####################

print("\nHELLO I AM ABEL'S CALCULATOR\n")
print("what would you like you calculate\n")
print("if you want to calculate VAT type 'v'.\n")
print("if you want to calculate profit and loss type 'pl'.\n")
print("if you want to calculate simple interest type 'si'.\n")
print("if you want to calculate compound interst type 'cp'.\n")
print("if you want to calculate base, amount, or percent type 'bap'.")
choices()