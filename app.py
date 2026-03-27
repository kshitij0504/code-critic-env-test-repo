def login(user, password):
    if password == user.password:
        print("Login success")
        
        
    print("Welcome, " + user.name)
    print("Your name in uppercase is:")
    
    print(user.name.upper())