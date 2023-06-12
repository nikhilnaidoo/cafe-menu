#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# imports nessesary for program 
from PyDictionary import PyDictionary
import spacy
# covert words 
nlp = spacy.load('en_core_web_sm')
dictionary = PyDictionary()

# creating options 
print("Welcome to Vocabulary 101")
print("Please choose from the following options:")
print("1. Add prefix un to a word")
print("2. Add prefixes to word groups")
print("3. Remove a suffix from a word")
print("4. Extract and transform a word")

# creating a def and point to loop back to 
def lang(word_sis):
    if word_sis == "1": # if used to s
        word = input("Please enter a word to add the prefix un: ")
        result = "un" + word # adding un to word 
        print(result)
        print(dictionary.meaning(result)) # creating dictionary def 
        
    elif word_sis == "2":
        prefix_word = []  # Initialize list to store prefixed words
        word_prefix = []
        make_words = int(input("Please enter the number of words you would like to add prefixes to: ")) # creating length of list 
        for _ in range(make_words): 
            prefix = input("Please enter the prefix you would like to add: ")
            word_to_add = input(f"Please enter the word you would like to add '{prefix}' to: ")
            prefixed_word = prefix + word_to_add # creating new word 
            prefix_word.append(prefixed_word) # appending list
            word_prefix.append(prefix + ":" + word_to_add) 
            
        print(*prefix_word, sep='\n')  # Print the list of prefixed words sepratly 
        for word in prefix_word:
            meanings = dictionary.meaning(word) # creating meaning from dictionary 
            
            if meanings:
                print(f"Meanings of {word}:") 
                for pos, meaning in meanings.items():
                    print(f"{pos}: {', '.join(meaning)}")# creating a print with definition
            else:
                print(f"No meanings found for {word}")
                    
    elif word_sis == "3":
        word = input("Please enter the word you would like to remove suffix 'ness' from: ")
        if word.endswith("ness"):
            modified_word = word[:-4]# slicing last 4 letters
            if modified_word[-1] == "i": # if i last letter to remove
                modified_word = modified_word[:-1] + "y" # modifing word with y if i
            print(f"Modified word: {modified_word}")
            print(dictionary.meaning(modified_word))
        else:
            print("The word does not end with 'ness'.")
        
        
    elif word_sis == "4":
        doc = nlp(input("Please write the sentence you would like to analyze: ")) # creating npl doc
        print([(w.text, w.pos_) for w in doc]) # converting 
        print("Words with the tag 'ADJ' are adjectives.")
        print("Adjectives can be converted into verbs by adding the suffixes -ate, -ise, -en, and -ify to root words ending in 'e'. Words that end in 'y' change to 'i' before adding the suffix. Words that end in 'e' drop the 'e' before adding the suffix.")
        print("Please add the correct suffixes and apply the correct rule.")
        adjective = input("Please enter the adjective to become a verb: ") # asking for word to convert 
        print(dictionary.meaning(adjective))
                

while True:
    # creating function for program
    word_sis = input("Please enter a number from the options above. To end the session, enter 'finish': ").lower()

    if word_sis == "finish":
        print("Thank you for the session")
        break
        # handel errors from sis 
    while word_sis not in["1","2","3","4", "finish"]:
        print("\nincorrect input please try again")
        word_sis = input("Please enterhappy a number from the options above. To end the session, enter 'finish': ").lower()
        # creats loop using def
    lang(word_sis)

