def login(user, password):
    """
    Prints login outcome and welcome messages for a user, including their name in uppercase.
    
    Parameters:
        user: An object with `password` and `name` attributes; `password` is compared to the supplied `password`, and `name` is used for welcome messages.
        password: The credential value to compare against `user.password`.
    
    Description:
        If `password` equals `user.password`, prints "Login success". Always prints a welcome line, the literal "Your name in uppercase is:", and the user's name converted to uppercase.
    """
    if password == user.password:
        print("Login success")
        
        
    print("Welcome, " + user.name)
    print("Your name in uppercase is:")
    
    print(user.name.upper())