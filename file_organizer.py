import os

def create_directories():
    # Define the main directory name
    main_dir = "MyFiles"
    
    # Define the subdirectory names
    sub_dirs = ["Docs", "Images", "Videos"]
    
    try:
        # Create the main directory
        if not os.path.exists(main_dir):
            os.mkdir(main_dir)
            print(f"Directory {main_dir} created")
        
        # Create each subdirectory
        for sub_dir in sub_dirs:
            sub_dir_path = os.path.join(main_dir, sub_dir)
            if not os.path.exists(sub_dir_path):
                os.mkdir(sub_dir_path)
                print(f"Subdirectory {sub_dir_path} created")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to create directories
create_directories()
