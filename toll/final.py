import sys
from argparse import ArgumentParser
import pandas as pd
import matplotlib.pyplot as plt

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
            print(f"Hello {member_info['name']},\nyou have passed through I95 {member_info['i95_a']} times,\n"
                  f"The Fort McHenry Tunnel {member_info['fmt_a']} times,\n"
                  f"The Chesapeake Bay Bridge {member_info['cbb_a']} times,\n"
                  #decimal places and $
                  f"and your total balance is ${total_balance:.2f}")
            
        else:
            print("Name not found in the records.")
    def make_payment(self, name):
        #joe
        name = input("what is your name? ")
        member_info = self.get_member(name)
        if not member_info:
            print("record not found")
            return
        payment_balance = self.get_balance(name)
        print(f"Hello {name}, your balance is {payment_balance}.")
        choice = input("Would you like to pay you balance?(Y/N) ")
        if choice.upper() == "Y":
            while True:
                try:payment_amount = float(input("How much do you want to pay? "))
                    break
                except ValueError
            new_balance = payment_balance - payment_amount
            print(f"Your updated balance is {new_balance}")
        elif choice.upper() == "N":
            print("no payment")
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
    #not finished 
    df = pd.read_csv(filepath)
    if choice == "1":
        key = df.iloc[:, 1]
        keyCount = key.value_counts()
        keyCount.plot(kind='bar', color=['blue', 'red'])
        plt.title('Purple Pass Members')
        plt.xlabel('Membership Status')
        plt.ylabel('Membership Count')
        plt.xticks(rotation=0)
        plt.show()
    elif choice =="2":
        key = df.iloc[:, 3]
        key = key.value_counts()
    elif choice == "3":
        key = df.iloc[4:7]
        key = key.value_counts()
    

    if key not in df.columns:
        print(f"{key} doesn't exist")
        return

#can make more arguments like a new txt file for writing.
def parse_args(arglist):
    #Ty
    parser = ArgumentParser()
    parser.add_argument('file', help="Path to file")
    return parser.parse_args(arglist)

#biggest change. we talked about using input statements and it just makes the entire program easier imo
def main(filepath):
    #judi
    data = read_file(filepath)
    newMem = Member(data)
    option = input("What would you like to do?:\n1: Search a name\n2: Check average toll fees\n 0: cancel\n")

    if option == "1":
        name = input("What name do you want to look up?: ")
        member = newMem.get_member(name)
        if member:
            balance = newMem.get_balance(name)
        else:
            print(f"{name} not found")
        
        response= input("Would you like to make a payment? Y/N")    
        if response == "Y":
            charge= newMem.make_payment(name)
            print(charge)
        
    elif option == "2":
        choice = input("What do you want to graph?\n1: Members\n2: Vehicle Type\n3: Bridges\n")
        get_graph(filepath, choice)
    
    elif option == "0":
        print("Terminating")
    else:
        print("Invalid option")


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)

