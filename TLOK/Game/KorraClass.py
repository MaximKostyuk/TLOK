class Hero(object):
	def __init__(self, name, money, society):
		self.name = name
		self.money = money
		self.society = society
		print ( "Имя: " + name + " Денег: " + str(money) + " Соц.Статус: " + society )
	def status(self, health):
		self.health = 100
		print ( "Здоровье: " + health )
		return health
