#monthly amount calculator 

def m_amount():
    print(' MONTHLY AMOUNT CALCULATOR ')
    print('')

    principal = float(input('Enter the loan amount : '))
    rate_of_interest = float(input('Enter the rate of interest : '))
    years = int(input('Enter the number of years : '))

#monthly 

    number_of_months = years*12
    monthly_rate_of_interest = rate_of_interest/1200
    monthly_amount = principal* monthly_rate_of_interest/ (1- (1 + monthly_rate_of_interest)**(-number_of_months))

    print('The monthly payment for the loan is : ' + str(monthly_amount))
m_amount()









    
