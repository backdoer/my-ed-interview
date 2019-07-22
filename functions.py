## linear search
def linear_search(iterable, attribute, value):
	for obj in iterable:
		if getattr(obj, attribute) == value:
			return obj

def create_dict_from_list(iterable):
	## creates a dictionary, with id and name, from a list of objects assuming objects have an id and name
	new_dict = {}
	for x in iterable:
		new_dict[x.id] = x.name
	return new_dict
