def main():
    while True:
        print("\n=== Shop Menu ===")
        print("1. View items")
        print("2. Exit")
        
        choice = input("Enter your choice (1-2): ")
        
        if choice == "1":
            print("Viewing items...")  # Placeholder for item viewing functionality
        elif choice == "2":
            print("Thank you for visiting the shop!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()