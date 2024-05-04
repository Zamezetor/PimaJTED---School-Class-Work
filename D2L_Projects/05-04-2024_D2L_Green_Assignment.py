# Logan White 05/04/2024
# 05-04-2024_D2L_Green_Assignment.py
# D2L Going Green Assignment
# CC BY-NC-SA 4.0
# Imports 
# Variables 
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
green_dicts = [{'January' : {}}, {'February' : {}}, {'March' : {}}, {'April' : {}}, {'May' : {}}, {'June' : {}}, {'July' : {}}, {'August' : {}}, {'September' : {}}, {'October' : {}}, {'November' : {}}, {'December' : {}}]
# Functions
def main():
    end_program = False
    while not end_program:
        for i in range(len(green_dicts)):
            green_dicts[i][months[i]].update({('Not Green', int(input(f' What are the Not Green Costs for {months[i]} \n ►\t')))})
            green_dicts[i][months[i]].update({('Green', int(input(f' What are the Green Costs for {months[i]} \n ►\t')))})
        for i in range(len(green_dicts)):
            green_dicts[i][months[i]].update({('Saved',(green_dicts[i][months[i]]['Not Green'] - green_dicts[i][months[i]]['Green']))})
        print(green_dicts)
        print(f'--------------------------------┤ Savings ├--------------------------------')
        print(f'   Savings ($)       Not Green ($)        Green ($)         Month ($)   ')
        for i in range(len(green_dicts)):
            print('       ' , (green_dicts[i][months[i]])['Saved']  , '             ' , (green_dicts[i][months[i]])['Not Green'] , '              ' , (green_dicts[i][months[i]])['Green'] , '           ' , months[i] , '        ')
        end_program = 'y' in input('Do you want to end program? (yes/no): \n→ ').lower()


# Code
main()
