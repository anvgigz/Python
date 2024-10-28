def replace_artist(top_artists):
    while True:
        try:
            # Get user input for the index and new artist name
            index = int(input("Enter the index of the artist to replace: "))
            new_artist = input("Enter the new artist name: ")
            
            # Replace the artist at the specified index
            top_artists[index] = new_artist
            break
        except (ValueError, IndexError):
            print("An input error occurred. Please enter a valid index and artist name.")

def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    
    # Call the function to replace an artist
    replace_artist(top_artists)
    
    # Print the updated list
    print("\nUpdated list of top artists:")
    print(top_artists)

# Entry point of the script
if __name__ == "__main__":
    main()