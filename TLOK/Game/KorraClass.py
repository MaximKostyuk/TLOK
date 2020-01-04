class Hero(object):
	def __init__(self,name,money,society,health):
		self.name = name
		self.money = money
		self.society = society
		self.health = health
		print ( "Имя:" + name + " Денег:" + str(money) + " Соц.Статус:" + society )
	def status(self):
		print ( "Здоровье: " + str(self.health) )
	def talking(self,told):
		print ("Корра сказала: "+told)
