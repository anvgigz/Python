

def bottle_song():
    bottles = 100
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down, pass it around, 1 bottle of beer on the wall.\n")
            print("No more bottles of beer on the wall, no more bottles of beer.")
        bottles -= 1
            
bottle_song()