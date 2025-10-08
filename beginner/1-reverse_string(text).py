def reversing(text :str):
    reverse_string=""
    for i in text :
        reverse_string=i+reverse_string
    return reverse_string

text = input("enter text ")
re_text = reversing(text)
print (re_text)


#using slicing method / the shortcut 
def string_reverse(text: str):
    return text[::-1]

print("time for reversing string using slicing method")
string = input("enter string : ")
reverse_string = string_reverse(string)
print(reverse_string)