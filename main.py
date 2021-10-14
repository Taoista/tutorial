import random

def carton():
    print("==========INICIANDO==========")
    option_carton = input("Selecciona el carton Selecciona 1 - para un carto aleatoreo o 2- para seleccionar tus numero()son 15: \n")
    carton = list()
    limite_1 = 1
    limite_2 = 90
    iniciando_software = False
    if int(option_carton) == 1:
        print(f"seleccionaste la option {option_carton}, debes elegir tus numeros entre 1 y 90")
        while iniciando_software == False:
            if len(carton) == 15:
                print("el carton fue seleccionado con exito")
                print(carton)
                print(len(carton))
                iniciando_software = True
            else:
                numero_seleccionado = int(input("ingresa un numero en entre 1 y 90, no se puede repetir: \n"))
                if numero_seleccionado < limite_1:
                    print(f"debe seleccionar un numero mayor a {limite_1} minimo seleccionado")
                elif numero_seleccionado > limite_2:
                    print(f"debe seleccionar un numero meno a {limite_2}  seleccionado")
                else:
                    if len(carton) <=0:
                        print('primer numero')
                        carton.append(numero_seleccionado)
                    else:
                        encontrado = False
                        cont = 0
                        while len(carton) > cont:
                            if carton[cont] == numero_seleccionado:
                                encontrado = True
                            cont += 1
                        if encontrado == False:
                            carton.append(numero_seleccionado)
                        else:
                            print("el numero ya fue agregado con anterioridad")

    else:
        print("Seleccionaste la opcion 2....generando carton...")
        while len(carton) < 15:
            numero = random.randint(limite_1,limite_2)
            encontrado = False
            for i in carton:
                if i == numero:
                    encontrado = True
            if encontrado == False:
                carton.append(numero)        

    return carton


def tombola():
    print("==============================================")
    print("===============iniciando la tombola============")
    print("==============================================")
    nueva_tombola = list()
    carton_completo = list()
    veces = list()
    estado_carton = True
    for i in range(1, 91):
        nueva_tombola.append(i)

    nuevo_carton = carton()
    print("nuevo carton--------")
    print(nuevo_carton)
    print("--------------------")
    # print(len(nueva_tombola))
    while estado_carton == True:
        
        for i in nueva_tombola:
            
            seleccion = random.choice(nueva_tombola)
            nueva_tombola.remove(seleccion)
            # 
            # este es el contador que cree, creo q sirve ya que agregue los numero que fueron seleccionados
            # a un array, puede ser un contador como tu quieras, pero no se dode o como creee el profesor 
            # donde debe ir el contador
            # 
            # cambia los print por algo que te acomode
            # 
            veces.append(seleccion)

            # print(f"seleccion de la tombola..... es el numero {seleccion} ")
            
            for x in nuevo_carton:
                if x == seleccion:
                    nuevo_carton.remove(seleccion)
                    carton_completo.append(seleccion)
                    print(f"Bola encontrada....{seleccion}")
                if len(nuevo_carton) == 0:
                    print("CARTON LLENO CONCHETUMADRE")
                    print(carton_completo)
                    estado_carton = False
                
    return len(veces)  



def premio(cantidad):
    premio = 1000000
    print("++++++++++++-- TERMINO EL JUEGO -++++++++++++++++")
    if cantidad == 15:
        print(f"Total cantidad de intentos {cantidad} tu premios es de {premio}")
    elif 16 >= cantidad <= 30:
        print(f"Total cantidad de intentos {cantidad} tu premios es de { premio * 0.5 }")
    elif 31 >= cantidad <= 60:
        print(f"Total cantidad de intentos {cantidad} tu premios es de { premio * 0.25 }")
    elif 61 >= cantidad <= 75:
        print(f"Total cantidad de intentos {cantidad} tu premios es de { premio * 0.1 }")
    elif 76 >= cantidad:
        print(f"Total cantidad de intentos {cantidad} tu premios es de { premio * 0.05 }")
    else:
        print(f" eri penca fueron  {cantidad} tintentos tu premio es un  8===D ")


def main():
    # nuevo_carton = carton()
    cantidad = tombola()
    premio(cantidad)


if __name__ == '__main__':
    main()
    # dos()