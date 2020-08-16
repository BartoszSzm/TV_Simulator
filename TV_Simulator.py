#TV simulator

#Program will simulate TV, user can change channel, adjust volume and check channel/volume

#Class
    #TV(object)
    #def __init__
    #@property (volume and channel getters and setters)
    #def channel
    #def volume

#Menu
#print introduction
#create tv object
#While loop, menu
#1. Adjust volume
#2. Change channel
#3. Check actual volume and channel
#4. Turn off TV
#Ending

class TV(object):
    def __init__(self, vol=20, chan=1):
        self.__volume = vol
        self.__channel = chan

    @property
    def volume(self):
        print("Sprawdzam głośność...")
        return self.__volume
    @volume.setter
    def volume(self, value):
        value = int(value)
        if value >= 0 and value < 50:
            print("Zmieniam głośność...")
            self.__volume = value
        else:
            print("Głośność musi być liczbą w zakresie od 0 do 50...")

    @property
    def channel(self):
        print("Sprawdzam kanał...")
        return self.__channel
    @channel.setter
    def channel(self,value):
        value = int(value)
        if value > 0 and value < 100:
            print("Zmieniam kanał...")
            self.__channel = value
        else:
            print("Numer kanału musi być liczbą od 1 do 100")  

#Main
def main():
    #Intro text
    print("Włączyłeś telewizor. Co chcesz zrobić ?")

    #Create object
    TV1 = TV()

    #Menu loop
    rep = None
    vol_change = None
    while rep != "4":
        print("""
                1. Sprawdź aktualną głośność i kanał
                2. Zmień głośność
                3. Zmień kanał
                4. Wyłącz telewizor
              """)
        rep = input("\nCo wybierasz ?\n")
        #Options from menu
        if rep == "1":
            print("Aktualny kanał:",TV1.channel)
            print("Aktualna głośność:",TV1.volume)
        if rep == "2":
            vol_change = input("\nJaką głośność ustawić ? (0-50)")
            TV1.volume = vol_change
        if rep == "3":
            chan_change = input("\nNa jaki kanał zmienić ? (1-100)")
            TV1.channel = chan_change

    print("\nTV wyłączony...")

anwser = "tak"
while anwser not in ("nie"):
    main()
    anwser = input("\nWłączyć telewizor ponownie ? (tak/nie)")

input("\nWciśnij dowolny klawisz, żeby zakończyć...")
    
            


        
    
        


        
        
        

