#Email id validation
import re

def check_valid_email(mail):

    if len(mail) > 254:
        return False

    if mail.count('@') != 1:
        return False

    local, domain = mail.split('@')
    if len(local) > 64 or len(local) == 0:
        return False

    if not re.match(r'^[A-Za-z0-9._%+-]+$', local):
        return False

    if local.startswith('.') or local.endswith('.') or '..' in local:
        return False

    if len(domain) == 0:
        return False

    if domain.count('.') != 1:
        return False

    labels = domain.split('.')
    for label in labels:
        if not re.match(r'^[A-Za-z0-9._%+-]+$', label):
            return False

        if label.startswith('-') or label.endswith('-'):
            return False
    return True

email = input("Enter email address: ")

if check_valid_email(email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")