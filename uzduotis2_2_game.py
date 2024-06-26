import pickle
from random import choice

while True:
    with open("quotes.pkl", 'rb') as file:
        quote = choice(pickle.load(file))

    print(quote['quote'])
    answer1 = input("Quess the author: ")
    if answer1 == quote["author"]:
        print(f"Correct! Answer is {quote['author']}")
    else:
        print(" ".join(word[0] + "." for word in quote['author'].split()))
        answer2 = input("Quess the author: ")
        if answer2 == quote["author"]:
            print(f"Correct! Answer is {quote['author']}")
        else:
            print(quote['author_born'])
            answer3 = input("Quess the author: ")
            if answer3 == quote["author"]:
                print(f"Correct! Answer is {quote['author']}")
            else:
                print(f"Wrong! Answer is {quote['author']}")

    if_continue = input("Continue? y/n: ")
    if if_continue == "n":
        break
