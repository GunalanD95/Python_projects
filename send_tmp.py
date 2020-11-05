import os

email_txt = "templates.txt"

content = ''

fp = os.path.abspath(__file__)
print(fp)
BASE_DR = os.path.dirname(fp)
print(BASE_DR)
ENTIRE_PRO_DIR = os.path.dirname(BASE_DR)
print(ENTIRE_PRO_DIR)

email_txt = os.path.join(BASE_DR,"guna","templates.txt")

with open(email_txt, 'r') as f:
	content = f.read()


print(content.format(name = "gunalan"))