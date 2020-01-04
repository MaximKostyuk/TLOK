"""Если KorraCanBeHere True, это значит, что локация должна выполнять свое предназначение"""
def islandOfAir(KorraCanBeHere = True):
	KCBHCheker = f'Позволитель = {KorraCanBeHere}'
	print ( KCBHCheker)
	nameOfIsland = "Остров Воздуха"
	print ( nameOfIsland )
	if KorraCanBeHere == False:
		print ( "Эта сюжетно важная локация больше не доступна" )
		KorraCanBeHere = False
	else:
		print ( "Можно запускать действия" )
		def doSomething():
			print ( "In DoSomething" )
#KorraCanCheks = { "IslandOfAir" : True }
#k =islandOfAir(KorraCanCheks["IslandOfAir"])
#KorraCanCheks["IslandOfAir"] = k
#islandOfAir(KorraCanCheks["IslandOfAir"])
