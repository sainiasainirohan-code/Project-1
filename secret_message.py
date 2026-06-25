diary_password = "12345"
with open("diary.txt","a") as file:
    pass

print("_____MY SECRET DIARY____")
password_attempt = input("Enter your password:")

if diary_password != password_attempt:
    print("wrong password")
else:
    print("acess granted")
    while True:
        print("___ DIARY MENU ___")
        print("1. Write / Save a note")
        print("2. Open and view all notes")
        print("3. Delete everything")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            note = input("\nType your diary entry here:\n> ")
            with open("diary.txt", "a") as file:
                file.write(note + "\n---------------------\n")
            print("Note saved successfully!\n")

        elif choice == "2":
            print("\n--- YOUR DIARY ENTRIES ---")
            with open("diary.txt", "r") as file:
                content = file.read()
            if content == "":
                print("Your diary is currently empty!\n")
            else:
                print(content)
        
        elif choice == "3":
            confirm = input("Are you sure you want to wipe your diary clean? (yes/no): ").lower()
            if confirm == "yes":
                # 'w' mode opens the file fresh, clearing everything out
                with open("diary.txt", "w") as file:
                    file.write("") 
                print("All notes deleted permanently!\n")
                
        elif choice == "4":
            print("Closing diary. Your secrets are safe!")
            break
            
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.\n")