import sys
import json
from lxml import etree

maxdepth =0
#max depth function
def depth(elem, level): 
    global maxdepth
    if (level == maxdepth):
        maxdepth += 1
    # recursive call to function to get the depth
    for child in elem:
        depth(child, level + 1)
    return maxdepth

def stats(file, j_file):
    #create dict to convert to JSON later
    stat_dict={}
    #open the file and get lxml etree setup to sort elements
    tree = etree.parse(file) 
    #create counts for file and directory
    number_of_files = int(tree.xpath('count(//fsimage/INodeSection/inode[type="FILE"])')) 
    number_of_directories = int(tree.xpath('count(//fsimage/INodeSection/inode[type="DIRECTORY"])'))

    #find the max depth of the directory tree
    maximum_depth_of_directory_tree = depth(tree.getroot(), 0)
    # maximum_depth_of_directory = depth(tree.xpath(//fsimage/INodeDirectorySection), -1)

    #get file size max and min
    #get all NumBytes
    file_info = tree.xpath('//fsimage/INodeSection/inode/blocks/block/numBytes/text()')
    #make the list of list of ints
    file_info = [int(i) for i in file_info]
    #create dict to add to existing dict
    file_size= {}
    file_size['max']=max(file_info)
    file_size['min']=min(file_info)

    #add the values from the created variables to the stat_dict
    for variable in ["number_of_files","number_of_directories", "maximum_depth_of_directory_tree", "file_size"]: 
        stat_dict[variable]=eval(variable)

    #convert dict to json file
    with open(j_file, "w") as outfile:
        json.dump(stat_dict, outfile)

if __name__ == '__main__':
    k = sys.argv[1]
    l = sys.argv[2]
    stats(k,l)
