# correct userid and password

correct_id = "admin"
correct_password = "1234"

for attempt in range(1, 4):
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")

    if user_id == correct_id and password == correct_password:
        print("Login Successful ")
        
       