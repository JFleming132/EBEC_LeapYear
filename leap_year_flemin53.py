"""
Author: Your Name, flemin53@purdue.edu
Assignment: m.n - Leap Year
Date: 09/14/2021

Description:
    This program will determine if an input year is a leap year or not based on its divisibility by 4 and 100.

Contributors:


My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""


def main():

    year = int(input('Please input a year: '))
    if year%100 == 0:
        if year%4 ==0:
            LeapYear = True
        else:
            LeapYear = False
    elif year%4 == 0:
        if year%100 == 0:
            LeapYear == True
        else:
            LeapYear == False
    else:
        False
    year = str(year)
    if LeapYear:
        print('In the year '+year+', February has 29 days.')
    else:
        print('In the year '+year+', February has 28 days.')



if __name__ == '__main__':
    main()
