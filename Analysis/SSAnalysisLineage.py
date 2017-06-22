#This program is used for analysis of the LineageData.json file produced by simple systme.
#Currently, it finds the alive organisms in the population, and locates the last common ancestor.

import json

#function to loop through tree & find alive organisms
def findAlive(data, alive, organisms,parent):
	for org in data['children']:
			org['parent']= parent
			if(org['alive']):
				newparent=data['children'][0]
			elif(org['children']):
				newparent=org
			else:
				newparent= org['parent']

		#Find alive organisms
			if (org['alive']):
				alive.append(org['name'])
				organisms.append(org['name'])
				findAlive(org, alive, organisms, newparent)

			else:
				findAlive(org, alive, organisms, newparent)
				organisms.append(org['name'])


#Function to find the bottom leaf nodes (nodes with no children at bottom of lineage tree)
def findBottomNodes(data, nodes):
	for org in data['children']:
		if(org['children']):
			findBottomNodes(org, nodes)

		else:
			nodes.append(org['name'])
			findBottomNodes(org, nodes)

#Function to find the last common ancestor
def findCommon(data, count):
	for child in data['children']:
		count = 0
		for org in child['children']:
			count=count+1
		if(count == 2):
			print("common ancestor is :", child['name'])
		elif(child['alive']):
			print("common ancestor is:", child['name'])
		else:
			findCommon(child, count)


def traceCommon(data):
	to_delete = []

	for org in data['children']:
		if(org['children'] or org['alive']):
			traceCommon(org)
			if not (org['children']) and not (org['alive']):
				to_delete.append(org)

		else:
			to_delete.append(org)

	for organism in to_delete:
		data['children'].remove(organism)

def main():
	#load json file
		#with open(r'/user/johankn1/hpcc/simpleSystem/experiment1/1/lineageData.json') as datafile:
		with open(r'Data/lineageData.json') as datafile:
			data=json.load(datafile)

		#NOTES: alive-> list of alive organisms, organisms->list of all organisms in tree, nodes->list of bottom leaf node organisms in tree, data-> json lineage data
			alive= []
			organisms=[]
			parent=data[0]

			findAlive(data[0], alive, organisms,parent)

			nodes=[]
			findBottomNodes(data[0], nodes)

			traceCommon(data[0])

			print("alive organisms: ", alive)
			count=0
			findCommon(data[0], count)

		return 0

if __name__ == '__main__':
	main()
