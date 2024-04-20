from random import randint


class cryptage:
    
    def __init__(self):
        self.patern = {"a":["PLR","R9P","L0D","M4S"],"b":["ZIA","KI1","F3R","PII"],"c":["FG6","KD6","MDF","PIT"],
                       "d":["9PF","UIO","DE4","PP4"],"e":["BE9","MD4","45T","TI4"],"f":["SDG","PO9","P3E","14V"],
                       "g":["P7E","CI9","CVO","MAL"],"h":["K23","XC4","XQC","V53"],"i":["0DF","QSD","PSD","M4B"],
                       "j":["08S","68Q","PZA","W4U"],"k":["Q3D","PSP","S90","0GX"],"l":["AER","AMG","CTD","WN3"],
                       "m":["MPL","D8F","QS0","PD0"],"n":["S4Y","TKT","BRO","P4F"],"o":["F6G","W3S","09D","D9F"],
                       "p":["12F","SDR","ERT","DD4"],"q":["POI","CSF","MFT","0M4"],"r":["CS2","QSP","E45","PPA"],
                       "s":["MFI","G9E","WRF","C24"],"t":["QS9","DSG","98G","ALO"],"u":["SSG","SOG","QSR","C12"],
                       "v":["8DF","WGH","QWS","OLA"],"w":["WRG","Q5G","S45","N4E"],"x":["3GJ","CFT","0DP","ALK"],
                       "y":["POG","G9D","QRG","I3F"],"z":["P9F","PQD","WND","I2C"],"0":["DPZ","Y7F","SNK","K4F"],
                       "1":["FPD","PIU","D8A","FOR"],"2":["PDT","CE1","PD4","JDT"],"3":["LOQ","PI2","DBZ","HRT"],
                       "4":["9QS","MLW","9QE","JET"],"5":["FGH","7DX","FDT","OKE"],"6":["SQD","CEO","09Q","83F"],
                       "7":["PA4","CBO","NAR","B3W"],"8":["PER","QS4","A45","BBC"],"9":["UW8","TRZ","LOG","QS5"],
                       "":["EXP","AF0","KA9","SD9"]
                    }

    def encrypt_data(self,fileToRead,fileToWrite):
        crypted_txt = ""
        with open(fileToRead,'r') as f:
            data = f.read()
        
        for words in data: #parcour des mots dans le fichier txt
            caract = ''.join(words.split()) #sépration de toutes les lettres 
            for letter in self.patern:
                if caract == letter: #si caractère minuscule dans self.patern
                    for i in self.patern[caract][randint(0,1)]: #choix entre le paterne 1 et 2 
                        if randint(0,1): #change la lettre en maj ou min au hasard
                           crypted_txt += i.lower() 
                        else:
                            crypted_txt += i 
                        
                elif caract == letter.upper(): #si lettre maj
                    for i in self.patern[caract.lower()][randint(2,3)]:
                        if randint(0,1):
                            crypted_txt += i.lower()
                        else:
                            crypted_txt += i
        with open(fileToWrite,'w') as f:
            f.write(crypted_txt)

    def decrypt_data(self,fileToRead,fileToWrite):
        decrypted_txt = ""
        with open(fileToRead,'r') as f:
            data = f.read()
        readed_data = ''.join(data)
        count = 0
        while count != len(readed_data): #parcour la chaine 3 éléments à la fois 
            patern = ""
            for index in range(3): 
                patern += readed_data[count+index].upper() #séparation des patern de 3
                for i in self.patern: #pour chaque éléments de self.patern
                    for j in self.patern[i]: # pour chaques élément des tables de self.patern
                        if j == patern: #si patern se trouve dans la table de self.patern en fonction de i
                            if j in self.patern[""]: #si le patern détecter est l'espace 
                                decrypted_txt += " "
                            elif self.patern[i].index(patern) > 1: #si l'index du patern est 2 ou 3, lettre est maj
                                decrypted_txt += i.upper()
                            elif self.patern[i].index(patern) < 2: #sinon est min
                                decrypted_txt += i
            count +=3
        
        with open(fileToWrite,'w') as f:
            f.write(decrypted_txt)

            



txt = cryptage()
txt.encrypt_data("normal_text.txt","scrypted_text.txt")
txt.decrypt_data("scrypted_text.txt","scryptToText.txt")