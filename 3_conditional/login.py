default_username = 'admin'
default_password = '123456'

username = input('username: ')
password = input('password: ')

if username == default_username and password == default_password:
    print("Login Successful")
else:
    print("Login Failed")
