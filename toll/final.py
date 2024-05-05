"""
Class notes 4/26
-add repr magic method to return a string with the toll info
-next team meeting - split up all the functions to make sure each member has at least
two methods
-make the data file containing toll info
-find a toll bill to model it after - 5 rows should be good

"""
import sys
from argparse import ArgumentParser

class Members: 
    """
    """
    def __init__(self, dict, person_name): 
        """judi is going to redo this to instatiate correctly
        """
        data = self.dict
        name = self.person_name
        

    def get_balance(self,dict):  
        """ 
        arguments should be readjusted accordingly
        should use name as key to find information of person
        should assign names/ titles to correct indices
        should return information and balance
        """ 
        with open(file_path, "r", encoding="utf-8" ) as f:
                for line in f:
                    lines = line.strip().split(",")
                    on_f_name = lines[0].strip()
                    member = lines[1].strip()
                    license_plate = int(lines[2].strip())
                    vehicle_type = int(lines[3].strip())
                    I95_amount = int(lines[4].strip())
                    BHT_amount = int(lines[5].strip())
                    FMT_amount = int(lines[6].strip())
                    CBB_amount = int(lines[7].strip())
                    

                    if name == on_f_name:
                        print(f"Hello {on_f_name}, you have passed through I95 {I95_amount} times, The Fort 
                        McHenry Tunnel {FMT_amount} times, The Chesapeake Bay Bridge {CBB_amount} times 
                        and ")
                        
    
    def get_member(self, name):
        """ Searches for person's name in toll txt file.

        Args: Name (str): name of the person
        Returns: debtor (dictionary): All relevant information for the person's toll data. (plate, name, 
        times crossed, etc.) If the name isn't found, return None.
        
        should be renamed member and checks if person is member and then returns member info 
        for example would return 
        
        """
        debtor = {}
        for info in self.data.values():
            if info[0].strip() == name:
                debtor = {
                    "name": info[0].strip(),
                    "member": info[1].strip(),
                    "license_plate": info[2].strip(),
                    "vehicle_type": info[3].strip(),
                    "i95_a": info[4].strip(),
                    "bht_a": info[5].strip(),
                    "fmt_a": info[6].strip(),
                    "cbb_a": info[7].strip(),
                    }
        return debtor if debtor else None
                
class Purplepass(Members):
    """ Class will access the member object associated with the name provided.
        Will allow users to use the toll and make payments to their bill.
    """
    def __init__():
        """ overrides members init 
        instansiates arguments passed in
        """
        
    def usetoll(self,dict, name, license= None, location=None, vehicle_type = None ):
        """ 
        judi 
            will need to update locations accordingly
            if name does not exist in members add name and toll information to document 
            if name does exist update information 
            first need to figure out what index to overwrite
        """
        i = 0
        if location != None:
            if location == "Bridge":
                i = 3
            if location == "HWY":
                i =4
            if location == "Otherloc":
                i =5
            if location == "lastloc":
                i=6 
        
        if name in dict:
            p_info= dict[name]
            info_to_change= p_info[i]
            info_to_change += 1
            dict[name] = info_to_change
        if name not in dict:
            default_dict= ["N", license, vehicle_type,0, 0, 0, 0]
            info_to_change= default_dict[1]
            dict[name]= info_to_change
        
            
        
        
    def make_payment():
        """ will allow person to make a payment and will update the file accordingly if person exists
        """
    
def read_file(filepath):
        """ judi 
        Opens and reads the file
        """
        data ={}
        with open(filepath, "r", encoding= "utf-8") as infile:
            for line in infile:
                information = line.strip.split(",")
                data[information[0]]=[information[1],
                                    information[2],
                                    information[3], int(information[4]), 
                                    int(information[5]), int(information[5]),
                                    int(information[6]), int(information[7])]
        return data
    
def parse_args(arglist):
    
    parser = ArgumentParser()
    parser.add_argument('file', help="Path to file")
    parser.add_argument('name', help="Name of specified bill debtor")
    parser.add_argument('-l', '--location', help="Location of bridge")
    parser.add_argument('-p', '--payment', type=float, help="Payment amount")
    return parser.parse_args(arglist)

def main(filepath, name, pay_amount, location, output_file):
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
        
    with open (output_file, "w", encoding = 'utf-8') as outfile:
        outfile.write(f"")
        

    

if __name__ == "__main__":
    args = parse_args(sys.argv[:1])
    main(args.file, args.name, args.location, args.payment)
    