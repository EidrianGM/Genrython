# Annotation Sources
BioInformatics, and I would say unfortunately, has different nomenclatures
to deal with the genomic information due to different academia. Which It is traduced in different ways of naming and localising the different genome's elements.
To concieve an idea of this variability here is a web tool in order to transform between different nomenclatures data bases [HGNC-Download](https://www.genenames.org/cgi-bin/download). 

In order to keep tidy and updated the genomic information needed for the research project here I offer some scripts in the [*bin directory*](https://github.com/EidrianGM/Genrython/tree/master/AnnotationSources/bin): 

* *Downloader.py* makes use of **AnnotUrls.json** so that once it is called, it will print the names given to the annotation files URLs added by me, plus thouse you have added in that json. Immediately after it will ask for the annotation name and download it.

* The same **AnnotUrls.json** can be updated calling *AnnotsURLsUpdater.py* which will show you the actual annotations recorded and ask for a *Name* and *URL* to be saved later writting **exit**.  

* *cols_jsonaizer.py* lets you to save in a json any tsv-like file specifying the number of the columns separated by ':'. The information is saved in a nested dictorionary considering that each column is categorical, for example imagine your annotation file is the Gene Ontology, the first column is the GO_ID the third is the GeneID and the seventh is the GO category. In this case the desired json could have the following structure {GOcategory:{GO_ID:[GeneID]} and to achieve this you have to indicate to the script the number of the columns in its proper order 7:1:3. Write >> *pyhton cols_jsonaizer.py -h* to understand its usage. 



