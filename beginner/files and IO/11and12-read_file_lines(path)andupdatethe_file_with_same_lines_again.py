

def read_file_lines(path: str) -> list:
    try:
        with open (path, 'r') as open_file:
            line_list = open_file.readlines()
        return line_list
        
    except FileNotFoundError:
        print(f"Error: The file at path '{path}' was not found.")
        return None
        
# funciton for updating the lines inside the same path file
def add_new_list_line(path: str, l: list) :
    for i in l:
        with open(path, 'a') as f:
            f.write(i)
    with open(path, 'r') as f:
        print(f.read())



file_path = input("enter the path of the file example : d:/python-grind/beginner/files and IO/ : ")
lines_list = read_file_lines(file_path)

if not lines_list:
    print("No lines found")
else:print(lines_list)


print("now adding these list in the same file as new lines")
add_new_list_line(file_path, lines_list)