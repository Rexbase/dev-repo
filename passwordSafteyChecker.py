import random, time

password = input("Enter Password: ")

characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
trypassword = ""
trypasswordTries = 0
timeStart = time.time()

while True:
    trypasswordTries += 1

    for character in range(len(password)):
        trypassword = trypassword + characters[random.randint(0, 9)]
    
    timeStop = time.time()
    timeTotal = round(timeStop - timeStart, 1)

    if trypassword == password:
        print(f"{trypasswordTries} | Valid | {trypassword} ({timeTotal}s)")
        break
    else:
        print(f"{trypasswordTries} | Invalid | {trypassword}")

    trypassword = ""