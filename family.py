import json 
with open('family.json') as outfile:
	data = json.load(outfile)

	#data1 = json.load(write_json)
found=False
find = False
find2 = False
test =True
test2 =True
list1 = []
list2 = []
def validateFamily(member):

	for c in member['child']:
		#parent_name = 'Prem'    
		#if parent_name == member['name']:
		if(c['age'] == '' and member['name']==''):
			print("Your enter a invalid data")
			return False
		elif(c['age'] == ''):
			print("Your enter a invalid age of a name ", c['name'])
			return False
		elif (member['age']==''):
			print("Your enter a invalid age of a name ", member['name'])
			return False
		elif(member['name']==''or c['name']==''):
			print("Your enter a nothing")
			return False

		if(c['age'] < member['age']): # It is recursive 
			#print("Child is elder than father")
			print("FAILED::: Child's  is:"+c['name']+"\tParents is: "+member['name'])

		else:
			print("PASS::: Child's is:"+c['name']+"\tParents is: "+member['name'])
		validateFamily(c)
# def user_input():
# 	name = str(input("Enter your name: "))
# 	age = str(input("Enter your age: "))
# 	parent_name = str(input("Enter your parent name: "))

def insertFamily(name, age, parent, member):
	for c in member['child']:
		global found
		if(c['name']==parent  and c['age']>age):
			
			found=True
			c['child'].append({'name':name, 'age':age, 'child':[]})
			with open('family.json', 'w') as write_json:
				json.dump(data, write_json)
			return
		elif(member['name']==parent and member['age']>age):
			found=True
			member['child'].append({'name':name, 'age':age, 'child':[]})
			with open('family.json', 'w') as write_json:
				json.dump(data, write_json)
			return
		elif(parent not in c['name'] and parent not in member['name'] ):
			insertFamily(name, age, parent, c)
		
def find_Ancestor_list1(member, person1):
	global test, list1, find
	if test == True:
		list1.append(member['name'])
		test = False
	for c in member['child']:
		#list1.append(member['name'])
		list1.append(c['name'])
		if(member['name'] == person1):
			list1.append(member['name'])
		if(c['name'] == person1 ):
				find = True	
				
		else:
			find_Ancestor_list1(c, person1)
	


def elementosEnComunEntre(list1, list2):

    elementosEnComun = set()

    for e1 in list1:
         if(e1 in list2):
             elementosEnComun.add(e1)

    return list(elementosEnComun)



def find_Ancestor_list2(member, person2):
	global test2, list2, find2
	if test2 == True:
		list2.append(member['name'])
		test2 = False
	for c in member['child']:
		#list1.append(member['name'])
		list2.append(c['name'])
		if(member['name'] == person2):
			list2.append(member['name'])
		if(c['name'] == person2 ):
				find2 = True	
				
		else:
			find_Ancestor_list2(c, person2)
	
if __name__ == "__main__":
	print("First to validate our data")
	key_to_hold = input('Enter any key')
	for member in data:
		validateFamily(member)

	print('To create a object or to existing parent user enter the following input')
	name = input("Enter your name :")
	parent = input('Enter your parent name :')
	age = str(input("Enter you age :"))
	for member in data:
		insertFamily(name, age, parent, member)

	if found == False:
		print("Parent not found : ", found)
		print("Data are enter as new object")
	if found == True:
		temprary_data = {'name':name, 'age':age, 'child':[]}
		data.append(temprary_data)
		with open('family.json', 'w') as write_json:
			json.dump(data, write_json)

	print("two strings are enter by user for comparision:")
	person1 = input("Enter the first string you want to compare :")
	person2 = input("Enter the second string you want to compare :")


	for member in data:
		find_Ancestor_list1(member, person1)
		#list1 = []
		#print(list1[0])

	if find == False:
		list1 = []

	
	for member in data:
		find_Ancestor_list2(member, person2)

	if find2 == False:
		list2 = []
		#print(list2[0])


		
	print('To find a common ancestors or does not belong to a family:')

	results = elementosEnComunEntre(list1, list2)
	if results:
		print("common ancestor is :")
		print(results)
		print("Least common ancestor is :")
		print(results[0])
	elif list1 == '' or list2 == '':
		print("It does not belong to same family")
	else:
		print("It does not belong to same family")


    

	

    
