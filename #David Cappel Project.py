#David Cappel Project

def sequence():
    print("What is my name?:")
    g= str(input())
    if g[0] == "d":
        print("Must be capitol")
        sequence()
    elif g[0] == "D":
        print("perfect")
print("hello")        
sequence()
       