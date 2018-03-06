# Genrython

A command line controlled tool to study gene or any other biological elements that have an associated ontology. 
The main idea is to develop a tool that let the user to provide any query list or lists (directory with lists) and an ontology mapping file and recieve as output an unformatted tab separated table with the results. An extra feature to be implemented is a network propagation analysis with the identification of modules using [Heat Diffusion](https://github.com/idekerlab/heat-diffusion) and [Networkx](https://networkx.github.io/).
During its development is expected the spontaneous materialisation of small Bioinformatic tools with different aims. The hard data is expected to be saved in JSON format.

The tool must evolve as more gene nomenclatures, ontologies and statistics tests are supported. 
The first version should be able to support:

## Ontology
1. [Gene Ontology](http://www.geneontology.org/)

## Gene Nomenclature
1. [EntrezID (NCBI)](https://www.ncbi.nlm.nih.gov/gene/1)

## Statistic
1. Fisher Exact test

# Derivative Tools
In **AnnotationSources** tools to download, and keep track of interesting annotation file sources and also to transform among different nomenclatures.
