
class Printer:

    def __init__(self):
        self.storage = ""
    
    def print_paper(self):
        print(self.storage)

    def scan_paper(self, paper):
        self.storage = paper