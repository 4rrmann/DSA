def process_file():
    try:
        f = open("data.txt")
        
        x = 1 / 0

    # except ZeroDivisionError as e:
    #     print("Inside except: ")
    #     print(e)

    finally:
        # The finally block always executes, regardless of exceptions
        print("\nCleaning up file\n")
        f.close()

process_file()