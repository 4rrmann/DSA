def process_file():
    try:
        f = open(r"C:\Users\arrma\OneDrive\Desktop\JUPYTER PROJECTS\.ipynb\DSA\python\AdvPyPractice\ExceptionHandling\data.txt")
        
        x = 1/0

    except FileExistsError as e:
        print("inside except")
        
    finally:
        print("cleaning up file\n")
        f.close()

process_file()