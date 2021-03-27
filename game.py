import csv
import pandas as pd
from random import shuffle
import login

def welcome():
    print("*" * 30)
    print("Quiz Game".center(30, "*"))
    print("*" * 30)
    print(" 1. Login and Play".center(30, "*"))
    print(" 2. Register ".center(30, "*"))
    print(" 3. Leaderboard ".center(30, "*"))
    print(" 4. Exit".center(30, "*"))
    print("*" * 30)
    n = int(input("Enter a number >>"))
    if n == 1:
        players = login.login()
    if n == 2:
        login.register()
        welcome()
    if n == 3:
        return leaderboard()
    if n == 4:
        return exit()
    if players:
        game(players[0], players[1])
    else:
        welcome()

def build_deck():
    deck = []
    colours = ["red", "yellow", "black"]
    for colour in colours:
        for number in range(1,11):
            deck.append(Card(colour, number))
    shuffle(deck)
    return deck


class Card:
    def __init__(self, colour, number):
        self.colour = colour
        self.number = number
        self.name = f"{number} of {colour}"

    
def game(username1, username2):
    print("You have started the game")
    
    p1hand, p2hand = [], []
    deck = build_deck()
    while len(deck) > 1:
        print(len(p1hand), len(p2hand))
        p1card, p2card = deck.pop(), deck.pop()
        print(p1card.name, p2card.name)
        outcomes = ["tie", f"{username1} wins", f"{username2} wins"]
        if p1card.colour == p2card.colour:
            # (p1card.number > p2card.number) is a Boolean, returns 1 or 0
            winning_player = 2 - (p1card.number > p2card.number)
        else: 
            colours = ["red", "yellow", "black"]
            # implementation of the "rock paper scissors" type logic for the winning colour
            winning_player = (colours.index(p1card.colour) - colours.index(p2card.colour))%3
        print(outcomes[winning_player])
        if winning_player == 1:
            p1hand.extend([p1card, p2card])
        else:
            p2hand.extend([p1card, p2card])
        input()
    if len(p1hand) > len(p2hand):
        print(f"{username1} has won! {username1} has the following cards:")
        for card in p1hand:
            print(card.name)
        save_scores(username1, len(p1hand))
    else:
        print(f"{username2} has won! {username2} has the following cards:")
        for card in p1hand:
            print(card.name)
        save_scores(username2, len(p2hand))

def save_scores(username, score):
    with open('scores.csv', 'a', newline="") as scoresfile:
        playersappend = csv.writer(scoresfile)
        playersappend.writerow([username, score])
        scoresfile.flush()

def leaderboard():
    with open('scores.csv', 'r', newline="") as scoresfile:
        players = pd.read_csv(scoresfile, names=["Username", "Score"])
        sortedplayers = players.nlargest(5, 'Score')
        scores = sortedplayers.values.tolist()
        print("LEADERBOARD")
        for row in scores:
            print(f"Username: {row[0]:<10} Score: {row[1]}")

welcome()