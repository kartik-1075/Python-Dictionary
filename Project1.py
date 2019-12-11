import json
from difflib import get_close_matches

data=json.load(open("data.json"))
def translate(word):
    word=word.lower()
    word_list=get_close_matches(word,data.keys())
    if word in data:
        return data[word]

    elif len(word_list)>0:
        YN=input("Did you mean %s instead? If yes Press Y, else Press N for No..." %word_list[0])
        if YN=='Y' or YN=='y':
             return data[word_list[0]]
        elif YN=='N' or YN=='n':
            return "please double check your word"
        else:
            return"Invalid Input"
    else:
        return"Word doesn't exist"
word=input("Enter word to search")
output=(translate(word))
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)                                                         
