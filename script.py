import requests
import json
import re
from pymongo import MongoClient
import pprint

map = {}
map['_id'] = 'PK_building_id'
map['roof_types'] = 'roof'
map['current_tenant'] = 'FK_current_tenant'
map['researcher'] = 'FK_researcher'
map['street_visibilities'] = 'visible_from_road'
map['eras'] = 'era'
map['owner'] = 'current_owner'
map['building_name'] = 'building_name_common'
map['threats'] = 'threats_to_site'
map['current_uses'] = 'FK_current_uses'
map['structures'] = 'structural_systems'
map['structural_conditions'] = 'structural_conditions'
map['external_conditions'] = 'external_conditions'
map['images'] = 'images'
map['archive_documents'] = 'archive_documents'
map['dimensions'] = 'dimensions'
map['social_history'] = 'social_history'
map['client'] = 'client'
map['styles'] = 'styles'
map['accessibilities'] = 'interior_accessible'
map['site_history'] = 'site_history'
map['levels'] = 'number_stories'
map['overview_description'] = 'overview'
map['roof_materials'] = 'roof_materials'
map['physical_description'] = 'physical_description'
map['year_built'] = 'year_built'
map['neighborhoods'] = 'neighborhoods'
map['materials'] = 'materials'
map['architect'] = 'FK_architect'
map['historic_uses'] = 'historic_uses'
map['past_tenants'] = 'past_tenants'
map['address'] = 'address'
map['latitude'] = 'longitude'
map['urban_setting'] = 'streetscape_urban_setting'
map['tours'] = 'tours'
map['related_outbuildings'] = 'related_buildings_and_features'
map['sources'] = 'sources'
map['creator'] = 'creator'

def createSection(page, token, title, text):
	data = {'action': 'edit',
	'title': page,
	'section': 'new',
	'sectiontitle': title,
	'text': text,
	'token': token }

	# Post request to create a new article using the data object abovek
	result = requests.post('http://montaigu.cs.yale.edu/nhba/mediawiki/api.php', data = data)
	#print(result.text) # Should see success in response if this works

def makeInfobox(page, token, building):

	address = ''
	architect = ''
	client = ''
	year_built = ''

	if 'address' in building:
		address = building['address']
	if 'architect' in building:
		architect = building['architect']
	if 'client' in building:
		client = building['client']
	if 'year_built' in building:
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
	#print(result.text) # Should see success in response if this works

def createArticle(building):
	# Get an edit token so you can create / edit an article
	r = requests.get('http://montaigu.cs.yale.edu/nhba/mediawiki/api.php?action=query&meta=tokens&format=json')
	#print(r.text)
	tmp = json.loads(r.text)
	token = tmp['query']['tokens']['csrftoken']

	building_name = ''
	address = ''
	year_built = ''
	overview_description = ''
	physical_description = ''
	site_history = ''
	social_history = ''
	urban_setting = ''

	if 'building_name' in building:
		building_name = building['building_name']
	if 'address' in building:
		address = building['address']
	if 'year_built' in building:
		year_built = building['year_built']
	if 'overview_description' in building:
		overview_description = building['overview_description']
	if 'physical_description' in building:
		physical_description = building['physical_description']
	if 'site_history' in building:
		site_history = building['site_history']
	if 'social_history' in building:
		social_history = building['social_history']
	if 'urban_setting' in building:
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
	#sql.write()

	insert = 'INSERT INTO ' + table_name + ' ('
	values = ') VALUES ('
	# for each column add the corresponding value for the current object
	for key in object:
		if key in map.keys():
			insert += map[key] + ','
			string = str(object[key])
			# re.sub(r'\\', )
			# re.sub(r'\'', '\\\'', string)
			values += "`" + re.sub(r'\'', '\\\'', str(object[key])) + "`" + ','

	insert = insert[:-1]

	values = values[:-1]
	values += ');'
	final = insert + values

	# # write insert statement
	# insert = 'INSERT INTO ' + table_name + ' ('
	# # for each column add the corresponding value for the current object
	# for key in object:
	#     insert += str(key) + ','
	#
	# insert = insert[:-1]
	# insert += ') VALUES ('
	#
	# for value in object.values():
	#     insert += "`" + str(value) + "`" + ','
	#
	# insert = insert[:-1]
	# insert += ')'

	sql.write(final + '\n')

	# close file
	sql.close()

def fixGeo():

	coords = '''
	{{{{ #set: |BuildingCoordinates={{{{ #geocode: {0} }}}}}}}}
	'''.format(address),

	#Add the coordinate geotagger to map buildings
	data = {'action': 'edit',
	'title': page,
	'section': 0,
	'text': '{{ #set: |BuildingCoordinates={{ #geocode: {0} }} }}'.format(address),
	'token': token }

	# Post request to create a new article using the data object abovek
	result = requests.post('http://montaigu.cs.yale.edu/nhba/mediawiki/api.php', data = data)

# These two lines are necessary to get the correct database from Mongo
client = MongoClient()
db = client.nhba

# Inside curly braces for find(), you can specify mongo queries. If blank, it just loads the entire thing
table = db.buildings.find({})

# This converts table to a iterable, list format
table_list = list(table)

# To make things easier to read in terminal
pp = pprint.PrettyPrinter(indent=4)
# building = table_list[0]
# insertToTable('Buildings', building)

# pp.pprint(building)
# for i in range(178, len(table_listo)-1):
for i in range(len(table_list)):
	# Create a new mediawiki entry using the post request below:
	building = table_list[i]
	if ('building_name' in building):
	# 	if (len(building['building_name']) > 0):
	# 		createArticle(building)
		insertToTable('Buildings', building)
