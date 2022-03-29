import urllib.parse
import requests
import os
#42qsqCB5.G-MW8b
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "ykuqqndSwpFXtEmSrL6nzuB71luq02Ar"

while True:
    orig = input("Origen")
    if orig == "s":
        break

    dest = input("Destino: ")
    if orig == "s":
        break

    clear = lambda: os.system('cls')
    clear()

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + url)

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("Estatus de la API:" + str(json_status) + "= 0 Se encontro la ruta.\n")
        print("Instrucciones de: " +(orig) + " a: " +(dest))
        print("Duración aproximada: " +str(json_data["route"]["formattedTime"]))
        print("Kilometros aproximados: " +str("{:2f}".format((json_data["route"]["distance"])*1.61)))
        print("Litros aproximados: " +str("{:2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=========== INSTRUCCIONES DE RUTA ===========")
        contador = 1
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print("Paso No." +str(contador)+ ":" + (each["narrative"]))
            #+"(" + str("{:2f}".format((each["distance"])*1.61) + "Km")))
            contador = contador + 1
        print("=========== FIN DE LA RUTA ===========")

    elif json_status == 402:
        print ("Oye flaco, habla serio no hay esa ruta")
    else:
        print("Ponte 11 flaco")
