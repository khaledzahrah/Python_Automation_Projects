import re
def check_password(pwd):
    rules={
    'uppercase':re.compile(r'[A-Z]'),
    'lowercase':re.compile(r'[a-z]'),
    'numbers':re.compile(r'[0-9]')
    }
    if len(pwd)<8:
        print(" - At least 8 characters.")
        return False
    for name, pattern in rules.items():
        if not pattern.search(pwd):
            print(f'the password is false check out:{name}')
            return False
    print('the password is true')
    return True
#example.
check_password("bcdsgf345")