import sys
from argparse import ArgumentParser
import pandas as pd
import matplotlib.pyplot as plt
import json

class Member:
    def __init__(self, data):
        self.data = data
    
    #returns dictionary debtors for get_balance
    def get_member(self, name):
        """ (Ty Hood)
        Retrieves the specific member information given the proper name.

        Parameters:
            name(string): Name of member to search
        Returns: 
            Dict or None: Dictionary that contains member information. If nothing is found, return None.
            
        """
        
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
                return debtor
        return None
    
    #returns total balance for make_payment 
    def get_balance(self, name):
        """
        (joe)
        
        get_balance: takes the user's name as an argument and plugs the name into the get_member function
        to calcualte the user's toll balance

        Args:
        name - string - name of the account holder

        Returns:
        total_balance - float - the calculated total balance of the user
        """
        member_info = self.get_member(name)
        if member_info:
            I95_a = float(member_info["i95_a"]) * 5
            BHT_a = float(member_info["bht_a"]) * 8
            FMT_a = float(member_info["fmt_a"]) * 3
            CBB_a = float(member_info["cbb_a"]) * 12
            
            total_balance = 0
            if member_info["member"].upper() == "Y":
                total_balance = I95_a + BHT_a + FMT_a + CBB_a
                return total_balance
            elif member_info["member"].upper() == "N":
                total_balance = (I95_a + BHT_a + FMT_a + CBB_a) * 1.5
                return total_balance

            
        else:
            print("Name not found in the records.")
    
    def balance_sheet(self):
        """
        Generates or retrieves the balance sheet which is a dictionary mapping
        customer names to their balance.
        
        Returns:
                new_sheet (dict): A dictionary with customer names as keys and their 
                                    corresponding balances.


        """
        new_sheet={}
        for name, information in self.data.items():
            new_sheet[name]= self.get_balance(name)
        return new_sheet
            
    def update_sheet(self, name, newbalance, out_file):
        """
        Updates the balance sheet with a new balance for a specific customer
        and writes the updated balances to a JSON file.
        
        Parameters:
                    name(str): The name of the customer who's balance needs to be updated.
                    newbalance(float): The customer's new balance after payment to update.
                    out_file(str): The filepath where the updated sheet will be saved.
        Returns:
                    updated_sheet(dict): returns the updated balance sheet.
        Side Effects:
                    - Modifies the balance sheet by updating it with the new balance.
                    - Writes the updated balance sheet to a file, altering the file's contents.
                    
        """
        updated_sheet={}
        current_sheet=self.balance_sheet()
        for n, b in current_sheet.items():
            if name ==n :
                updated_sheet[n]= newbalance
            else:
                updated_sheet[n]= b
        
        with open (out_file, "w", encoding = 'utf-8') as outfile:
            json.dump(updated_sheet, outfile, indent=4, separators=(',', ': '))
        
        return updated_sheet
      
        
    
    def make_payment(self, name):
        """
        (joe)

        make_payment: takes a name as input and uses the get_balance function to calculate the 
        total balance. The user then has an option to pay the whole balance or only part. After
        a payment has been recived the balance is updated

        Args:
        name - string - name of the account holder

        Returns:
        new_balance - float - the updated balance of the account holder
        """
       
        payment_balance = self.get_balance(name)
        print(f"\nHello {name}, your balance is ${payment_balance:.2f}.")
        payment_amount = float(input("How much do you want to pay? "))
        member_info = self.get_member(name)
        if not member_info:
            print("record not found")
            pass
        new_balance = payment_balance - payment_amount
        if new_balance < 0:
            new_balance = 0
            print("You overpaid so we refunded the remaining amount to your bank account")
        print(f"Your updated balance is ${new_balance:.2f}.\n")

        return new_balance 


def read_file(filepath):
    #judi
    """ Opens and reads a CSV file that contains the data of the people that have used the toll.
        Each line in the file represents a member's information and is split into components to
        be stored in a dictionary.
        
        Parameters:
            filepath (str): The path to the file thta contains member data.
            
        Returns:
        data (dict): A dictionary where each key is a customer's name, and the value is a list
                containing that customer's information.
    """
    data = {}
    with open(filepath, "r", encoding="utf-8") as infile:
        for line in infile:
            information = line.strip().split(",")
            data[information[0]] = information
    return data


