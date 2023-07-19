# Welcome to  district library
#       Noida (UP)
# email- districtlibraray007@gmail.com
# Phone no- 1800 4440 2000

Books={"maths":20, "science":20, "socialscience":20}
while True:
    Username=input("Username:-")
    login_id="rohit","jitendra007","vikas009"
    if Username in login_id:
        print("username_verified")
    else:
        print("invalid username")
    Password=input("Password:-" )
    pas="batch119"
    if Password in pas:
            while True:
                print("Welcome to the Library", Username)
                print("")
                print(
"""Press 1 for issuing
Press 2 for return or add more books
Press 3 for balance & return to home page""")

                C = int(input("Enter Your Choice:"))
                if C == 1:
                    print(Books)
                    d = input("Enter Your Book Choice:-").lower()
                    if d in Books.keys():
                        n = int(input("Enter quantity of Books:-"))
                        if n <= Books[d]:
                            Books[d] -= n
                        else:
                            print("We only have following balance of", d, Books[d])
                    else:
                        print(d, "Book is currently un-available")
                elif C == 2:
                    a = input("Which book you want to return:-")
                    b = int(input("Enter quantity of Books:-"))
                    if a in Books.keys():
                        Books[a] += b
                    else:
                        Books[a] = b
                    print(Books)

                elif C == 3:
                    print("-"*75)
                    print("Welcome to  district library")
                    print("Noida (U P)")
                    print("email- districtlibraray007@gmail.com")
                    print("Phone no- 1800 4440 2000")
                    print("username:-",Username)
                    print("available books stock:-",Books)
                    print("Have a nice day,.......", Username)
                    print("-"*75)
                    break
    else:
        print("Invalid Password")
