


def find_longest_word(sentence: str) -> str:

    longest_word = ''
    current_word = ''
    i = 0
    while i < len(sentence):
        char = sentence[i]
        if char != " ":
            current_word = current_word + char
        else :
            if len(longest_word)< len(current_word):
                longest_word= current_word
                
            current_word = ""
        i += 1
    
    if len(longest_word)< len(current_word):
        longest_word=current_word

    
    return longest_word

def find_longest_word2(sentence: str) -> str:
    longest_word = ''
    current_word = ''
    for i in sentence:
        if i != " ":
            current_word = current_word + i
        else :
            if len(longest_word)< len(current_word):
                longest_word= current_word
                
            current_word = ""
    if len(longest_word)< len(current_word):
        longest_word=current_word
    return longest_word

def find_longest_word3(sentence: str) -> str:
    words = sentence.split() #splitting the words in the sentence
    if not words: 
        return ""
    return max(words, key=len)



sentence = input("enter your sentence to find the longest word in it : ")
longest_word = find_longest_word(sentence)
longest_word2 = find_longest_word2(sentence)
longest_word3 = find_longest_word3(sentence)
print(longest_word)
print("using for loop and split function")
print(longest_word2)
print("using split function this time: ")
print(longest_word3)
                