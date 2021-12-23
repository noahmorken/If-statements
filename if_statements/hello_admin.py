usernames = ['admin', 'moderator', 'helper', 'builder', 'player']

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        elif user != 'player':
            print(f"Hello {user}, thank you for your work.")
        else:
            print("Welcome, player.") 
else:
    print("We need to find some users!")