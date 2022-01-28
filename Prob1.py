#====================================================
# Filename: Prob2.py
# 
# Your name: Malie Heine
# Who did you work with (if anyone)?: Nobody
# Estimate for time spent (in hrs)?: 2 hours
#====================================================

import karel

# Your program should create a checkerboard pattern on any
# rectangular world. I am defining a few functions below to
# get you started, but you can (and should) add whatever
# other helper functions you want below.

def create_checkerboard():
    """ Main function to create the checkerboard pattern. """
    # You need to add code here
    while facing_east():
        #Karel starts facing east, so this ensures the checkerboard loop starts.
        #The "facing west" loop also ensures that Karel will be facing east again in cases Karel must go east again to complete checkerboard
        while facing_east():
            checkerboard_east()
        while facing_west():
            checkerboard_west()
        if facing_north():
            #In the case of 1x8, where Karel ends facing north instead of facing east. If and While loops both end once Karel reaches the 8th street in 1x8
            while front_is_clear():
                checkerboard_north()



    # Remember to define any more helper functions you want down here

def checkerboard_east():
    """Helper function to make Karel paint checkerboard marks while facing east"""
    #Karel places a beeper and moves 1-2 times unless it reaches a wall.
    # If so, it makes Karel face north and checks if Karel is on a beeper
    put_beeper()
    if front_is_clear():
        move()
        if front_is_clear():
            move()
        else:
            turn_left()
            check_for_beeper()
    else:
        turn_left()
        check_for_beeper()

def checkerboard_west():
    """Helper function to make Karel paint checkerboard marks while facing west"""
    #Karel places a beeper and moves 1-2 times unless it reaches a wall.
    # If so, it makes Karel face north and checks if Karel is on a beeper
    put_beeper()
    if front_is_clear():
        move()
        if front_is_clear():
            move()
        else:
            turn_right()
            check_for_beeper()
    else:
        turn_right()
        check_for_beeper()

def checkerboard_north():
    """Helper function to make Karel paint checkerboard marks while facing north"""
    #Karel places a beeper, and if the front is clear it moves 1 time.
    # It then checks if Karel is on a beeper
    put_beeper()
    if front_is_clear():
        move()
        check_for_beeper()


def check_for_beeper():
    """Helper function on the outter wall to confirm whether Karel should paint that spot"""
    #Checks which reposition function Karel should do depending on if Karel is on a beeper currently
    if front_is_clear():
        if no_beepers_present():
            reposition_no_beeper()
        else:
            reposition_beeper()

def reposition_beeper():
    """Helper function to reposition Karel after checking for a beeper on the last row, skipping over that outter wall spot so it won't be painted"""
    if left_is_blocked() and right_is_blocked():
        #This is specifically for the 1x8 map, where Karel is facing north and both sides are blocked so Karel must move forward
        # Karel must move forward twice. This should only happen once, after placing the first beeper in 1x8
        move()
        move()
    else:
        #For maps that aren't 1x8
        if right_is_blocked():
            #If Karel's right is blocked, this sets Karel up to do checkerboard_west()
            # Moves Karel 1 up and turns Karel to face west
            move()
            turn_left()
            move()
        if left_is_blocked():
            #If Karel's left is blocked, this sets Karel up to do checkerboard_east()
            # Moves Karel 1 up and turns Karel to face east
            move()
            turn_right()
            move()

def reposition_no_beeper():
    """Helper function to reposition Karel after checking for a beeper on the last row, making sure that outter wall spot is painted"""
    """Karel should be facing north at the end of all checkerboard functions"""
    if left_is_blocked() and right_is_blocked():
        #This is specifically for the 1x8 map, where Karel is facing north and both sides are blocked so Karel must move forward
        move()
    else:
        #For maps that aren't 1x8
        if right_is_blocked():
            #If Karel's right is blocked, this sets Karel up to do checkerboard_west()
            # Moves Karel 1 up and turns Karel to face west
            move()
            turn_left()
        if left_is_blocked():
            #If Karel's left is blocked, this sets Karel up to do checkerboard_east()
            # Moves Karel 1 up and turns Karel to face east
            move()
            turn_right()

def turn_right():
    """Helper function to make Karel turn right"""
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    """Helper function to make Karel turn back around"""
    turn_left()
    turn_left()

