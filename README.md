# Scholarmap
Scholarmap shows the academic contribution using network structures.
This application is implemented by D3 and jQuery and inspired by [Mike Bostock’s force layout example](https://bl.ocks.org/mbostock/4062045) and [Simon Raper's feature showcase](http://www.coppelia.io/2014/07/an-a-to-z-of-extra-features-for-the-d3-force-layout/).


Check this [example](http://kin-y.github.io/scholarmap/), which is based on a [bibtex](https://github.com/kin-y/scholarmap/blob/master/bibtex.bib) of my papers.

## Features:
- A python script to parse BibTeX files to JSON files
- Draggable force layout graph
- Able to show/hide label of nodes 
- Able to search authors or publications

## How to use:

1. Clone this repository or download the zip.

  ```git clone https://github.com/kin-y/scholarmap.git```

2. Prepare a BibTeX file, and put it into the root directory of this repository. For example, you can save it as `bibtex.bib`

3. Parse the BibTeX file to JSON file using python script `bib2json.py`. To run the script, you need to add two arguments: the source BibTeX file name (e.g., `bibtex.bib`) and the target JSON file name (e.g., `bibtex.json`)

  ```python bib2json.py bibtex.bib bibtex.json```

4. Browse the graph on your HTTP server. For example, run python simple HTTP server and open the web browser `localhost:8000`. Enjoy it!
