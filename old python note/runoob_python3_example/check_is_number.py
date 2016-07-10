#check_is_number.py

def is_number(a):
	try:
		float(a)
		return True
	except ValueError:
		pass

	try:
		import unicodedata
		unicodedata.numeric(a)
		return True
	except (TypeError, ValueError):
		pass

	return False

