'''
Build an email slicer : create a function that takes an email as input and retrieve the username and domain of the email
'''

def email_slicer(email):
    username, domain = email.split('@')

    return f"Username: {username} , Domain: {domain}"

email = input("Enter an email ==> ", )
print(email_slicer(email))