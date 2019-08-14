import json
import pandas as pd 

class Invoice(): 
    
    def __init__(self): 
        self.name = input("Enter your name:")
        self.date = input("Enter the date: ")
        self.address = input("Enter your address: ")
        self.account_number = input('Enter your account number: ')
        
        user_data = {"Name": [], "Date" : [], "Address" : [], "Account Number" : []}
                
        user_data['Name'].append(self.name)
        user_data['Date'].append(self.date)
        user_data['Address'].append(self.address)
        user_data['Account Number'].append(self.account_number)
            
        filepath = "user_data.txt"
        
        with open(filepath, 'w') as f_obj: 
            json.dump(user_data, f_obj)
            
            
    def user_data(): 
        filepath = "user_data.txt"
        
        with open(filepath, 'r') as f_obj: 
            user_data = json.load(f_obj)
            
        user_df = pd.DataFrame.from_dict(user_data)
        #user_df = user_df.set_index(["Name"])
        return user_df 
    
    def items(): 
        another = 0
        item_dict = {'Item Name': [], 'Price': [], 'Quantity': [], "Cost": [], 'Taxable': [], "State": []}
        while another != 'n':
            item_name = input("Enter item name: ")
            price = input("Price: ")
            quantity = input("Quantity: ")
            tax = input("Taxable (true/false): ")
            state = input("Enter your state: ")
            another = input("Add another item (y/n): ")
            cost = float(price) * float(quantity)
            
            item_dict['Item Name'].append(item_name)
            item_dict['Price'].append(price)
            item_dict['Quantity'].append(quantity)
            item_dict['Cost'].append(cost)
            item_dict['Taxable'].append(tax)
            item_dict['State'].append(state)
            
        else: 
            item_df = pd.DataFrame.from_dict(item_dict)
            #item_df = item_df.set_index(["Item Name"])
            #global item_df
            #return item_df
            
            filepath = "user_items.txt"
        
            with open(filepath, 'w') as f_obj: 
                json.dump(item_dict, f_obj)
        
    def calc_totals(): 
        Invoice.items()
        
        filepath = "user_items.txt"
        
        with open(filepath, 'r') as f_obj: 
            user_items = json.load(f_obj)
            
        item_df = pd.DataFrame.from_dict(user_items)
            
        subtotal = 0
        for item in item_df['Cost']: 
            subtotal += float(item)
        
        tax = 0
        for item in item_df.index: 
            itemCost = float(item_df.get_value(item, "Cost"))
            itemTax = item_df.get_value(item, "Taxable")
            itemState = item_df.get_value(item, "State")
            
            if itemTax == "true": 
                if itemState == "MD":
                    tax += (itemCost * 0.06)
                if itemState == "VA":
                    tax += (itemCost * 0.0575)
                if itemState == "DC":
                    tax += (itemCost * 0.0530)
                if itemState == "other":
                    tax += (itemCost * 0.05)
        
        total = 0
        total = subtotal + tax
        
        #Invoice.user_data()
        filepath = "user_data.txt"
        
        with open(filepath, 'r') as f_obj: 
            user_data = json.load(f_obj)
            
        user_df = pd.DataFrame.from_dict(user_data)
        print(user_df)
        print ("\n")
        
        print(item_df)
        print ("\n")
        
        print(f"Subtotal: {subtotal}")
        print(f"Tax: {tax}")
        print(f"Total: {total}")