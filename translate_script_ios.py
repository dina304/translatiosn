import csv

file = open("Standard-nl.plist")
data = file.read()

beg = data.find("<string>")
end = data.find("</string") + len("</string>")


to_remove = []
while beg != -1 :
	to_add = data[beg:end]
	to_remove.append(to_add)
	beg = data.find("<string>",beg+1)
	end = data.find("</string",end+1) + len("</string>")

	
	
for string in to_remove:
	data = data.replace(string,'')
		
file.close()
file = open("Standard-nlTest.plist", "w+")
data = "".join(data)
file.write(data)


#creating dict of key and value
with open('Kruidvat Field Names and Values - kruidvat json.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	dict = {}
	for row in csv_reader:
		if row['iOS Field Name'] != '' and row['iOS Value'] != '':
			dict[row['iOS Field Name']] = row['iOS Value']
			
			
			

file = open("Standard-nlTest.plist","r+")
lines = file.readlines()
for key in dict.keys():
	strV = "<string>" + dict[key] + "</string>"
	strK = "<key>" + key + "</key>"
	for i in range(0,len(lines)-1):
		if strK in lines[i] and "<dict>" not in lines[i+1]:
			temp = lines[i][:lines[i].index('<')]
			temp += strV + "\n"
			lines[i] += temp
			
		
counter = 1
for i in range(0,len(lines)-1):
	if "string" not in lines[i] and "key" in lines[i] and "<dict>" not in lines[i+1]:
		strV = "<string>" + str(counter) + "</string>"
		temp = lines[i][:lines[i].index('<')]
		temp += strV + "\n"
		lines[i] += temp 
		counter += 1
				
data = "".join(lines)
file.close()



data = "".join(lines)


file = open("Standard-fr.plist","w+")
file.write(data)
