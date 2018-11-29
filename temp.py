import requests
import json
from pymongo import MongoClient
import pprint

# These two lines are necessary to get the correct database from Mongo

client = MongoClient()
db = client.nhba

# Inside curly braces for find(), you can specify mongo queries. If blank, it just loads the entire thing
table = db.buildings.find({})
# This converts table to a iterable, list format
table_list = list(table)

#print(len(table_list))

# To make things easier to read in terminal
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(table_list[0])

''' TODO: 
for i in range(len(table_list)):
	# Create a new mediawiki entry using the post request below: 
'''

def createArticle():
	# Get an edit token so you can create / edit an article
	r = requests.get('http://localhost:8888/api.php?action=query&meta=tokens&format=json')
	#print(r.text)
	tmp = json.loads(r.text)

	data = {'action': 'edit',
	'title': 'Hello',
	'text': 'Allen is cool',
	'token': tmp['query']['tokens']['csrftoken']}

	# Post request to create a new article using the data object above
	result = requests.post('http://localhost:8888/api.php', data = data)
	print(result.text) # Should see success in response if this works