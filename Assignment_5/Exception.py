class Error(Exception):
    pass


class ValueTooSmallError(Error):
    pass


class ValueTooLargeError(Error):
    pass


# GUESS CORRECT NUMBER

number = 10
attempts = 0
f = open("file1.txt", "w")
f.write("Number of attempts: ")
f.close()
while True:
    try:
        f = open("file1.txt", "a")
        num = int(input("Enter a number: "))
        attempts = attempts + 1
        if num < number:
            raise ValueTooSmallError
        elif num > number:
            raise ValueTooLargeError
        elif num == number:
            print("Congratulations! You guessed it correctly.")
            f.write(str(attempts))
            f.close()
            # open and read the file:
            # print("Number of attempts")
            f = open("file1.txt", "r")
            print(f.read())
            f.close()
            break
    # SYSTEM DEFINED EXCEPTION
    except FileNotFoundError:
        print("Exception: File Not Found")
        break
    # USER DEFINED EXCEPTIONS
    except ValueTooSmallError:
        print("Exception: Small Value")
        print()
    except ValueTooLargeError:
        print("Exception: Large Value")
        print()
