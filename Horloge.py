
import time
def afficher_heure():
  from datetime import datetime
  from time import strftime

  now = datetime.now()
  myobj = datetime.now()

  current_time = now.strftime("%H:%M:%S")
  print("Il est", current_time)
  starttime = time.time()
  while True:
   print(str(datetime.now().hour).zfill(2),":",str(datetime.now().minute).zfill(2), ":",str(datetime.now().second).zfill(2))
   time.sleep(1.0 - ((time.time() - starttime) % 1.0))

def regler_alarme():
 import time
 
second = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
               "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
               "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45",
               "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
minute =  ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
               "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
               "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45",
               "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
hour = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", 
            "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23")
my_alarm = []
if True:
 string_hour = input("Entrez votre heure: ")
if string_hour in hour:
 print("Ok")
 my_alarm.append(string_hour)
 string_minute = input("Entrez votre minute: ")
 if str(string_minute) in minute:
    print("Ok!")
    my_alarm.append(string_minute)
    string_second = input("Entrez votre seconde: ")
    if str(string_second) in second:
     print("Ok")
     my_alarm.append(string_second)
     print("Votre alarme est programmé pour ", str(string_hour.zfill(2)),":",str(string_minute.zfill(2)),":", str(string_second.zfill(2)))
     
    else:
     print("La seconde est incorrecte")
 else:
    print("La minute est incorrecte!")
else:
 print("L'heure est incorrecte ")


 

regler_alarme()

afficher_heure()




 

 