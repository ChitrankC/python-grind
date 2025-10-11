def capitalize_words(text: str) -> str:
    cap_str = [ text.upper(), text.title(), text.capitalize() ]
    return cap_str

str = input("enter the string : ")
cap_str = capitalize_words(str)
print (cap_str)