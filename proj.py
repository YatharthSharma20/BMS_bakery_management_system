import datetime as dt 
import pandas as pd 

#orders DataFrame before starting the loop to prevent data loss
orders = pd.DataFrame(columns=["CUSTOMER NAME", "ORDER", "ORDER QUANTITY", "DATE"])

while True:
    print("CHOOSE YOUR PREFERENCE :)")
    print("1. ADD ORDER")
    print("2. VIEW ORDER")
    print("3. SAVE TO EXCEL")
    print("4. EXIT")
    
    x = int(input("ENTER YOUR CHOICE (From 1 to 4):"))

    # 1. ADD ORDER
    if x == 1:
        while True:
            n = input("ENTER CUSTOMER NAME :")
            o = input("ENTER YOUR ORDER (CAKE/PASTRY/BREAD):")
    
            # Handling specific orders
            if o.lower() in ["cake", "cakes","CAKE","CAKES"]:
                print(" ")
                print("PLEASE LET US KNOW WHICH CAKE DO YOU WANT :)")
                print("1. CHOCOLATE CAKE")
                print("2. CHEESE CAKE")
                print("3. RED VELVET CAKE")
                ca = int(input("ENTER YOUR CHOICE (From 1 to 3) :"))
                if ca == 1:
                    o = "CHOCOLATE CAKE"
                elif ca == 2:
                    o = "CHEESE CAKE"
                elif ca == 3:
                    o = "RED VELVET CAKE"
                else:
                    print("Invalid choice! Please select between 1, 2, and 3.")
                    exit()

            elif o.lower() in ["pastry", "pastries","PASTRY","PASTRYS"]:
                print(" ")
                print("PLEASE LET US KNOW WHICH PASTRY DO YOU WANT :)")
                print("1. CHOCOLATE PASTRY")
                print("2. BLACK FOREST PASTRY")
                print("3. RED VELVET PASTRY")
                pa = int(input("ENTER YOUR CHOICE (From 1 to 3) :"))
                if pa == 1:
                    o = "CHOCOLATE PASTRY"
                elif pa == 2:
                    o = "BLACK FOREST PASTRY"
                elif pa == 3:
                    o = "RED VELVET PASTRY"
                else:
                    print("Invalid choice! Please select between 1, 2, and 3.")
                    exit()

            elif o.lower() in ["bread", "breads","BREAD","BREADS"]:
                print(" ")
                print("PLEASE LET US KNOW WHICH BREAD DO YOU WANT :)")
                print("1. WHOLE WHEAT BREAD")
                print("2. CROISSANT")
                print("3. WHITE BREAD")
                br = int(input("ENTER YOUR CHOICE (From 1 to 3) :"))
                if br == 1:
                    o = "WHOLE WHEAT BREAD"
                elif br == 2:
                    o = "CROISSANT"
                elif br == 3:
                    o = "WHITE BREAD"
                else:
                    print("Invalid choice! Please select between 1, 2, and 3.")
                    exit()
            else:
                print("Invalid order type! Please choose between CAKE, PASTRY, and BREAD :)")
                exit()

            q = int(input("ENTER QUANTITY OF FOOD :"))
            od = input("ENTER ORDER DATE (DDMMYYYY):")

            try: 
                # Convert to datetime
                d = dt.datetime.strptime(od, "%d%m%Y")
            except ValueError:
                print("Invalid date format! Please enter the date in DDMMYYYY format :)")
                exit()
            
            #save order using dataframe
            new_order = pd.DataFrame([{"CUSTOMER NAME": n, "ORDER": o, "ORDER QUANTITY": q, "DATE": d.strftime("%Y-%m-%d")}])
            orders = pd.concat([orders, new_order], ignore_index=True)


            x1=input("DO YOU WANT TO ADD MORE ITEMS IN ORDER ? (YES or NO) :")
            
            if x1.lower() == "no":
                print("THANK YOU, YOUR ORDER HAS BEEN PLACED :)")
                break  
    
    #TO SHOW ORDER
    elif x == 2:
        print(orders)

    # Save to CSV
    elif x == 3:
        excel=input("PLEASE ENTER LOCATION FOR EXCEL TO SAVE : ")
        path=excel+"/orders.csv"
        if not pd.io.common.file_exists(path):
            orders.to_csv(path, mode='w', header=True, index=False)
        else:
            orders.to_csv(path, mode='a', header=False, index=False)
        print(f"Your orders have been saved to '{path}':)")

    #exit from bakery
    elif x == 4:
        print("THANK YOU, FOR VISITING FOR OUR BAKERY :)")
        break