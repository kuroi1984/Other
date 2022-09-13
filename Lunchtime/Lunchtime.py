#number=input ("Что возвести в степень 3?:")
#print (number + "^3="+str(int(number)**3))

import time
hour = time.strftime("%H")
times = int(hour)
#print (str(times))
if times >= 8 and times < 11:
    print ("До обеда еще далеко, держись")
elif times >=11 and times <12:
    print ("Ура!! Скоро обед")
elif times >= 12 and times <13:
    print ("Пора на обед")
elif times >= 13 and times <14:
    print ("Обед только что прошел, работай")
elif times >=14 and times<17:
    print ("Скоро домой")
else:
    print ("Что ты делаешь на работе? Беги домой")
    
#print ( "Сейчас " + hour + " часов" )
