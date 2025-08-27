from getpass import getpass
username = 'Franzgeraldroque2'
pwd = 'franzroque17'

uname = input('input username -->' )
p_input = getpass('enter password --> ')

#valid username or password
if username == uname and pwd == p_input :
	print("Access granted")
else:
	print("Access denied")