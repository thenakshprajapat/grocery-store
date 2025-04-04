import random
item = input("Enter item you are looking for : ")
item_list = ['macbook','phone','surface go','boat headphones','pixelwatch']
item_dict = {'macbook':100000 , 'phone': 52000 , 'surface go' : 120000 , 'boat headphones' : 2000 , 'pixelwatch' : 30000}
luck_disc = random.randint(1,20)
rand_disc = random.randint(0,100)
luck_disc1 = luck_disc/100
rand_disc1 = rand_disc/100 
if item.lower() in item_list:
    print("Item Found")
    print("Price of ",item,"is ",item_dict[item.lower()])
    print("Do you want to play a game for discount?")
    ch = input("Type y or n ! : ")
    if ch.lower() == "y":
        print("There are two type of discounts \nOne is Luck\nAnother is Random")
        ch1 = input("Enter your choice [luck or random]: ")
        if ch1.lower() == "luck":
            print("you get a discount of : ",luck_disc,"%")
            print("Your total value is now : ",item_dict[item.lower()])
            print("Your disc = ",item_dict[item.lower()]*luck_disc1)
            print("Your cart value is : ",item_dict[item.lower()]-item_dict[item.lower()]*luck_disc1)
        elif ch1.lower() == "random":
            print("You will be charged 1000 rupees for this")
            ch2 = input("Type y or n : ")
            if ch2.lower() == "y":
                print("You get a discount of : ",rand_disc,"%")
                print("Your total value is now : ",item_dict[item.lower()])
                print("Charge for random discount opt : 1000")
                print("Your disc = ",item_dict[item.lower()]*rand_disc1)
                print("Your cart value is : ",item_dict[item.lower()]-item_dict[item.lower()]*rand_disc1 + 1000)
            elif ch2.lower() == "n":
                print("Pay original price i.e : ",item_dict[item.lower()])
                print("Thanks for shopping with us!")
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
    elif ch.lower() == 'n':
        print("Pay original price i.e : ",item_dict[item.lower()])
        print("Thanks for shopping with us")
    else:
        print("Invalid input")
else:
    print("Item not found\nSorry for the inconvinience\nStock will be back soon")