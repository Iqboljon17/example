print("exercise one")
usernames = {
    "iqboljon": "iqboljon1803",
    "shavkat": "shava",
    "mary": "maryjane",
    "thanos": "thanos@123",
    "Tomholland": "123456789",
}

validPasswords = {}
for username, password in usernames.items(): 
    if password.isalnum() and len(password) >= 6: 
        validPasswords[username] = password
    else :
        print(password, "invalid Passwords")
print(validPasswords, "these are valid passwords")



print("exercise two")
logs = "INFO: Server started,ERROR: Login failed,INFO: User logged in,WARNING: Low memory,ERROR: File not found,INFO: Data saved,WARNING: Slow network"

messages = logs.split(",")

counts = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

for text in messages:
    if text.startswith("INFO"):
        counts["INFO"] += 1
    elif text.startswith("WARNING"):
        counts["WARNING"] += 1
    elif text.startswith("ERROR"):
        counts["ERROR"] += 1

print(counts)
        
print("exercise three")
students = [
    "  JOHN SMITH  ",
    "MARY JANE",
    "  ali karimov",
    "Peter Parker  ",
    "  TOM HOLLAND ",
    "Emma Watson",
]

emails = []

for names in students: 
    name = names.strip()
    name = name.replace(" ", ".")
    email = name + "@university.edu"
    emails.append(email)

print(emails)

print("exercise four")

products = [
    "ELEC-204-599.99",
    "CLOTH-105-49.99",
    "FOOD-301-12.50",
    "BOOK-412-25.00",
    "PHONE-520-799.99",
    "SPORT-210-89.90"
]
for product in products:
    item = product.split("-")
    print("Category" , item[0])
    print("ID" , item[1])
    print("Price" , item[2])

