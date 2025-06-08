import os

with open("Input/Letters/starting_letter.txt", "r") as template_file:
    template = template_file.read()

with open("Input/Names/invited_names.txt", "r") as names_file:
    for name in names_file:
        format_name = name.strip()
        content = template.replace("[name]", format_name)
        with open(f"Output/ReadyToSend/letter_for_{format_name}.txt", "w") as new_file:
                content = content.replace("[name]","Romain")
                new_file.write(content)