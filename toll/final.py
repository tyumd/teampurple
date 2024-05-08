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
        #Ty
        
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
    
    #fix calculation 
    #returns total balance for make_payment 
    #doesnt need a with open statement anymore
    def get_balance(self, name):
        #joe
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
        new_sheet={}
        for name, information in self.data.items():
            new_sheet[name]= self.get_balance(name)
        return new_sheet
            
    def update_sheet(self, name, newbalance, out_file):
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
        #joe
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
        print(f"Your updated balance is {new_balance}\n")

        return new_balance 

#fix reading syntax line.strip didnt have () 
def read_file(filepath):
    #judi
    """ Opens and reads the file """
    data = {}
    with open(filepath, "r", encoding="utf-8") as infile:
        for line in infile:
            information = line.strip().split(",")
            data[information[0]] = information
    return data

#graphs some info from txt file. PEOPLE TXT NOT THE NEW ONE
def get_graph(filepath, choice):
    #Ty
    df = pd.read_csv(filepath, header=None, names=["name", "member", "license_plate", "vehicle_type", "i95_a", "bht_a", "fmt_a", "cbb_a"])
    if choice == "1":
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
    #Ty
    parser = ArgumentParser()
    parser.add_argument('file', help="Path to file")
    parser.add_argument('outfile', help="path to balance sheet")
    return parser.parse_args(arglist)

#biggest change. we talked about using input statements and it just makes the entire program easier imo
def main(filepath, outfile):
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
            choice = input("What do you want to graph?\n1: Crosses by Vehicle\n2: Vehicle Type\n3: Members")
            get_graph(filepath, choice)
        
        elif option == "0":
            print("Terminating")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file, args.outfile)
