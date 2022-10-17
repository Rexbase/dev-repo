'''
This programm converts the user's input into a code and runs it.
To use the programm, write your code in the input and then write "launch" on the last line.
For example:
a = 5
print(a)
launch

The output will be "5"

If your code includes input() functions, you should enter values for them after the "launch"
line:
a = input()
print(a)
launch
hello world!

Output: hello world!

code = []
while True:
    code += [(strc:=input()) + "\n"]
    if strc.lower() == "запуск" or strc.lower() == "launch":
        if len(code) == 1:
            del code[len(code)-1]
            print("You should write at least one line of code!")
            continue
        del code[len(code)-1]
        break
    if strc == "":
        break
code = "".join(code)
exec(code)'''


#All credits go to Himanshu Bhandari
#he wrote this code in cpp, i rewrote it in python

ime = input("Enter your name: \n\n")

for c in ime:

    c = c.upper()
    if (c == "A"):
        print("..######..\n..#....#..\n..######..\n..#....#..\n..#....#..\n\n")
    elif (c == "B"):
        print("..######..\n..#....#..\n..#####...\n..#....#..\n..######..\n\n")
    elif (c == "C"):
        print("..######..\n..#.......\n..#.......\n..#.......\n..######..\n\n")
    elif (c == "D"):
        print("..#####...\n..#....#..\n..#....#..\n..#....#..\n..#####...\n\n")
    elif (c == "E"):
        print("..######..\n..#.......\n..#####...\n..#.......\n..######..\n\n")
    elif (c == "F"):
        print("..######..\n..#.......\n..#####...\n..#.......\n..#.......\n\n")
    elif (c == "G"):
        print("..######..\n..#.......\n..#####...\n..#....#..\n..#####...\n\n")
    elif (c == "H"):
        print("..#....#..\n..#....#..\n..######..\n..#....#..\n..#....#..\n\n")
    elif (c == "I"):
        print("..######..\n....##....\n....##....\n....##....\n..######..\n\n")
    elif (c == "J"):
        print("..######..\n....##....\n....##....\n..#.##....\n..####....\n\n")
    elif (c == "K"):
        print("..#...#...\n..#..#....\n..##......\n..#..#....\n..#...#...\n\n")
    elif (c == "L"):
        print("..#.......\n..#.......\n..#.......\n..#.......\n..######..\n\n")
    elif (c == "M"):
        print("..#....#..\n..##..##..\n..#.##.#..\n..#....#..\n..#....#..\n\n")
    elif (c == "N"):
        print("..#....#..\n..##...#..\n..#.#..#..\n..#..#.#..\n..#...##..\n\n")
    elif (c == "O"):
        print("..######..\n..#....#..\n..#....#..\n..#....#..\n..######..\n\n")
    elif (c == "P"):
        print("..######..\n..#....#..\n..######..\n..#.......\n..#.......\n\n")
    elif (c == "Q"):
        print("..######..\n..#....#..\n..#.#..#..\n..#..#.#..\n..######..\n\n")
    elif (c == "R"):
        print("..######..\n..#....#..\n..#.##...\n..#...#...\n..#....#..\n\n")
    elif (c == "S"):
        print("..######..\n..#.......\n..######..\n.......#..\n..######..\n\n")
    elif (c == "T"):
        print("..######..\n....##....\n....##....\n....##....\n....##....\n\n")
    elif (c == "U"):
        print("..#....#..\n..#....#..\n..#....#..\n..#....#..\n..######..\n\n")
    elif (c == "V"):
        print("..#....#..\n..#....#..\n..#....#..\n...#..#...\n....##....\n\n")
    elif (c == "W"):
        print("..#....#..\n..#....#..\n..#.##.#..\n..##..##..\n..#....#..\n\n")
    elif (c == "X"):
        print("..#....#..\n...#..#...\n....##....\n...#..#...\n..#....#..\n\n")
    elif (c == "Y"):
        print("..#....#..\n...#..#...\n....##....\n....##....\n....##....\n\n")
    elif (c == "Z"):
        print("..######..\n......#...\n.....#....\n....#.....\n..######..\n\n")
    elif (c == " "):
        print("..........\n..........\n..........\n..........\n\n")
    elif (c == "."):
        print("----..----\n\n")

