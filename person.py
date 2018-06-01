
class Person(object):

 	def __init__(self, name):
 		self.name = name

	def has_bike(self):
		return self.bike is not None

	def rent_bike(self, bike):
		if (self.has_bike):
            raise ValueError('You can only use one bike at a time')
        else:
		    self.bike = bike

	def return_bike(self):
		self.bike = None

    @property
    def name(self):
        return self.name

    @property
    def bike(self):
        return self.__bike

    @bike.setter
    def bike(self, bike):
        self.__bike = bike