class Toll: 
    def __init__(self, path, name, data): 
        self.path = path
        self.name = name
        self.data = data if data is not None else {}

        
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
                        

    def read_file(filepath):
        """ Opens and reads the file
        """
        data ={}
        with open(filepath, "r", encoding= "utf-8") as infile:
            for line in infile:
                information = line.strip.split(",")
                data[information[0]]=[information[1],
                                    information[2],
                                    information[3], int(information[4]), 
                                    information[5], int(information[6]),
                                    information[7], int(information[8])]
        return data
    
    def search(self, name):
        """ Searches for person's name in toll txt file.

        Args: Name (str): name of the person
        Returns: debtor (dictionary): All relevant information for the person's toll data. (plate, name, 
        times crossed, etc.) If the name isn't found, return None.
        
        """
        name = input("name: ")
        self.name = name
        for info in self.data:
            if info[0] == name:
                debtor = {
                    "name": info[0],
                    "plate": info[1],
                    "axle": int(info[2]),
                    "times_crossed": int(info[3])
                }
                return debtor
                
        print(f"{self.name} wasn't found in our record book.")
        return None

def main(filepath, name, pay_amount =0, location= None):
    """ Main function to recieve information, update information, make a payment, pass a toll
    
    Args:
        filepath
        name
        pay_amount
        location
        
    Side effects:
        Reads the toll data from the file located at "filepath" using read_file
        - If only filepath and name are provided will create instance of 
        Member class and return name, license, vehicle type, toll information and balance
        - If filepath name and pay_amount is provided, will create instance of 
        Member class and Purplepass class
        - 
    """
    #data_dict = read_file(filepath)
    #person_info = Member(data_dict, name)
    #person_info.

path = "people.txt"
test = Toll(path, "", {})
data = test.read_file(path)
debtor = test.search("")
if debtor:
    print(debtor)