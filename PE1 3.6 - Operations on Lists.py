global_available_seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def seat_reservation():
    current_event_res = global_available_seats[:]
    while current_event_res:
        print(f"Available seats: {current_event_res}")
        print("Please choose a seat you would like to reserve")
        print("Enter the letter 'O' to continue with purchase")
        
        seat_choice = input()
        if seat_choice == 'O':
            print("Continuing to payment info")
            break
        
        try:
            seat_choice = int(seat_choice)
            if seat_choice not in current_event_res:
                print("Seat is already reserved or invalid.")
            else:
                current_event_res.remove(seat_choice)
                print(f"You have reserved seat {seat_choice}")
        except ValueError:
            print("AHHHH Please enter a valid number.")
    
    if not current_event_res:
        print("All seats have been reserved.")

seat_reservation()