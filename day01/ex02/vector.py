class Vector:
	def __init__(self, values):
		if not isinstance(values, list):
			raise TypeError("values have to be a list")
		else:
			for i in values:
				if not isinstance(i, float):
					raise TypeError("values have to be float")
		self.values = list(values)
		self.size = len(self.values)
	def __radd__(self, other):
		v = Vector([])
		j = 0
		for i in self.values:
			v.values.append(i + other.values[j])
			j += 1
		return v
	def __add__(self, other):
		v = Vector([])
		try:
			for i in self.values:
				v.values.append(i + float(other))
			return v
		except:
			return self.__radd__(other)
	def __rsub__(self, other):
		v = Vector([])
		j = 0
		for i in self.values:
			v.values.append(i - other.values[j])
			j += 1
		return v
	def __sub__(self, other):
		v = Vector([])
		try:
			for i in self.values:
				v.values.append(i - float(other))
			return v
		except:
			return self.__rsub__(other)
	def __rtruediv__(self, other):
		v = Vector([])
		j = 0
		for i in self.values:
			v.values.append(i / other.values[j])
			j += 1
		return v
	def __truediv__(self, other):
		v = Vector([])
		try:
			for i in self.values:
				v.values.append(i / float(other))
			return v
		except:
			return self.__rtruediv__(other)
	def __rmul__(self, other):
		v = Vector([])
		j = 0
		for i in self.values:
			v.values.append(i * other.values[j])
			j += 1
		return v
	def __mul__(self, other):
		v = Vector([])
		try:
			for i in self.values:
				v.values.append(i * float(other))
			return v
		except:
			return self.__rmul__(other)
	#def __str__(self, other):
	#def __repr__(self, other):
v1 = Vector([0.0, 1.0, 2.0, 3.0])
print(v1.values)
v2 = v1 + 2
print(v2.values)
v3 = v1.__add__(v2)
print(v3.values)
print(Vector([0.0, 1.0, 2.0, 3.0]).size)