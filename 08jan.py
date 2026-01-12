#Foundation Track
Usernames = []
Platforms = ()
Account_types = set()

username = input("Enter username : ")
platform = input("Enter Platform name (e.g Github , Instagram) : ")
account_type = input("Enter account type (Work / Personal ) : ")


user_platform = { 
   username :  platform
}

Usernames.append(username)
tuple = (platform , account_type)
Account_types.add(account_type)


print("\n\t USER ACCOUNT DATA ")
print("Username : " , username ) 
print("Platform & Acccount Type : " , tuple  )
print("User Mapping : " ,user_platform)
print("Account type : " ,  account_type)

Usernames.append(username)

print(Usernames)