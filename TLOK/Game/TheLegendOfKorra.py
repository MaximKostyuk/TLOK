import KorraClass 
import Locations
import Scene
#Проверка на возможность нахождения на локации
KorraCanCheks = { "IslandOfAir" : True }
KorraItems = {"Дробовик":0,"Соя":0}
Korra = KorraClass.Hero("Корра", 0, "Аватар",100)
KorraAlive=True
while KorraAlive == True:
    Korra.status()
    Scene.Tutorial_Field()
    print(Korra.Status())
    print(KorraItems)
    KorraAlive=False
End=input("This Is The End.Press Enter To Exit")
