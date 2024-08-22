with open("Input/Letters/starting_letter.txt") as letter_file:
    template = letter_file.read()

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

for name in names:
    stripped_name = name.strip()
    with open(f"Output/ReadyToSend/{stripped_name}.txt", mode="w") as data:
        data.write(f"{template.replace("[name]", stripped_name)}")


