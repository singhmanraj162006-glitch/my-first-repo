'''
import sys
class Home:
    def homeFun(this):
        print("\n\n====================================================================================================================")
        print("1- Menu")
        print("2- New Customer")
        print("3- Exit")
        ch1=int(input("Enter your choice :"))
        return ch1
        
class Customer(Home):
    c=[]
    def custFun(this):
        print("\n\n======================================================================================================================")
        nm=input("Enter Customer Name - ")
        cid=input("Enter Customer ID - ")
        this.c.append(cid)
        this.c.append(nm)
        dy=input("Do you want to continue(y/n)? - ")
        return dy
    
class Menu(Customer):
    total=0    
    def disMenu(this):
       
            print("\n\n====================================================================================================================")
            print("1- Tea")
            print("2- Coffee")
            print("3- ColdDrink")
            print("4- Shakes")
            print("5- Exit")
            mc=int(input('\nEnter your choice-'))
            return mc


class Tea(Menu):
    t=[]
    tt=1
    def disTea(this):
        print('\n\n========================================== Tea Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- White Tea \t\t\t\t ₹ 10')
        print('b- Black Tea \t\t\t ₹ 15')
        print('c- Green \t\t\t ₹ 20')
        print('d- Herbal Tea\t\t\t ₹ 30')
        tc=input('\nEnter your order-')
        tq=int(input('Enter quantity-'))
        if tc=='a':
            tc='White Tea'
            tt=10*tq
        if tc=='b':
            tc='Black Tea'
            tt=15*tq
        if tc=='c':
            tc='Green Tea'
            tt=20*tq
        if tc=='d':
            tc='Herbal Tea'
            tt=30*tq
        this.t.append(tc)
        this.t.append(tq)
        this.t.append(tt)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

        
class Coffee(Tea):
    cf=[]
    cft=1
    def disCoffee(this):
        print('\n\n========================================== Coffee Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- Cold Coffee \t\t\t\t ₹ 100')
        print('b- Hot Coffee \t\t\t ₹ 50')
        print('c- Chocolate Coffee \t\t\t ₹ 150')
        cfc=input('\nEnter your order-')
        cfq=int(input('Enter quantity-'))
        if cfc=='a':
            cfc='Cold Coffee'
            cft=100*cfq
        if cfc=='b':
            cfc='Hot Coffee'
            cft=50*cfq
        if cfc=='c':
            cfc='Chocolate Coffee'
            cft=150*cfq
        this.cf.append(cfc)
        this.cf.append(cfq)
        this.cf.append(cft)
        dy=input("Do you want to continue(y/n)? - ")
        return dy


class ColdDrink(Coffee):
    cd=[]
    cdt=1
    def disColdDrink(this):
        print('\n\n========================================== Cold Drink Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- Thumbs-up \t\t\t\t ₹ 20')
        print('b- Sprite \t\t\t\t ₹ 30')
        print('c- Mountain-Dew \t\t\t\t ₹ 50')
        print('d- Mirinda \t\t\t\t ₹ 50')
        print('e- CoCo-Cola \t\t\t\t ₹ 30')
        print('f- Jira-Soda \t\t\t\t ₹ 30')
        print('g- Red-Bull \t\t\t\t ₹ 100')
        cdc=input('\nEnter your order-')
        cdq=int(input('Enter quantity-'))
        if cdc=='a':
            cdc='Thumbs-up'
            cdt=20*cdq
        if cdc=='b':
            cdc='Sprite'
            cdt=30*cdq
        if cdc=='c':
            cdc='Mountain-Dew'
            cdt=50*cdq
        if cdc=='d':
            cdc='Mirinda'
            cdt=50*cdq
        if cdc=='e':
            cdc='CoCo-Cola'
            cdt=30*cdq
        if cdc=='f':
            cdc='Jira-Soda'
            cdt=30*cdq
        if cdc=='g':
            cdc='Red-Bull'
            cdt=100*cdq
        this.cd.append(cdc)
        this.cd.append(cdq)
        this.cd.append(cdt)
        dy=input("Do you want to continue(y/n)? - ")
        return dy                

class Shakes(ColdDrink):
    sn=[]
    snt=1
    def disShakes(this):
        print('\n\n========================================== Shakes Items ===============================================================')
        print('Item Name \t\t\t\t Price')
        print("--------------------------------------------------------------------------------------------------------------------------")
        print('a- Oreo \t\t\t\t ₹ 200')
        print('b- Kitkat \t\t\t\t ₹ 200')
        print('c- Caramel \t\t\t\t ₹ 220')
        print('d- Java Chip \t\t\t\t ₹ 220')
        print('e- Mocha \t\t\t\t ₹ 220')
        snc=input('\nEnter your order-')
        snq=int(input('Enter quantity-'))
        if snc=='a':
            snc='Oreo'
            snt=20*snq
        if snc=='b':
            snc='Kitkat'
            snt=20*snq
        if snc=='c':
            snc='Caramel'
            snt=20*snq
        if snc=='d':
            snc='Java Chip'
            snt=20*snq
        if snc=='e':
            snc='Mocha'
            snt=20*snq
        this.sn.append(snc)
        this.sn.append(snq)
        this.sn.append(snt)
        dy=input("Do you want to continue(y/n)? - ")
        return dy

    def end(this):
            cl=len(this.c)
            
            tl=len(this.t)
            cfl=len(this.cf)
            cdl=len(this.cd)
            snl=len(this.sn)
            
            if cl>0:
                print("\n\n****************************************")
                print("\n================================================== BILL ===============================================================")
                print("Customer Details-")
                print("ID - "+this.c[0])
                print("Name - "+this.c[1])
                print('\n\n=====================================================================================================================')
                print('Item Name \t\t\t\t\t Quantity \t\t\t Total')
                print("-------------------------------------------------------------------------------------------------------------------------")
               
    
                if tl>0:
                    temp=0
                    try:
                        while temp<=tl:
                            print(this.t[temp],' \t\t\t\t\t ',end='')
                            temp+=1
                            print(this.t[temp],end='')
                            temp+=1
                            print('\t\t\t\t',this.t[temp])
                            this.total=this.total+int(this.t[temp])
                            temp+=1
                    except IndexError:
                        pass
    
                if cfl>0:
                    temp=0
                    try:
                        while temp<=cfl:
                            print(this.cf[temp],' \t\t\t\t\t ',end='')
                            temp+=1
                            print(this.cf[temp],end='')
                            temp+=1
                            print('\t\t\t\t',this.cf[temp])
                            this.total=this.total+int(this.cf[temp])
                            temp+=1
                    except IndexError:
                        pass
    
                if cdl>0:
                    temp=0
                    try:
                        while temp<=cdl:
                            print(this.cd[temp],' \t\t\t\t\t ',end='')
                            temp+=1
                            print(this.cd[temp],end='')
                            temp+=1
                            print('\t\t\t\t',this.cd[temp])
                            this.total=this.total+int(this.cd[temp])
                            temp+=1
                    except IndexError:
                        pass
    
                if snl>0:
                    temp=0
                    try:
                        while temp<=snl:
                            print(this.sn[temp],' \t\t\t\t\t ',end='')
                            temp+=1
                            print(this.sn[temp],end='')
                            temp+=1
                            print('\t\t\t\t',this.sn[temp])
                            this.total=this.total+int(this.sn[temp])
                            temp+=1
                    except IndexError:
                        pass
                
                print("--------------------------------------------------------------------------------------------------------------------")
                print('Total Amount : ',this.total)
                sys.exit()
                        
                              
            else:
                sys.exit()
        
  
while True:
    h=Shakes()
    ch=h.homeFun()
    if(ch==1):#for displaying menu
        mc=h.disMenu()
        if mc==5:#for displaying home menu
            ch=h.homeFun()
        if mc==1:#for displaying Tea menu
            dy=h.disTea()
            if dy=='y':
                continue
            if dy=='n':
                h.end()
        if mc==2:#for displaying Coffee menu
            dy=h.disCoffee()
            if dy=='y':
                continue
            if dy=='n':
                h.end()
        if mc==3:#for displaying ColdDrink menu
            dy=h.disColdDrink()
            if dy=='y':
                continue
            if dy=='n':
                h.end()
        if mc==8:#for displaying Shakes menu
            dy=h.disShakes()
            if dy=='y':
                continue
            if dy=='n':
                h.end()
                
    if(ch==2):
        dy=h.custFun()
        if dy=='y':
            continue
        if dy=='n':
            h.end()
            
    if(ch==3):#for displaying exit
        h.end()
    

# A class for menu items
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# A class for the café
class Cafe:
    def __init__(self):
        self.menu = {}
        self.inventory = {}

    # A method to add a new menu item
    def add_menu_item(self, item, ingredients):
        self.menu[item.name] = {"price": item.price, "ingredients": ingredients}

    # A method to check inventory and update inventory
    def update_inventory(self, ingredient, qty):
        if ingredient in self.inventory:
            self.inventory[ingredient] += qty
        else:
            self.inventory[ingredient] = qty

    # A method to check if the café has enough ingredients to make a menu item
    def can_make(self, item):
        for ingredient, qty in self.menu[item].items():
            if ingredient == "ingredients":
                for ing, q in qty.items():
                    if ing not in self.inventory or self.inventory[ing] < q:
                        return False
        return True

# creating object of Cafe class
cafe = Cafe()

# adding menu items and ingredients
latte = MenuItem("Latte", 3.50)
cafe.add_menu_item(latte, {"milk": 12, "coffee beans": 20})

# updating inventory
cafe.update_inventory("milk", 20)
cafe.update_inventory("coffee beans", 50)

# check if café can make latte
can_make_latte = cafe.can_make("Latte")
print(can_make_latte) # Output: True


print("hello");
A = 3;
B = 4;
C= A+B;
print(C);


IN = int(input("give input"))
A = IN
B = IN
print(A + B)

A = 100
B = 200

'''
a=10
b=20

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

