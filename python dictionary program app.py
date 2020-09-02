import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))
#print(data)
#print(type(data))
#print(data["hacker"])


def find_word(word):
    word = word.lower()
    if word in data.keys():
        print("--"*200)
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        print("did you mean |'%s'| " % get_close_matches(word,data.keys())[0])
        print("-"*100)
        decide = input("Enter y if this is your word : ").lower()
        if decide == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == "n":
            return "Wrong Word ! "
        else:
            print("You have enter wrong word. please enter y or n ..")

    else:
        print("_"*52)
        print("|")
        print("| You enter wrong word. please try again !!!!!!!!! (^.^)")
        print("|",("_"*50))



h = find_word("hac")
if type(h) == list:
    for i,v in enumerate(h):
        print()
        print("--" * 200)
        print("|")
        print("|", i,"| ", v)
        print("|")
else:
    print(h)