qtdE=(int(input("How many employeers? ")))
if(qtdE<1 or qtdE>100):
    while True:
        print("The quantity of employeers need to be bigger than 1 and minor than 100")
        qtdE=(int(input("How many employeers? ")))
        if not (qtdE<1 or qtdE>100):
            break
        
for i in range(qtdE):
    valueHour=(float(input("Enter with the value per hour: ")))
    if(valueHour<2 or valueHour>100):
        while True:
            print("Error! The value per hour needs to be bigger than 2 and minor than 100")
            valueHour=(float(input("Enter with the value per hour: ")))
            if not (valueHour<2 or valueHour>100):
                break

    qtdDays=(int(input("Enter with the days quantity: ")))
    if(qtdDays<1 or qtdDays>31):
         while True:
            print("Error! The quantity of days needs to be bigger than 1 and minor than 31")
            qtdDays=(int(input("Enter with the days quantity: ")))
            if not (qtdDays<1 or qtdDays>31):
                break

    perc=(float(input("Enter with the readjust percentage in the wage: ")))
    if(perc<10 or perc>50):
        while True:
            print("Error! The percentage of readjust needs to be bigger than 10 and minor than 50")
            perc=(float(input("Enter with the readjust percentage in the wage: ")))
            if not(perc<10 or perc>50):
                break

    valueHour=valueHour+valueHour*(perc/100)

    wage=valueHour*qtdDays

    print("Your wage is: ", wage)





