class Toll: 
    def __init__(self, path, name): 
        self.path = path
        self.name = name

    def search(self, name):
        with open(self.path, 'r') as file:
            for line in file:
                tollinfo = line.strip().split(",")
                person = [info.strip() for info in tollinfo]
            
                if name in person:
                    debtor = {
                        "name": person[0],
                        "plate": person[1],
                        "axle": person[2],
                        #do we want times_crossed? 
                        "times_crossed": person[3]
                    }
                    return debtor
            
            print(f"{name} wasn't found in our record book.")
            return None

path = "people.txt"
while True: 
    toll = Toll(path, "")
    name = input("Enter name or blank input to exit: ")
    if name == "": 
        break
    toll.name = name
    debtor = toll.search(name)
    if debtor:
        print(debtor.get("axle"))