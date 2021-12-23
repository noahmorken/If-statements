# alien_color = 'green'
#
# if alien_color == 'green':
#     print("You have earned 5 points.")
#
# alien_color = 'yellow'
#
# if alien_color == 'green':
#     print("You have earned 5 points.")
#
#
# alien_color = 'green'
#
# if alien_color == 'green':
#     print("You have earned 5 points.")
# elif alien_color == 'yellow':
#     print("You have earned 10 points.")
# 
# alien_color = 'yellow'
#
# if alien_color == 'green':
#     print("You have earned 5 points.")
# elif alien_color == 'yellow':
#     print("You have earned 10 points.")

alien_color = 'red'
points = 1

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15

if points % 5 == 0:
    print(f"You have earned {points} points.")