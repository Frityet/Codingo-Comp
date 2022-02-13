# Write your code here!

import requests
import json

word = requests.get("https://random-word-api.herokuapp.com/word?number=1").json()[0]

#print(word)
lives = 8

letters = ""

def worddisp(word, letters):
    wstr = ""
    for x in word:
        if x == " ":
            wstr = wstr + " "
        elif x in letters:
            wstr = wstr + x
        else:
            wstr = wstr + "_"
    return wstr

def printstatus():
    print("You have", lives, "attempts left.")
    incletters = ""
    for x in letters:
        if x not in word:
            incletters += x
    print("You have guessed these incorrect letters:", incletters)
    print(worddisp(word, letters))


print("Welcome to Hangman! Let us begin.")
while True:
    if lives <= 0:
        break
    printstatus()
    ch = input("Make your guess.")
    if len(ch) != 0 and ch[0] != " ":
        l = ""
        l = ch[0].lower()
        if l in letters:
            print("You've already guessed this one!")
            continue
        letters += l[0]
        if l[0] not in word:
            print("Oh hot diggity darned it! You're WRONG! Try again.")
            lives -= 1
            continue
        else:
            print("Nice pick!")
            continue
    else:
        print("Oop. Seems you've written something wrong. Make sure: Only letters!")
        continue
print("Aw gosh darndit, aren't you an unluckly little critter. Until next time, and good luck in all your future endeavours!")