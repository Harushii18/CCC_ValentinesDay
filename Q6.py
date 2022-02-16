#need this to determine the consonants
vowel=["a","e","i","o","u", "y"]
word=input()
while (word!="quit!"):
    #if it has length 4-> output immeidately
    if (len(word)<=4):
        print(word)
    else:
        #get the suffix pos
        wordlen=len(word)-3
        suffix=word[wordlen:]
        if ((suffix[1]+suffix[2])=="or"):
            #change word to use our instead of or
            if (suffix[0] not in vowel):
                print(word[:wordlen+1]+"our")
            else:
                print(word)
        else:
            print(word);
    #get input again
    word=input()