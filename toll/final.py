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
        
def toll(self, name, license_number = None):
        file_path = "toll/people.txt"
        self.name = name
        self.license_number = license_number if license_number is not None \
                                                                else None
        with open(file_path, "r", encoding="utf-8" ) as f:
            for line in f:
                lines = line.strip().split(",")
                on_f_name = lines[0].strip()
                on_f_license_number = lines[1].strip()
                toll_number = int(lines[2].strip())
                toll_amount = int(lines[3].strip())
                balance = toll_number*toll_amount

                if name == on_f_name:
                    print(f"Hello {on_f_name}, you have a balance of {balance}")

                elif license_number == on_f_license_number:
                    print(f"Hello {on_f_name}, you have a balance of {balance}")
                else:
                    print("We have no record of your transactions")
