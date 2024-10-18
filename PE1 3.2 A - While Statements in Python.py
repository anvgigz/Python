

def bottle_song():
    bottles = 100
    while bottles > 0: #Program will loop untill 100 decrements to 0
        if bottles > 2: #The If statement loops in the while statement util decremented to 2 >> The the Elif statement is ececuted followed by the ending of the def bottle_song()
            print(f"{bottles} bottles of beer on the wall\n{bottles} bottles of beer.")
            print(f"Take one down, pass it around\n{bottles - 1} bottles of beer on the wall.\n") # bottles -1 decrements 1 from bottles = 100 (so 99 after first loop)
        else: # once 100 
            print("1 bottle of beer on the wall\n1 bottle of beer.")
            print("Take one down, pass it around\n1 bottle of beer on the wall.\n")
            print("No more bottles of beer on the wall")
        bottles -= 1 # end of while statment decrementing bottles(variable) to 0
            
bottle_song()
