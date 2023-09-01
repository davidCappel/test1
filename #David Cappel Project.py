#David Cappel Project
g= str(input())
def sequence():
    print("What is my name?")
    if g[0] == "d":
        print("Must be capitol")
        sequence()
    elif g[0] == "D":
        print("perfect")