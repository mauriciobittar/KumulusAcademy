print("would you like to continue?")
bool1 = 'a'

while bool1 != 'yes' and bool1 != 'no':
    bool1 = input()
    if bool1 == 'yes':
        print("Continuing...")
        print("Complete")
        break
    elif bool1 == 'no':
        print("Exiting")
        break
    print("Please try again and respond with yes or no.")
        