import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
import json
import re

bibfile = "sample.bib"
jsonfile = "sample.json"

with open(bibfile) as bibtex_file:
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    bib_database = bibtexparser.load(bibtex_file, parser=parser)

nodes = []
links = []
bibjson = {'nodes': nodes, 'links': links}


def split_authors(authors_string):
    return re.split(' [a, A][n, N][d, D] ', authors_string.replace("\n", " "))


def get_pairs(list):
    result = []
    for p1 in range(len(list)):
        for p2 in range(p1 + 1, len(list)):
            val1 = list[p1]
            val2 = list[p2]
            if (val1 < val2):
                result.append([val1, val2])
            else:
                result.append([val2, val1])
    return result


author_list = []
link_list = {}
id_count = 0

# create nodes and links
for bib in bib_database.entries:
    authors = []
    if 'author' in bib.keys():
        authors = split_authors(bib['author'])
    if 'editor' in bib.keys():
        authors = authors.append(split_authors(bib['editor']))
    if authors is not None:
        author_ids = []
        for author in authors:
            a_node = {}
            author_name = author.strip()
            # print author_name
            if re.search(",", author_name):
                m = re.split(",", author_name)
                a_node['name'] = (m[1] + " " + m[0]).strip()
            else:
                a_node['name'] = author_name.strip()
            a_node['weight'] = 1  # author type equals to 1

            current_id = None

            new_node = True
            for node in nodes:
                if node['name'] == a_node['name']:
                    node['weight'] += 1
                    new_node = False
                    current_id = node['id']

            if new_node:
                a_node['id'] = id_count
                current_id = id_count
                id_count += 1
                nodes.append(a_node)

            if current_id is None:
                raise ValueError('This cannot happen!')
            else:
                author_ids.append(current_id)

        for pair in get_pairs(author_ids):
            key = "%d_%d" % (pair[0], pair[1])
            if key in link_list.keys():
                link_list[key] += 1
            else:
                link_list[key] = 1

for key, weight in link_list.items():
    link = {}
    pair = key.split('_')
    link['source'] = int(pair[0])
    link['target'] = int(pair[1])
    link['weight'] = weight
    links.append(link)

with open(jsonfile, 'w') as outfile:
    json.dump(bibjson, outfile)
