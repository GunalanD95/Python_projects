guna_tmp = """hello iam {name}, iam {age}"""


def guna(my_name = "guna", my_age = "22"):
	v = guna_tmp.format(name = my_name, age = my_age)
	return v

print(guna())