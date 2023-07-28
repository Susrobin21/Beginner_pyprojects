#currency convertor 

def main():

    print('This calculator converts Indian rupees into US dollars ')
        
    rupees = eval(input('Enter amount in rupees : '))

    dollars = convert_to_dollars(rupees)

    print('The amount is ',dollars,'$')

convert_to_dollars = lambda rupees : rupees * 0.012

main()




