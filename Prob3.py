#====================================================
# Filename: Prob3.py
# 
# Your name: Malie Heine
# Who did you work with (if anyone)?: Nobody
# Estimate for time spent (in hrs)?: 0.75 hours
#====================================================


def print_multiples():
    """
    Prints all the numbers between 1 and 100 which are multiples
    of 6 and 7 but not both. One number printed per line.
    """
    # Add your code here!
    for n in range(1,100): #n is any number between 1 and 100, and the function loops through every number
        if n%6==0 or n%7==0: #includes numbers that are divisible by 6 or 7, no remainders from dividing
            if not (n%6==0 and n%7==0): #excludes numbers that are divisible by BOTH 6 and 7, no remainders from dividing
                print(n)
















if __name__ == '__main__':
    print_multiples()
