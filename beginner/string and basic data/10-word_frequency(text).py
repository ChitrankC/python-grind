import re

def word_frequency (text: str) -> dict | None:
    if not text:
        return None
    text_refined = re.findall(r'\w+', text.lower())
    word_count = {}
    for i in text_refined:
        word_count[i] = word_count.get(i, 0) + 1
    return word_count


text = input("enter the text : ")
result = word_frequency(text)
print(result)


