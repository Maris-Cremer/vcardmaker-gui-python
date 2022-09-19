import os
import tkinter as tk
import time
from turtle import position

print("Vcard Maker TXT v1 (CC by Maris Cremer)")

def generate_file():
 forname = entry_forname.get()
 surname = entry_surname.get()
 date_of_birth = entry_dob.get()
 gender = entry_gender.get()
 size = entry_size.get()
 body_shape = entry_body_shape.get()
 email = entry_email.get()
 phone_number = entry_phone_number.get()
 adress = entry_adress.get()
 nationality = entry_nationality.get()
 other_information = entry_other_information.get()

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
 f.write(f"\n")
 f.write(f"CC by Maris Cremer")
 f.close()
 time.sleep(1)
 label_sucess = tk.Label(text="File is created!", background="green")
 label_sucess.grid(row=25, column=0)

window = tk.Tk()

window.title("Vcard Maker TXT v1")
window.resizable(False, False)
#window.iconbitmap(r'/idcard.ico/')

label = tk.Label(font=15,text="Vcard Maker TXT", anchor="center", width=35, height=2)
label.grid(row=1,column=0)

label_forname= tk.Label(font=5, text="Forname:", anchor="center")
label_forname.grid(row=2,column=0)
entry_forname = tk.Entry()
entry_forname.grid(row=3,column=0)

label_surname= tk.Label(font=5, text="Surname:", anchor="center")
label_surname.grid(row=4,column=0)
entry_surname = tk.Entry()
entry_surname.grid(row=5,column=0)

label_dob= tk.Label(font=5, text="Date of birth:", anchor="center")
label_dob.grid(row=6,column=0)
entry_dob = tk.Entry()
entry_dob.grid(row=7,column=0)

label_gender= tk.Label(font=5, text="Gender:", anchor="center")
label_gender.grid(row=8,column=0)
entry_gender = tk.Entry()
entry_gender.grid(row=9,column=0)

label_size= tk.Label(font=5, text="Size:", anchor="center")
label_size.grid(row=10,column=0)
entry_size = tk.Entry()
entry_size.grid(row=11,column=0)

label_body_shape= tk.Label(font=5, text="Body Shape:", anchor="center")
label_body_shape.grid(row=12,column=0)
entry_body_shape = tk.Entry()
entry_body_shape.grid(row=13,column=0)

label_phone_number= tk.Label(font=5, text="Phone Number:", anchor="center")
label_phone_number.grid(row=14,column=0)
entry_phone_number = tk.Entry()
entry_phone_number.grid(row=15,column=0)

label_email= tk.Label(font=5, text="Email:", anchor="center")
label_email.grid(row=16,column=0)
entry_email = tk.Entry()
entry_email.grid(row=17,column=0)

label_adress= tk.Label(font=5, text="Adress:", anchor="center")
label_adress.grid(row=18,column=0)
entry_adress = tk.Entry()
entry_adress.grid(row=19,column=0)

label_nationality= tk.Label(font=5, text="Nationality:", anchor="center")
label_nationality.grid(row=20,column=0)
entry_nationality = tk.Entry()
entry_nationality.grid(row=21,column=0)

label_other_information= tk.Label(font=5, text="Other Information:", anchor="center")
label_other_information.grid(row=22,column=0)
entry_other_information = tk.Entry()
entry_other_information.grid(row=23,column=0)

button = tk.Button(text="Create File", command= generate_file)
button.grid(row=24, column=0)

window.mainloop()

