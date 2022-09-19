import os
import time

print("This is a ID Card Maker from Maris. It makes a Vcard in the TXT Format! Have fun!")
os.system("pause")

forname = input("first name: ")
surname = input("surname: ")
date_of_birth = input("date of birth (DD/MM/YYYY): ")
nationality = input("nationality: ")
gender = input("gender: ")
size = input("size (X,XX): ")
body_shape = input("body shape (description): ")
email = input("email: ")
phone_number = input("phone number: ")
adress = input("Adress: ")
other_information = input("Other Information: ")

#Thx an https://stackoverflow.com/questions/48959098/how-to-create-a-new-text-file-using-python
f = open(f"{forname}_{surname}.txt","w")   # 'r' for reading and 'w' for writing
f.write(f"Data from {forname} {surname}\n")
f.write("--------------------------------------------------------------------------------\n")
f.write(f"Forname: {forname}\n")
f.write(f"Surname: {surname}\n")
f.write(f"Date of Birth: {date_of_birth}\n")
f.write(f"Nationality: {nationality}\n")
f.write(f"Gender: {gender}\n")
f.write(f"Size: {size}m\n")
f.write(f"Body shape: {body_shape}\n")
f.write(f"Email: {email}\n")
f.write(f"Phone Number: {phone_number}\n")
f.write(f"Adress: {adress}\n")
f.write(f"Other Information: {other_information}\n")
f.close()

print("The File is now finished, bye!")

time.sleep(5)













