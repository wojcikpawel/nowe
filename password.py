password = "0"
while (password != "1234"):
    password = raw_input("Podaj haslo: ")
    if (password == "1234"):
        print("Haslo poprawne")
    else :
        print("Haslo niepoprawne")
