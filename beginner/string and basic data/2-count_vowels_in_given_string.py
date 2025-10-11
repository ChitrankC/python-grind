def count_vowels(sen : str):
    count = 0
    sen = sen.lower() # normalize input by lowering all the cases in the sentence making sure that all the vowels are counted capital or lower both 
    for i in sen:
        if i in ['i', 'a', 'e', 'o', 'u'] :
            count+= 1
    return count

sentence = input("enter string or sentence : ") 
count = count_vowels(sentence)
print(count)

