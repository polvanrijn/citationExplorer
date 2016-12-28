import bibtexparser
import json
import re
import sys

try:
	bibfile = str(sys.argv[1])
	jsonfile = str(sys.argv[2])
except IndexError:
	print('Arguments are not enough.')
	raise

with open(bibfile) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

nodes = []
links = []
bibjson = {'nodes':nodes, 'links':links}

# create nodes and links
for bib in bib_database.entries:
	# publication nodes
	p_node = {}
	p_node['name'] = bib['ID'] # ID (e.g., John2010Venue)
	p_node['author'] = bib['author']	
	p_node['type'] = 2 # publication node equals to 2
	# add icon
	p_node['icon'] = 'icon/pnode.png'
	p_node['title'] = bib['title']
	# pages
	if 'pages' in bib:
		p_node['pages'] = bib['pages'].replace("--", "-")
	# year	
	if 'year' in bib:
		p_node['year'] = bib['year']
	# keyword
	if 'keyword' in bib:
		p_node['keyword'] = bib['keyword']
	# Publisher, organization
	if 'publisher' in bib:
		p_node['publisher'] = bib['publisher']
	# Organization
	if 'organization' in bib:
		p_node['organization'] = bib['organization']	
	# DOI
	if 'doi' in bib:
		p_node['doi'] = bib['doi']
	# ISBN
	if 'ISBN' in bib:
		p_node['isbn'] = bib['isbn']
	# booktitle
	if 'booktitle' in bib:
		p_node['booktitle'] = bib['booktitle']
	# journal
	if 'journal' in bib:
		p_node['journal'] = bib['journal']
	if 'number' in bib:
		p_node['number'] = bib['number']
	if 'volume' in bib:
		p_node['volume'] = bib['volume']
	nodes.append(p_node)
	
	# author nodes
	authors = re.split(' and ', bib['author'].replace("\n", " "))
	for author in authors:
		a_node = {}
		author_name = author.strip()
		# print author_name
		if re.search(",", author_name):
			m = re.split(",", author_name)
			a_node['name'] = (m[1] + " " + m[0]).strip()
		else:
			a_node['name'] = author_name.strip()
		a_node['type'] = 1 # author type equals to 1
		a_node['icon'] = 'icon/anode.png'		
		if a_node not in nodes:
			nodes.append(a_node)
		# create links
		link = {}
		link['source'] = nodes.index(a_node) 
		link['target'] = nodes.index(p_node)
		links.append(link)

with open(jsonfile, 'w') as outfile:
    json.dump(bibjson, outfile)
