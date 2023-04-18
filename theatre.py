normal_seat = 50
price_normal_seat = 100
recliner_seat = 30
print_recliner_seat = 200
total = 0
while True:
    print("WELCOME TO NATRAJ CINEMA HALL JHANSI (UTTAR PRADESH)")
    print("PHONE NO-18004007000")
    print("EMAIL ID - natramjhansi1452@gmail.com")
    print()

    print("Hello Sir/Mam.....")
    print()
    print("total normal seat in theater=50")
    print("total recliner seat in theater=30")
    print("normal seat price=100")
    print("recliner seat price=200")
    print()
    user = input("Enter your name:- ")
    mob_no = input("Enter your mobile no:- ")
    seat_types = input("What type of seat do you want (normal, recliner)? ")

    if seat_types == "normal":
        confirm_seat1 = int(input("How many seats do you want: "))
        if confirm_seat1 <= normal_seat:
            total += confirm_seat1 * price_normal_seat
            normal_seat -= confirm_seat1
            print("Normal seats available: ", normal_seat)
        else:
            print("Sorry, there are not enough normal seats available.")
    elif seat_types == "recliner":
        confirm_seat2 = int(input("How many seats do you want: "))
        if confirm_seat2 <= recliner_seat:
            total += confirm_seat2 * print_recliner_seat
            recliner_seat -= confirm_seat2
            print("Recliner seats available: ", recliner_seat)
        else:
            print("Sorry, there are not enough recliner seats available.")
    else:
        print("You entered an invalid seat type.")

    print("-"*50)
    print("WELCOME TO NATRAJ CINEMA (JHANSI)")
    print("PHONE NO: 18001251522")
    print("EMAIL ID - natraj154@gmail.com")
    print("Customer name:- ", user)
    print("Mobile no:- ", mob_no)
    print("Your seat type:- ", seat_types)
    print("Total bill Rupee:- ", total)
    print("THANK YOU FOR VISITING....")
    print("-" * 50)
    repeat=input("next coustmer(yes/no)")
    if repeat=="no":
        break