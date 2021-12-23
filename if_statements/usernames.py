current_users = ['Reimu', 'Marisa', 'Sanae', 'Sakuya', 'Youmu']
new_users = ['REISEN', 'AYA', 'YOUMU', 'CIRNO', 'REMILIA']

for item in range(len(current_users)):
    current_users[item] = current_users[item].lower()

for item in range(len(new_users)):
    new_users[item] = new_users[item].lower()

for user in new_users:
    if user in current_users:
        print(f"I'm sorry, \"{user}\" is already taken. Please pick another username.")
    else:
        print(f"Greetings, {user}.")