import csv

def login():
    print("Player 1 login:")
    username1 = str(input("Enter your username >> "))
    password1 = str(input("Enter your password >> "))
    if check_credentials(username1, password1):
        print("Player 2 login:")
        username2 = str(input("Enter your username >>"))
        password2 = str(input("Enter your password >>"))
        if check_credentials(username2, password2):
            return [username1, username2]
    print("Invalid credentials. Please try again")
    return False

def check_credentials(username, password):
    with open('players.csv', 'r', newline="") as playersfile:
        players = csv.reader(playersfile)
        for row in players:
            if row [0:2] == [username, password]:
                return True
        return False

def register():
    username = str(input("Enter your username >> "))
    password = str(input("Enter your password >> "))

    if len(username) < 4:
        print("Usernames must be at least 4 characters long")
        return False
    elif len(password) < 4:
        print("Passwords must be at least 4 characters long")
        return False
    else:
        if check_credentials(username, password):
            print("Username already exists. Please try again")
            return False
        with open('players.csv', 'a', newline ="") as playersfile:
            playersappend = csv.writer(playersfile)
            playersappend.writerow([username, password])
            playersfile.flush()
            print("You have successfully registered!")
            return True             

