class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def print_exception(self):
        print("User defined exception:", self.msg)

try:
    raise Accident("crash between cars")
except Accident as e:
    e.print_exception()

# try:
#     raise MemoryError("memory error")
# except MemoryError as e:
#     print(e)