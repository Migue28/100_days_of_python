PLACEHOLDER = "[name]"

letter_dir = "./Input/Letters/starting_letter.txt"
output_dir = "./Output/ReadyToSend"
invited_names_dir = "./Input/Names/invited_names.txt"
with open(letter_dir) as letter:
    placeholder_letter = letter.read()

with open(invited_names_dir) as names:
    name_list = names.readlines()

for name in name_list:
    if name == "\n":
        pass
    else:
        if "\n" in name:
            name_striped = name.strip("\n")
            new_letter = placeholder_letter.replace(PLACEHOLDER, f"{name_striped}")
            new_letter_with_my_name = new_letter.replace("Angela\n", "Aphee")
            with open(f"./Output/ReadyToSend/letter_to_{name_striped}.txt", mode="w") as letter_to_send:
                letter_to_send.write(new_letter_with_my_name)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp