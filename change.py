def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(float(expense))
    print("Dinero recibido")
    print(int(money))
    
    print("Vuelto")

    print("Pesos:")
    print(int(money-expense))
    print("Centavos:")
    print(int((round(expense)-expense)*100))
