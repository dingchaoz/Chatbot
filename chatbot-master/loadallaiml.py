import glob
x = glob.glob('roise/*aiml')
z = ['<learn>aiml/'+y+'</learn>' for y in x]
for y in z:
	print y