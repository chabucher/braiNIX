"""References provided command in source tree at ../src/."""

command = input("\nCommand: ").lower()

for index in range(len(command)):

    char = command[index]
    ascii = ord(char)
    add = '+' * ascii
    subtract = '-' * ascii

    with open(f"../src/add/{char}.bf", 'w') as file:
        for line in range(len(add) // 80 + 1):
            file.writelines(add[80 * line: 80 * (line + 1)] + '\n')

    with open(f"../src/subtract/{char}.bf", 'w') as file:
        for line in range(len(subtract) // 80 + 1):
            file.writelines(subtract[80 * line: 80 * (line + 1)] + '\n')

    try:

        with open(f"../src/decode/{command[:index + 1]}.bf", 'r') as file:
            text = file.read()

    except FileNotFoundError:

        if index < len(command) - 1:

            with open(f"../src/decode/{command[:index + 1]}.bf", 'w') as file:
                file.write(f"""+
>
(subtract/{char})
[
    (add/{char})
    <
    -
]
<
[
    -
    >
    (decode/{command[:index + 2]})
    <
]
>""")

        else:

            with open(f"../src/decode/{command}.bf", 'w') as file:
                file.write(f"""+
>
(subtract/{char})
[
    (add/{char})
    <
    -
]
<
[
    -
    >
    (decode/{command}_command)
    <
]
>""")

    else:

        if index < len(command) - 1:

            if f"(decode/{command[:index + 2]})" in text:
                continue

            text = text.split('\n')
            text.insert(12, f"    (decode/{command[:index + 2]})")

            with open(f"../src/decode_{command[:index + 1]}.bf", 'w') as file:
                file.write('\n'.join(text))

        else:

            if f"(decode/{command}_command)" in text:
                continue

            text = text.split('\n')
            text.insert(12, f"    (decode/{command}_command)")

            with open(f"../src/decode/{command[:index + 1]}.bf", 'w') as file:
                file.write('\n'.join(text))

with open(f"../src/commands.bf", 'r') as file:
    text = file.read()

if f"(decode/{command[0]})" not in text:
    text =  text.split('\n')
    text.insert(2, f"    (decode/{command[0]})")

    with open(f"../src/commands.bf", 'w') as file:
        file.write('\n'.join(text))

with open(f"../src/decode/{command}_command.bf", 'w') as file:
    file.write(f"""+
>
(subtract/space)
[
    (add/space)
    <
    -
]
<
[
    -
    >
    (command/{command})
    (clear_cell_down)
    <
]
>""")

print("\nIntegrated into source tree.\n")
