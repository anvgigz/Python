# Global list of available seats
global_available_seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 

def seat_reservation():
    # Copy global available seats to a local variable to simulate a real event without modifying the global list
    current_event_res = global_available_seats[:]
    
    # Loop until all seats are reserved or the user chooses to continue with the purchase
    while current_event_res:
        print(f"Available seats: {current_event_res}")
        print("Please choose a seat you would like to reserve")
        print("Enter the letter 'O' to continue with purchase")
        
        # Get user input for seat choice
        seat_choice = input()
        
        # Check if the user wants to continue with the purchase
        if seat_choice == 'O':
            print("Continuing to payment info")
            break
        
        try:
            # Convert the input to an integer
            seat_choice = int(seat_choice)
            
            # Check if the chosen seat is available
            if seat_choice not in current_event_res:
                print("Seat is already reserved or invalid.")
            else:
                # Remove the reserved seat from the list
                current_event_res.remove(seat_choice)
                print(f"You have reserved seat {seat_choice}")
        except ValueError:
            # Handle invalid input that cannot be converted to an integer
            print("Please enter a valid number.")
    
    # Check if all seats have been reserved
    if not current_event_res:
        print("All seats have been reserved.")

# Call the function to start the seat reservation process
seat_reservation()
