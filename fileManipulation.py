# function for file manipulations
import os #OS module in Python provides functions for interacting with the operating system.

# writing contents into a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# appending contents at the end of the file
def append_to_file(path, data):
    with open(path, 'a') as file:# with statement makes the code compact and readable. with statement helps avoiding bugs
    #and leaks by ensuring that a resource is properly released when the code using the resource is completely executed
        file.write(data + '\n')

# read a file and convert each line into set items
def file_to_set(fileName):
    results = set()
    with open(fileName, 'rt') as f: 
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# Iterate through a set. Each items in the set, will be a new line in the file
def set_to_file(links, fileName):
    with open(fileName, 'w'):
        for link in sorted(links):
            append_to_file(fileName, link)

def create_project_dir(directory):
    if not os.path.exists(directory):#returns true or false
        print("Creating project: ", directory) #Crawler.project_name is directory
        os.makedirs(directory)

# creating a new file
def create_data_files(project_name, base_url):
    queue = project_name + '/queueList.txt'
    crawled = project_name + '/crawledList.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url) # we pass the base_url as the initial variable
    if not os.path.isfile(crawled):
        write_file(crawled, '')
