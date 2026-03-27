def login(user, password):
    if password == user.password:
        print("Login success")
    
    print(user.name.upper())