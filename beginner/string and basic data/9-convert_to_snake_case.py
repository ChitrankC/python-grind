import re

def convert_to_snake_case (sentence: str) -> str | None:
    if not sentence:
        return None
    """
    else:
        sentence = sentence.lower().replace(" ","_")
        return sentence
    """
    
    words = re.findall(r'\w+', sentence.lower())  # extracts only alphanumeric sequences
    return '_'.join(words)
    
sentence = input("enter the sentence to be converted into snake case : ")
snake_case = convert_to_snake_case(sentence)
print(snake_case)
        

