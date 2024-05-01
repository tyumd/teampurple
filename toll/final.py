"""
Class notes 4/26
-add repr magic method to return a string with the toll info
-next team meeting - split up all the functions to make sure each member has at least
two methods
-make the data file containing toll info
-find a toll bill to model it after - 5 rows should be good

"""

class Members: 
    """
    """
    def __init__(self, path, name, data): 
        """judi is going to redo this to instatiate correctly
        """
        self.path = path
        self.name = name
        self.data = data if data is not None else {}

        
    def toll(self, name, license_number = None):
        """should be renamed get_balance
            should calculate balance. 
            toll price will be different depending on vehicle type--- options are:
            GOV(x1.1), COMMERCIAL(x1.2), TRUCK(2), MOTORCYCLE(x1), SEDAN(1.5), SUV(1.7)
            location options will be:
            MD-->1.50, DC-->2.00, VA-->1.20, OTHER-->3.00
            price will be location*vehicle type. ex: truck in dc is 4.00
            print statements will be similar to what you have now feel free to adjust as you see best
            
        """
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
                        
    
    def search(self, name):
        """ Searches for person's name in toll txt file.

        Args: Name (str): name of the person
        Returns: debtor (dictionary): All relevant information for the person's toll data. (plate, name, 
        times crossed, etc.) If the name isn't found, return None.
        
        should be renamed member and checks if person is member and then returns member info 
        for example would return 
        
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
    
class Purplepass(Members):
    """ Class will access the member object associated with the name provided.
        Will allow users to use the toll and make payments to their bill.
    """
    def __init__():
        """ overrides members init 
        instansiates arguments passed in
        """
        
    def usetoll():
        """ if name does not exist in members add name and toll information to document 
            if name does exist update information 
        """
        
    def make_payment():
        """ will allow person to make a payment and will update the file accordingly if person exists
        """
    
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
    

def main(filepath, name, pay_amount, location):
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
    data_dict = read_file(filepath)
    person_info = Members(data_dict, name)
    if location is not None:
        person_info.usetoll(location)
    
    if pay_amount is not None:
        person_info.make_payment(pay_amount)
        

    
