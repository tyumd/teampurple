class Toll: 
    def __init__(self, path): 
        self.path = path

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
            
            if name not in tollinfo:
                print(f"{name} wasn't found in our record book.")

path = "people.txt"
toll = Toll(path)
while True: 
    name = input("Enter a name or enter nothing to quit: ")
    if name == "":
        break
    debtor = toll.search(name)
    print(debtor['axle'])