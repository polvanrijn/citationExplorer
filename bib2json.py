import bibtexparser
import json
import re

with open('ref.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

nodes = []
links = []
bibjson = {'nodes':nodes, 'links':links}

# create nodes and links
for bib in bib_database.entries:
	# publication nodes
	p_node = {}
	p_node['name'] = bib['ID'] # ID (e.g., John2010Venue)
	if bib['ENTRYTYPE'] == 'article': # article type equals to 2
		p_node['type'] = 2
	elif bib['ENTRYTYPE'] == 'inproceedings': # inproc type equals to 3
		p_node['type'] = 3
	elif bib['ENTRYTYPE'] == 'book': # book type equals to 4
		p_node['type'] = 4
	elif bib['ENTRYTYPE'] == 'misc': # misc type equals to 5
		p_node['type'] = 5
	p_node['icon'] = 'icon/pnode.png' 
	nodes.append(p_node)
	
	# author nodes
	authors = re.split(' and ', bib['author'].replace("\n", " "))
	for author in authors:
		a_node = {}
		author_name = author.strip()
		print author_name
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

with open('bibtex.json', 'w') as outfile:
    json.dump(bibjson, outfile)
