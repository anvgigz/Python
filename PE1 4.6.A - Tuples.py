#Assignment: Create and Use Tuples


def print_classes(list_classes):
    for cls in list_classes:
        print(cls)

def print_number_of_classes(count_classes):
    print(f"Number of classes: {len(count_classes)}")

def main():
    programming_classes = (
        'Intro to Python',
        'Advanced Python',
        'Database Essentials',
        'Web Development Basics',
        'Data Structures in Python',
        'Web Design Fundamentals'
    )
    
    print_classes(programming_classes)
    print_number_of_classes(programming_classes)

if __name__ == "__main__":
    main()
