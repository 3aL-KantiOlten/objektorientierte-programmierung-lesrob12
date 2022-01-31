class Schuelerin:
    
    # Konstruktormethode
    def __init__(self, energie):
        self.energie = energie

    def in_schule_gehen(self):
        self.energie -= 5 # self.energie = self.energie - 5

    def kollegin_nerven(self):
        pass

hans = Schuelerin(10)
frida = Schuelerin(15)
lena = Schuelerin(20)

print(f"Hans hat eine Energie von {hans.energie}")
print(f"Frida hat eine Energie von {frida.energie}")

hans.in_schule_gehen()
frida.in_schule_gehen()

print(f"Hans hat eine Energie von {hans.energie}")
print(f"Frida hat eine Energie von {frida.energie}")


