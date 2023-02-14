
# Ask the user to fill a dictionary of information about 

class task:
    def __init__(self, name, priority, hours, minutes, 
                 isExcite, isAnxious, isBad, isWorth) -> None:
        self.name = name
        self.priority = priority
        self.hours = hours
        self.isExcite = isExcite
        self.isAnxious = isAnxious
        self.isBad = isBad
        self.isWorth = isWorth
        
    def __repr__(self) -> str:
        pass

def main():
    
    print("Hello World!")
    
if __name__ == "__main__":
    main()