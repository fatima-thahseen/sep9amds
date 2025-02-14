def reverse_string(s):
    """Return the reversed version of a string."""
    return s[::-1] if s else "You entered an empty string!"

def reverse_words(s):
    """Reverse each word in the string while keeping word order."""
    return " ".join(word[::-1] for word in s.split()) if s else "You entered an empty string!"


print("✨ Welcome to the Advanced String Reverser! ✨")

while True:
    
    text = input("\nEnter a string to reverse (or type 'exit' to quit): ").strip()
    
    if text.lower() == "exit":
        print("Goodbye! Thanks for using the program. 😊")
        break
 
    print("\nChoose an option:")
    print("1. Reverse entire string")
    print("2. Reverse each word individually")
    
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        print("Reversed String:", reverse_string(text))
    elif choice == "2":
        print("Reversed Words:", reverse_words(text))
    else:
        print("❌ Invalid choice! Please enter 1 or 2.")

    again = input("\nDo you want to reverse another string? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye! Have a great day! 😊")
        break










