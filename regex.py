import re

def ler_arqw():
    try:
        with open("Falso_log.txt", "r") as continua:
            slow= continua.read()

            return slow
    
    except Exception as e:
        print(f"Houve um erro. {e}")

    except FileNotFoundError:
        print("Não achei.")

wow= ler_arqw()

def Regex(olimpia):
    matriz= {}
    
    love= r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) \- \- \[(\d{2}\/[a-zA-Z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} \-\d{4})\] \"(.*?)\" (\d{3}) (\d{2,4})"

    não= re.findall(love, olimpia)

    if não: 
        for i in não:

            if i[0] not in matriz:
                matriz[i[0]] = {"ENDPOINT":  i[2], "STATUS": i[3], "CONTAGEM": 0}

            else:
                matriz[i[0]]["CONTAGEM"] += 1

                matriz[i[0]]["STATUS"] = i[3]

                if i[3] == "404" or matriz[i[0]]["CONTAGEM"] >= 3:
                    matriz[i[0]]["CLASSIFICAÇÃO"] = "PERIGOSO"

                else:
                    matriz[i[0]]["CLASSIFICAÇÃO"] = "TRANQUILO"

        print(matriz)

    else:
        print("errado")

chamei= Regex(wow)