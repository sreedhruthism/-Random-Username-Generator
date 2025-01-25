import random
import string

# Predefined lists
adjectives = ["Cool", "Happy", "Funky", "Bright", "Charming", "Swift"]
nouns = ["Tiger", "Dragon", "Eagle", "Panda", "Wolf", "Hawk"]

def generate_username(include_numbers, include_specials, length):
    # Base username: adjective + noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun
    
    # Add numbers if required
    if include_numbers:
        username += str(random.randint(0, 999))
    
    # Add special characters if required
    if include_specials:
        special_char = random.choice(string.punctuation)
        username += special_char
    
    # Adjust length if specified
    if length and length > len(username):
        extra_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=length - len(username)))
        username += extra_chars
    
    return username

def save_usernames_to_file(usernames, filename="usernames.txt"):
    with open(filename, "a") as file:
        for uname in usernames:
            file.write(uname + "\n")
    print(f"Usernames saved to {filename}")

def main():
    print("Welcome to the Random Username Generator!")
    
    # User preferences
    include_numbers = input("Include numbers in the username? (yes/no): ").strip().lower() == "yes"
    include_specials = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    try:
        length = int(input("Specify username length (or press Enter to skip): ") or 0)
    except ValueError:
        length = 0
    
    # Generate usernames
    usernames = [generate_username(include_numbers, include_specials, length) for _ in range(10)]
    
    # Display usernames
    print("\nGenerated Usernames:")
    for uname in usernames:
        print(uname)
    
    # Save to file
    save_user_option = input("\nDo you want to save these usernames to a file? (yes/no): ").strip().lower()
    if save_user_option == "yes":
        save_usernames_to_file(usernames)

if __name__ == "__main__":
    main()
