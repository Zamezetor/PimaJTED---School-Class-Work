# Balneo CSC 02/13/2024, Logan White, Nick Russell, Zachary Jenkins, Brody Villaman, Harry Barsiwal
# 02-13-2024_Operational_Lesson_Primes.py
# prints all primes from 1 to n
# CC BY-NC-SA 4.0
# Imports 
# Variables 
# Functions
def prime_check(num):
    prime_check = False
    if num > 1 :
        for i in range(2, num):
            if (num % i) == 0:
                prime_check = True
                break
    else:
        prime_check = True
    if not prime_check:
        return num
    else:
        return False


def main(length):
    prime_list = []
    for i in range(length):
        if prime_check(i) != False:
            prime_list.append(prime_check(i))
    print(f'The list of all primes from 0 to {length - 1} is:')
    print(prime_list)
    
# Code
main(int(input("What is your range of Numbers? \n ► ")) + 1)
