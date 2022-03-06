# 3 tipuri de dispozitive
# 1. telefon -(capabilitati: face poze, poti suna, navigare online, GPS, video
# 2. smart_tv - (capabilitati: navigare online, video, cablu_TV)
# 3. smart_watch - (capabilitati: GPS, poti suna, numara pasi, healty monitoring)

# I.Definirea capabilitatile prin clase
class Gps:
    def get_position(self):
        print("Getting the current position")


class Video:
    def run_viode(self):
        print("Running current video")


class Calling:
    def calling_person(self):
        print("Call me maybe")

    def answer_call(self):
        print("Wrong number")


class Health:
    def heart_rate(self, number_beats):
        try:                                    # prevenim erori si permite continuarea rularii fara erori
            if number_beats >= 220:
                print("You are having a heart-attack")
            else:
                print("you are doing great!")
        except:
            print("Atentie! Numar invalid")


    def num_pasi(self, tenthousand_perday):
        if tenthousand_perday >= 10000:
            print("Congrats")


class Cablu:
    def setare_canal(self):
        print("Canalul dorit este setat")


class NavigareOnline:
    def open_chrome(self):
        print("search google")


class Foto:
    def take_picture(self):
        print("the picture was taken")


# II. Definirea claselor pt cele 3 dispozitive
class Telefon(Gps, Video, Foto, Calling, NavigareOnline):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def take_picture(self):
        print("The HD photo was taken")


class SmartTV(Video, NavigareOnline, Cablu):
    def __init__(self, brand, rezolutie):
        self.brand = brand
        self.rezolutie = rezolutie

    def setare_canal(self):
        print("Fara semnal - 404")


class SmartWatch(Gps, Calling, Health):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def calling_person(self):
        print("The person is not reachable. Try again later")


# III. Crearea obiectelor si invocarea acestora

if __name__ == "__main__":
    # t = Telefon("iPhone", "12pro")
    tv = SmartTV("samsung", "24x720")
    ceas = SmartWatch("OPPO", "x1")

# t.take_picture()
# t.calling_person()
# t.answer_call()
    print("=================")
    tv.open_chrome()
    tv.setare_canal()
    print("=================")
    ceas.heart_rate(50)
    ceas.heart_rate('abc')

    ceas.num_pasi(11000)
    ceas.calling_person()