def get_graph(filepath, choice):
    """
    (Ty Hood)
    Creates three different graphs displaying data. 

    Parameters:
        filepath(string): Path to file that holds data (people.txt)
        choice(str): String that determines which graph is shown.
        1 - Average bridge crosses by specific vehicle 
        2 - Different types of vehicles
        3 - Amount of people who have the Purple Pass
    
    """
    df = pd.read_csv(filepath, header=None, names=["name", "member", "license_plate", "vehicle_type", "i95_a", "bht_a", "fmt_a", "cbb_a"])
    
    if choice == "1":
        #average crossings per vehicle type
        bridge_crossings = df.iloc[:, -4:]
        df["total_crossings"] = bridge_crossings.sum(axis=1)
        average_crossings_by_vehicle = df.groupby("vehicle_type")["total_crossings"].mean()
        
        print(average_crossings_by_vehicle)
        
        average_crossings_by_vehicle.plot(kind="bar", color="blue")
        plt.title("Average Bridge Crossings by Vehicle Type")
        plt.xlabel("Vehicle Type")
        plt.ylabel("Average Number of Bridge Crossings")
        plt.xticks(rotation=45)
        plt.grid(axis="y")
        plt.tight_layout()
        plt.show()

    elif choice =="2":
        #number of different vehicles
        key = df.iloc[:, 3]
        keyCount = key.value_counts()
        
        print(keyCount)
        
        keyCount.plot(kind='bar', color='green')
        plt.title('Types of Vehicles')
        plt.xlabel('Vehicles')
        plt.ylabel('Number of Vehicles')
        plt.xticks(rotation=45)
        plt.show()

    elif choice == "3":
        #Number of Purple Pass members vs Non
        key = df.iloc[:, 1]
        keyCount = key.value_counts()
        
        print(keyCount)
        
        keyCount.plot(kind='bar', color=['blue', 'red'])
        plt.title('Purple Pass Members')
        plt.xlabel('Membership Status')
        plt.ylabel('Membership Count')
        plt.xticks(rotation=0)
        plt.show()
    else:
        print(f"Invalid choice {choice}")

#can make more arguments like a new txt file for writing.
def parse_args(arglist):
    """ (Ty Hood)
    Parses the command line arguments
    
    Parameters: 
        argparse: Object holding the parsed arguments
    """
    parser = ArgumentParser()
    parser.add_argument('file', help="Path to file")
    parser.add_argument('outfile', help="path to balance sheet")
    return parser.parse_args(arglist)

def main(filepath, outfile):
    """
    The main function to handle the program's flow. It initiates the program, processes
    user input, and interacts with other functions to search for member information, 
    update balances, generate graphs, and manage the data file based on user choices.
    
    Parameters:
                filepath (str): The path to the file containing consumer data.
                outfile (str): The path to the output file where balance updates are stored.
    Side Effects:
                - Reads from and writes to files given by the user.
                -
                - 
    """
    #judi
    data = read_file(filepath)
    newMem = Member(data)
    while True:
        option = input("What would you like to do?:\n1: Search a name\n2: Graphs\n0: cancel\n")

        if option == "1":
            name = input("What name do you want to look up?: ")
            member = newMem.get_member(name)
            if member:
                newMem.get_balance(name)
            else:
                print(f"{name} not found")
            
            response= input("Would you like to make a payment? Y/N: ")    
            if response == "Y":
                charge= newMem.make_payment(name)
                newMem.update_sheet(name, charge, outfile)
                
            elif response == "N":
                pass
            else:
                print("Please respond 'Y' for Yes or 'N' for No")
            
            
            
            
        elif option == "2":
            choice = input("What do you want to graph?\n1: Crosses by Vehicle\n2: Vehicle Type\n3: Members\n")
            get_graph(filepath, choice)
        
        elif option == "0":
            print("Terminating")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file, args.outfile)
