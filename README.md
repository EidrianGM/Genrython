# Genrython

A command line tool for studying genes and other biological elements with associated ontologies. 

The main idea is to develop a tool that receives a query list (or directory of lists) and an ontology mapping file, and outputs an unformatted, tab-separated table containing the results. It would also be beneficial to implement a network propagation analysis feature that identifies modules using [Heat Diffusion](https://github.com/idekerlab/heat-diffusion) and [Networkx](https://networkx.github.io/).
Throughout development, a variety of spontaneous [bioinformatics tools](#derivative-tools) are expected the materialise.

*Genrython* must evolve to support more gene nomenclatures, ontologies and statistics tests; the first version should support:

## Ontology
1. [Gene Ontology](http://www.geneontology.org/)

## Gene Nomenclature
1. [EntrezID (NCBI)](https://www.ncbi.nlm.nih.gov/gene/1)

## Statistic
1. Fisher Exact test

# *Derivative Tools*
In **AnnotationSources** tools to download, and keep track of interesting annotation file sources and also to transform among different nomenclatures.
