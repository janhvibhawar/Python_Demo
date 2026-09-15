# password match
correct_pass = "123"
not_found = True

while not_found:
    passw = input("Enter password:")
    if passw == correct_pass:
        not_found = False

print("Password Matched")

