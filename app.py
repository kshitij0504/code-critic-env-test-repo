def login(user, password):
    if password == user.password:
        print("Login success")
        
        
    print("Welcome, " + user.name)
    
    print(user.name.upper())