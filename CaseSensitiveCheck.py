import json

data = json.load(open("dictionary.json"))

def retrive_definition(word):

    word = word.lower()

    if word in data:
        return data[word]
    else:
        return ("THe word Doesn't exist.")

word_user = input("Enter the word: ")

print(retrive_definition(word_user))
