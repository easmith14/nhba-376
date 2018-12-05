import requests
import json
from pymongo import MongoClient
import pprint

def createSection(page, token, title, text):
	data = {'action': 'edit',
	'title': page,
	'section': 'new',
	'sectiontitle': title,
	'text': text,
	'token': token }

	# Post request to create a new article using the data object abovek
	result = requests.post('http://montaigu.cs.yale.edu/nhba/mediawiki/api.php', data = data)
	print(result.text) # Should see success in response if this works

def makeInfobox(page, token, building):

	address = building['address']
	architect = building['architect']
	client = building['client']
	year_built = building['year_built']

	infobox = '''
	{{{{Infobox
	|title = {0}
	|header1 = {1}
	|label2 = Address
	|data2 = {2}
	|label3 = Architect
	|data3 = {3}
	|label4 = Client
	|data4 = {4}
	|label5 = Year Built
	|data5 = {5}
	}}}}'''.format(page, page, address, architect, client, year_built)

	data = {'action': 'edit',
	'title': page,
	'section': 0,
	'text': infobox,
	'token': token }

	# Post request to create a new article using the data object abovek
	result = requests.post('http://montaigu.cs.yale.edu/nhba/mediawiki/api.php', data = data)
	print(result.text) # Should see success in response if this works

	#Add the coordinate geotagger to map buildings
	data = {'action': 'edit',
	'title': page,
	'section': 0,
	'text': '{{ #set: |BuildingCoordinates={{ #geocode: {0} }} }}'.format(address),
	'token': token }

	# Post request to create a new article using the data object abovek
	result = requests.post('http://montaigu.cs.yale.edu/nhba/mediawiki/api.php', data = data)
	print(result.text) # Should see success in response if this works

def createArticle(building):
	# Get an edit token so you can create / edit an article
	r = requests.get('http://montaigu.cs.yale.edu/nhba/mediawiki/api.php?action=query&meta=tokens&format=json')
	#print(r.text)
	tmp = json.loads(r.text)
	token = tmp['query']['tokens']['csrftoken']

	building_name = building['building_name']
	address = building['address']
	year_built = building['year_built']
	overview_description = building['overview_description']
	physical_description = building['physical_description']
	site_history = building['site_history']
	social_history = building['social_history']
	urban_setting = building['urban_setting']

	makeInfobox(building_name, token, building)

	if len(overview_description) > 0:
		createSection(building_name, token, 'Overview Description', overview_description)
	if len(physical_description) > 0:
		createSection(building_name, token, 'Physical Description', physical_description)
	if len(site_history) > 0:
		createSection(building_name, token, 'Site History', site_history)
	if len(social_history) > 0:
		createSection(building_name, token, 'Social History', social_history)
	if len(urban_setting) > 0:
		createSection(building_name, token, 'Urban Setting', urban_setting)



def insertToTable(table_name, object):
	# open file
	filename = 'nhba-db.sql'

	sql = open(filename, 'a')
	sql.write()

	# write insert statement
	insert = 'INSERT INTO ' + table_name + ' ('
	# for each column add the corresponding value for the current object
	for key in object:
	    insert += str(key) + ','

	insert = insert[:-1]
	insert += ') VALUES ('

	for value in object.values():
	    insert += '"' + str(value) + '"' + ','

	insert = insert[:-1]
	insert += ')'

	sql.write(insert + '\n')

	# close file
	sql.close()


# These two lines are necessary to get the correct database from Mongo
client = MongoClient()
db = client.nhba

# Inside curly braces for find(), you can specify mongo queries. If blank, it just loads the entire thing
table = db.buildings.find({})

# This converts table to a iterable, list format
table_list = list(table)

# To make things easier to read in terminal
pp = pprint.PrettyPrinter(indent=4)
building = table_list[2]
pp.pprint(building)

''' TODO:
for i in range(len(table_list)):
	# Create a new mediawiki entry using the post request below:
'''
createArticle(building)
insertToTable('Buildings', building)
