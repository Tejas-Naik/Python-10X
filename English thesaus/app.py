from difflib import get_close_matches

import json
data = json.load(open("data.json"))


def translate(choice):
    if choice in data:
        print()
        return data[choice]

    elif len(get_close_matches(choice, data.keys())) > 0:
        yn = input("Did you mean '{}' instead? Enter Y if yes, or N if no: ".format(
            get_close_matches(choice, data.keys())[0]))
        if yn == "Y" or "y":
            print()
            return data[get_close_matches(choice, data.keys())[0]]

        elif yn == "N" or "n":
            print()
            return "The word doesn't exist. Please double check it."

        else:
            print()
            return "We didn't understand your entry."

    else:
        print()
        return "The word doesn't exist. Please double check it."


another_word = True
while another_word:
    choice = input(
        "Please enter the word you wanna get the meaning of? ").casefold()

    output = translate(choice)
    if type(output) == list:
        for definition in output:
            print(definition)
    else:
        print(output)
    print()
    print()
    # again = input("Do you wanna search another word or quit type Y to continue or N to quit: ")
    # if again == "y" or "Y":
    #     another_word = True
    # else:
    #     another_word = False
