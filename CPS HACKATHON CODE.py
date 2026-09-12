buses = {1: {'startpoint': 'Chennai', 'endpoint': 'Madurai', 'fare': 670, 'totalseats': 20, 'seatsavailable': 6, 'category': 'AC'},
         2: {'startpoint': 'Bangalore', 'endpoint': 'Mysore', 'fare': 1220, 'totalseats': 20, 'seatsavailable': 7, 'category': 'AC'},
         3: {'startpoint': 'Chennai', 'endpoint': 'Madurai', 'fare': 1040, 'totalseats': 20, 'seatsavailable': 0, 'category': 'Non-AC'},
         4: {'startpoint': 'Bangalore', 'endpoint': 'Mysore', 'fare': 1400, 'totalseats': 20, 'seatsavailable': 4, 'category': 'Non-AC'},
         5: {'startpoint': 'Vijayawada', 'endpoint': 'Hyderabad', 'fare': 1001, 'totalseats': 20, 'seatsavailable': 3, 'category': 'AC'},
         6: {'startpoint': 'Chennai', 'endpoint': 'Bangalore', 'fare': 420, 'totalseats': 20, 'seatsavailable': 7, 'category': 'AC'},
         7: {'startpoint': 'Vijayawada', 'endpoint': 'Hyderabad', 'fare': 1000, 'totalseats': 20, 'seatsavailable': 0, 'category': 'Non-AC'},
         8: {'startpoint': 'Chennai', 'endpoint': 'Bangalore', 'fare': 1500, 'totalseats': 20, 'seatsavailable': 8, 'category': 'Non-AC'},
         9: {'startpoint': 'Bangalore', 'endpoint': 'Mangalore', 'fare': 1000, 'totalseats': 20, 'seatsavailable': 20, 'category': 'Non-AC'},
         10: {'startpoint': 'Coimbatore', 'endpoint': 'Ooty', 'fare': 999, 'totalseats': 20, 'seatsavailable': 19, 'category': 'AC'}}

def account():
    global accounts
    accounts = {}
    found = True
    i = 5
    while found == True and i > 0:
        d = {}
        email = input("Enter USER ID: ")
        phone_number = input("Enter 10 digit phone number: ")
        if len(phone_number) == 10:
            phone_number = int(phone_number)
        else:
            print("INVALID PHONE NUMBER.")
            found = False
            break
        password = input("Enter password: ")
        d['email'] = email
        d['phone number'] = phone_number
        d['password'] = password
        d['status'] = 'active'
        if email == 'vaishnavisgood@gmail.com':
            d['status'] = 'blocked'
        accounts[i] = d
        i -= 1
    if found == True:
        login()


def login():
    name = input("Enter username: ")
    found = False
    for i in accounts.values():
        if i['email'] == name:
            found = True
    if found == False:
        print("User Not Found.")
    else:
        pass_word = input("Enter password: ")
        for i in accounts.values():
            if i['email'] == name:
                if pass_word != i['password']:
                    print("Incorrect Password.")
                else:
                    if i['status'] == 'blocked':
                        print("Account Blocked, Contact Support.")
                    else:
                        print("Login Successful.")
                        start = input("Enter start location: ")
                        end = input("Enter end location: ")
                        for j in buses.values():
                            if start == j['startpoint']:
                                if end == j['endpoint']:
                                    if j['seatsavailable'] != 0:
                                        print(j)
                                        if j['category'] == 'AC':
                                            if j['seatsavailable'] != 0:
                                                print("Number of seats left= ", j['seatsavailable'])
                                        elif j['category'] == 'Non-AC':
                                            print("Number of seats left= ", j['seatsavailable']-1)
                                        a = [key for key,val in buses.items() if val == j]
                                        print('Booking receipt:-')
                                        print("Name: ",name)
                                        print("Bus number: ",a)
                                        print("Startpoint: ",j['startpoint'])
                                        print("Endpoint: ",j['endpoint'])
                                        print("Category: ",j['category'])
                                        print("Fare: ",j['fare'])
                                        print("Seats available after booking: ",j['seatsavailable']-1)
                                        print("Booking confirmed!!")
                                        break
                        else:
                            print("No available buses for this route")
                            break

account()