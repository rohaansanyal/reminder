#reads what in the file
with open('text_file', 'r') as text:
	content = text.read()
	print(content)		
#replaces everything in file
with open('text_file', 'w') as text:
	content = text.write("anything")	
#adds to file
with open('text_file', 'a') as text:
	content = text.write("anything")	