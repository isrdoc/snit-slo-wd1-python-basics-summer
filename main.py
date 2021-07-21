with open("ninja.txt", "r") as ninja_file:
    contents = ninja_file.read()
    lines = contents.splitlines()

    for line in lines:
        print(line)

with open("ninja2.txt", "w") as ninja_file_2:
    ninja_file_2.write("Hello, new file!")
