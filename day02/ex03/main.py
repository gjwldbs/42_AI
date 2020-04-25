from csvreader import CsvReader

if __name__ == "__main__":
	print("---GOODCSV---")
	with CsvReader("good.csv", ',', True) as reader:
		if reader == None:
			print("File corrupted!")
		else:
			print(reader.getheader())
			print(reader.getdata())
			for i in reader.getdata():
				print(i)
	print("---BADCSV---")
	with CsvReader("bad.csv", ',', False) as reader:
		if reader == None:
			print("File corrupted!")
		else:
			print(reader.getheader())
			print(reader.getdata())
			for i in reader.getdata():
				print(i)