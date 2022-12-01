def main():
    print('enter two variables')
    result = None
    try:

        integer1 = int(input())
        integer2 = int(input())
        result = integer1/integer2
    except ValueError as err:
        print(err)
        print("You entered the wrong data type")
    except ZeroDivisionError:
        print('Cannot divide by 0, please try again.')
    except:
        print("An unknown error has occurred.")
    else:
        print(result)

main()