# 7. Integer Division
print(a // b)

# 8. Area of a Rectangle (Length = 5, Breadth = 3)
print("Area of rectangle:", a * b)

# 9. Perimeter of a Square (Side = 6)
print("Perimeter of square:", 4 * 6)

# 10. Celsius to Fahrenheit (C = 25)
print("Fahrenheit:", (25 * 9/5) + 32)


### 🧠 Math Expressions & Logical Thinking

# 11. Average of 3 numbers
print("Average:", (10 + 20 + 30) / 3)

# 12. Simple Interest (P=1000, R=5%, T=2 years)
print("Simple Interest:", (1000 * 5 * 2) / 100)

# 13. Compound Interest (Year 1)
print("Amount after 1 year:", 1000 * (1 + 5/100))

# 14. Square of a number
print("Square of 9:", 9 ** 2)

# 15. Cube of a number
print("Cube of 4:", 4 ** 3)


### 🎉 Fun with Output Formatting

# 16. Print multiple values
print("Sum:", 7 + 8, "Product:", 7 * 8)

# 17. Print equation result
print("5 + 6 =", 5 + 6)

# 18. Print table of 3
print("3 x 1 =", 3 * 1)
print("3 x 2 =", 3 * 2)
print("3 x 3 =", 3 * 3)

# 19. Square root approximation
print("Approx. square root of 49:", 49 ** 0.5)

# 20. Final message with expression
print("Total Score:", 50 + 40 + 60)













































