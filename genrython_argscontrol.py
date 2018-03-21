#usr/bin/python3
# Adrian Garcia Moreno

#Script to control the input of the commands using argparse

import argparse
import os
        
def is_directory(path_str):
    if os.path.isdir(path_str):
        return path_str
    else:
        msg = "{} is not a directory".format(path_str)
        raise argparse.ArgumentTypeError(msg)    


parser = argparse.ArgumentParser(  
    prog='Genrython',
    prefix_chars='-',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='''A functional analysis tool''',
    epilog='''Under development''',
    )

# The inputs to the program must be:
# 1. Input
    # File/s
    # Directory/ies
# 2. Ontology/Mapping File
# 3. Statistic Test
# 4. p-Value Cut-Off
# 5. Output Folder/File-s

input_group = parser.add_mutually_exclusive_group(required=True)

input_group.add_argument('-f','--infile', 
help='File/s as input', nargs='?', type=open)

input_group.add_argument('-d','--directory', 
help='Directory/ies with all and only your query files', nargs='?',
type=is_directory)

parser.add_argument('-map','--mapfile', 
help='Mapping file/s with the desired ontology', nargs='?')

parser.add_argument('-test','--teststatistic', 
help='Statistic test to apply for your data and ontology', nargs='?')
# Avoid required arguments!!!!! # Until defaults can be providen

parser.add_argument('-cut','--pvalcutoff', nargs='?',
help='Determine the minimun valor of the p-value to filter the results ((values: between) - default: %(default)s) ',
default=0.05, type=float, choices=map(lambda x: x/100.0, range(0,105, 5)))

parser.add_argument('-o','--outputfolder', 
help='The name of the folder where your results will be dumped', nargs='?')
parser.add_argument('-v', '--version', 
action='version', version='%(prog)s 0.0.1')

args = parser.parse_args()

#print ("Files:{}\nMap:{}\nCutOff:{}\nOutFolder:{}\nTest:{}".format(
#args.infile, args.mapfile, args.pvalcutoff, args.outputfolder, args.teststatistic))


