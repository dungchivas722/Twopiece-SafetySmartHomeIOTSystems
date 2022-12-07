class program():
    def __init__(self):
            super(program, self).__init__()
            print("program 1")
    def sub_program1(self):
        print("sub program 1")

if __name__ == "__main__":
        a = program()
        a.sub_program_1()
