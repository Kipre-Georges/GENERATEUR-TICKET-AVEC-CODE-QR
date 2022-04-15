import os 
import qrcode
from qrcode import ERROR_CORRECT_L


qr = qrcode.QRCode(
    version=20,
    error_correction=ERROR_CORRECT_L,
    box_size=3,
    border=5,
)


nom = str(input("saisissez votre nom : "))
prenom = str(input("saisissez votre prenom : "))
born = int(input("saisissez votre annee de naissance  : "))
mail = str(input("saisissez votre adresse mail : "))
motif=str(input("Quelle est le motif de votre venue ? : "))




renseignement = "Nom : ", nom + "     " + "Prenom : ", prenom + "     " + "Année de naissance : ", str(
born) + "     " + "Adresse mail : ", mail+"     "+"Motif : ",motif
renseignement="".join(renseignement)
print(renseignement)


qr.add_data(renseignement)
qr.make(fit=True)
img = qr.make_image(fill_color="Black", back_color="white")
img.save('qrcode.png')
