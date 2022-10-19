# with open("new_file.txt", mode="w") as file:
#     file.write("New text and file.")

with open("C:/Users/migue/Desktop/new_file.txt") as file:
    content = file.read()
    print(content)

with open("../../../../../Desktop/new_file.txt") as file:
    content = file.read()
    print(content)


