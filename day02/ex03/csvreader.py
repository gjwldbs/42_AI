
class CsvReader(object):
	def __init__(self, file_name,sep=',', hbool=False, skip_top=0, skip_bottom=0):
		self.name = file_name
		self.sep = sep
		self.hbool = hbool
		self.top = skip_top
		self.bottom = skip_bottom
	def __enter__(self):
		try:
			self.file_obj = open(self.name, 'r')
		except:
			return None
		lst = self.file_obj.read().split('\n')
		if self.hbool is True:
			self.header = (lst[0].split(self.sep))[0]
		else:
			self.header = "No header"
		lst = lst[self.top: len(lst) - self.bottom - 1]
		self.data = (self.sep).join(lst).split(self.sep)
		return self
	def __exit__(self, *args):
		try:
			self.file_obj.close()
		except:
			return None
	def getheader(self):
		return self.header
	def getdata(self):
		return self.data
