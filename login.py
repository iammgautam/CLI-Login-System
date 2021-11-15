# Login System Project
import bcrypt
# create a file to store thed username & password
# with open('database.txt','w') as db:
#     pass

# register function
def register():
    username = input("Username:")
    password = input("Password:")
    password1 = input("Confirm Password:")

    db = open('database.txt', 'r')
    user = []
    passwd = []
    for i in db:
        a,b = i.split('--->')
        b = b.strip()
        user.append(a)
        passwd.append(b)
    data = dict(zip(user, passwd))
    print(data)
    if password != password1:
        print("Password Don't match,restart:")
        register()
    else:
        if len(password) < 6:
            print("Password is too short, restart:")
            register()
        elif username in user:
            print("Username already exist, restart:")
            register()
        else:
            if password == password1:
                password = password.encode('utf-8')
                password = bcrypt.hashpw(password, bcrypt.gensalt())
            with open('database.txt', 'a') as db:
                db.write(username+'--->'+str(password)+'\n')
                print(data)
    db.close()

# login access function
def login():
    username = input('Enter your Username:')
    password = input('Enter your Password:')

    if not len(username or password) < 1:
        user = []
        passwd = []
        db = open('database.txt','r')
        for i in db:
            a,b = i.split('--->')
            b = b.strip()
            user.append(a)
            passwd.append(b)
        data = dict(zip(user,passwd))
        
        try:
            if data[username]:
                hashed_passwd = data[username].strip('b')
                hashed_passwd = hashed_passwd.replace("'","")
                hashed_passwd = hashed_passwd.encode('utf-8')
                try:
                    if bcrypt.checkpw(password.encode(),hashed_passwd):
                        print('Login Accesed')
                        print(F'Hi {username}')
                    # else:
                    #     print("Incorrect Password")
                    #     login()
                except:
                    print("Incorrect Password")
                    login()
            # else:
            #     print('This username & Password doesn\'t exist')
            #     exit()
        except:
            print('Login error')
    else:
        print("Enter a value")

# central function
def home(option=None):
    option = input('Login|Signup: ')
    if option == 'Login':
        login()
    elif option == 'Signup':
        register()
    else:
        print('Please Enter the correct option')

home()