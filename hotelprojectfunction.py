print("''''''''''''WELCOME RDS HOTEL''''''''''''''''")
veg=["dosa","idly","poori","vadai","pongal"]
nonveg=["chickenbriyani","muttonbriyani","chickenrice","thandoori"]
#veg
dosa=25
idly=5
poori=50
vadai=10
pongal=30
#nonveg
chickenbriyani=110
muttonbriyani=150
chickenrice=90
thandoori=380
#user
def veg_or_nonveg(choice):
 if choice=="veg":
        print(f"{veg} items")
        enter=input("what do you want:")
        print(f"{enter} available")
        how_many=int(input(f"How many {enter} you want:"))
        cooldrinks=("pepsi","sprite")
        user=input("you want cooldrinks:")
        pepsi=30
        sprite=35
     
        if  user=="yes":
                print(f"{cooldrinks} are there")
                cool=input("which drinks you want:")
                if cool=="pepsi":
                   print(f"Take a {cooldrinks[0]}")
                elif cool=="sprite":
                   print(f"Take a {cooldrinks[1]}")
                else:
                   print("cooldrinks are not available...")
         
                bottles=int(input(f"How many {cool} bottles you want:"))      
                if enter=="dosa":
                 amount=dosa*how_many+pepsi*bottles or sprite*bottles
                 print(f"your bill is Rs.{amount}")   
                elif enter=="idly":
                 amount=idly*how_many+pepsi*bottles or sprite*bottles
                 print(f"your bill is Rs.{amount}") 
                elif enter=="poori":
                 amount=poori*how_many+pepsi*bottles or sprite*bottles
                 print(f"your bill is Rs.{amount}") 
                elif enter=="vadai":
                 amount=vadai*how_many+pepsi*bottles or sprite*bottles
                 print(f"your bill is Rs.{amount}") 
                elif enter=="pongal":
                 amount=pongal*how_many+pepsi*bottles or sprite*bottles
                 print(f"your bill is Rs.{amount}") 
        else:    
            if enter=="dosa":
                 amount=dosa*how_many+pepsi
                 print(f"your bill is Rs.{amount}")   
            elif enter=="idly":
                 amount=idly*how_many
                 print(f"your bill is Rs.{amount}") 
            elif enter=="poori":
                 amount=poori*how_many
                 print(f"your bill is Rs.{amount}") 
            elif enter=="vadai":
                 amount=vadai*how_many
                 print(f"your bill is Rs.{amount}") 
            elif enter=="pongal":
                 amount=pongal*how_many
                 print(f"your bill is Rs.{amount}")     
#nonveg
 elif choice=="nonveg":
         print(f"{nonveg} are items")
         enter=input("What do want:")
         print(f"{enter} available ")
         how_many=int(input(f"How many {enter} you want:"))
         cooldrinks=("pepsi","sprite")
         user=input("you want cooldrinks:")
         pepsi=30
         sprite=35
         if  user=="yes":
                 print(f"{cooldrinks} are there")
                 cool=input("which drinks you want:")
                 if cool=="pepsi":
                   print(f"Take a {cooldrinks[0]}")
        
                 elif cool=="sprite":
                   print(f"Take a {cooldrinks[1]}")
                 else:
                   print("cooldrinks are not available...")
    
                 bottles=int(input(f"How many {cool} bottles you want:")) 
                 if enter=="chickenbriyani":
                     amount=chickenbriyani*how_many+pepsi*bottles or sprite*bottles
                     print(f"your bill is Rs.{amount}")   
                 elif enter=="muttonbriyani":
                     amount=muttonbriyani*how_many+pepsi*bottles or sprite*bottles
                     print(f"your bill is Rs.{amount}") 
                 elif enter=="chickenrice":
                     amount=chickenrice*how_many+pepsi*bottles or sprite*bottles
                     print(f"your bill is Rs.{amount}") 
                 elif enter=="thandoori":
                     amount=thandoori*how_many+pepsi*bottles or sprite*bottles
                     print(f"your bill is Rs.{amount}") 
         else:
                 if enter=="chickenbriyani":
                     amount=chickenbriyani*how_many
                     print(f"your bill is Rs.{amount}")   
                 elif enter=="muttonbriyani":
                     amount=muttonbriyani*how_many
                     print(f"your bill is Rs.{amount}") 
                 elif enter=="chickenrice":
                     amount=chickenrice*how_many
                     print(f"your bill is Rs.{amount}") 
                 elif enter=="thandoori":
                     amount=thandoori*how_many
                     print(f"your bill is Rs.{amount}") 
 else:
            print("incorrect choice")
#coustmer 
yourchoice=input("Veg or Non-Veg:")
veg_or_nonveg(yourchoice)
    
             
    
    