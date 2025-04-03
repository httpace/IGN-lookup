import requests
import re
import itertools
from bs4 import BeautifulSoup
import itertools
import string

def check_username_exists(username: str) -> bool:
    
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = requests.get(url)

    
    if "Couldn't find any profile with name" in response.text:
        return False  # The username does not exist
    return True  # The username exists

def get_words():
    word_list = ["ign1","ign2","ign3"] 
    return word_list
#    chars = ["i","v","y","x","vi","iyi", "yi"]
#    
#    
#    word = "bolt"
#    
#    
#    variations = []
#   
#
#
#    for i in range(1, 7):  
#        for comb in itertools.product(chars, repeat=i):
#            for idx in itertools.combinations(range(1, 5), i):  
#                temp = list(bolt)  
#                for j, pos in enumerate(idx):
#                    temp.insert(pos, comb[j]) 
#                new_word = "".join(temp)
#                if len(new_word) <= 5:  
#                    variations.append(new_word)
#    
#    return variations
# The function must return a list of strings to be checking as available igns


def contains_invalid_chars(username: str) -> bool:
    
    if re.search(r'[^a-zA-Z]', username):  
        return True
    return False

def main():
    ###
    elements = get_words()

    #print(elements)
    for element in elements:
        if check_username_exists(element):
            print(f"'{element}' NOT AVAILABLE")
            #continue
        else:
            print(f"'{element}' AVAILABLE")

# Run the program
if __name__ == "__main__":
    main()
