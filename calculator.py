#changing to main_app.py for import


class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return 0

    def m_plus(self, memory, memory_store):
        import importlib
        main_app = importlib.import_module("main-app")

        memory_store[0] = memory.pop()
        #print(last_value)
        main_app.displayResult(memory_store[0])
        print("was added to memory." + "\n")

    def m_reset(self, memory, memory_store):
        #import importlib
        #main_app = importlib.import_module("main-app")

        memory.clear()
        memory_store.clear()
        memory.append(0)
        memory_store.append(0)
        print("Memory was cleared")
        #main_app.displayResult(0)

    def m_recall(self, memory_store):
        import importlib
        main_app = importlib.import_module("main-app")

        stored_value = memory_store[0]
        main_app.displayResult(stored_value)

    def switch_display_list(self, mode):
        print("You are in " + mode)
        modes = ["decimal", "hexadecimal", "binary", "octal"]
        index = modes.index(mode)


    def switch_display_input(self, mode):
        import importlib
        main_app = importlib.import_module("main-app")

        print("You are in " + mode)
        new_mode = input("Input a new mode. \n")
        modes = ["decimal", "hexadecimal", "binary", "octal"]
        if new_mode in modes:
            print("You have switched to " + new_mode + ".")
            main_app.mode = new_mode
        else:
            print("That is not a valid mode.")



# add lots more methods to this calculator class.
