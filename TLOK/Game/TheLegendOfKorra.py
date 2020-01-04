import KorraClass 
import Locations
KorraCanCheks = { "IslandOfAir" : True }
Korra = KorraClass.Hero("Корра", 0, "Аватар",100)
Korra.status()
Korra.talking("Привет")
k = Locations.islandOfAir(KorraCanCheks["IslandOfAir"])
KorraCanCheks["IslandOfAir"] = k
Locations.islandOfAir(KorraCanCheks["IslandOfAir"])
