#====================================================
# Filename: Prob2.py 
# 
# Your name: Malie Heine
# Who did you work with (if anyone)?: Nobody
# Estimate for time spent (in hrs)?: 0.5 hours
#====================================================


# Define negate here
def negate(string):
    #Function that adds the prefix "un" to an inputted string
    #Doesn't include a space to separate the prefix and the string
    return "un"+string








# Define intensify here
def intensify(string):
    #Function that adds the prefix "plus" to an inputted string
    #Doesn't include a space to separate the prefix and the string
    return "plus"+string








# Define reinforce here
def reinforce(string):
    #Function that adds the prefix "double" to an inputted string
    #Doesn't include a space to separate the prefix and the string
    return "double"+string








if __name__ == '__main__':
    # I've included the example in the description here for you to test against!
    print(negate("cold"))
    print(intensify("cold"))
    print(reinforce(intensify("cold")))
    print(reinforce(intensify(negate("good"))))
