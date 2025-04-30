
import sys
def calling():
    isVowel= lambda c:c.lower() in 'aeiou'
    check=input("Enter a character: ")
    isVowel(check)
    if isVowel(check):
        print(f"{check} is a vowel")
    else:
        print(f"{check} is a consonant")
    while True:
        # Ask the user if they want to continue
        print("Do you want to continue? (yes/no)")
        choice = input().lower()
        if choice == 'yes':
            calling()
        elif choice == 'no':
            print("Exiting the program.")
            sys.exit()
        else:
            continue
calling()
# In the above code, I have used a lambda function to check if the character is a vowel or consonant.