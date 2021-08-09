import threading
from queue import Queue
from crawler import Crawler
import fileManipulation as files
import time
from urllib.parse import urlparse

# Get domain name (edu.pk)
def get_domain_name(url):
    try:
        results = get_subdomain_name(url).split(".") #results = ['lms', 'nust', 'edu', 'pk']
        return results[-2] + '.' + results[-1] #only the last 2 items of the results list
    except:
        return ''

# Get the subdomain name (lms.nust.edu.pk)
def get_subdomain_name(url):#returns
    try:
        return urlparse(url).netloc # parse through the given url and return the network location (netloc)
        #from the whole URL ignore scheme, query, fragments, port, username, password etc except location of network which comes after scheme
    except:
        return '' # since we need to return something!

# Creating Threads (The threads will die after main terminates)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)# When you create a Thread, you pass it a function.In this case,we are passing work function
        t.daemon = True 
        t.start() 

# Do the next job in the queue
# Essentially iterate through the queue and take each url and crawl it
# runs the threads in order due to semaphores
sem = threading.Semaphore() #for semaphores
def work():
    while True:
        url = queue.get()
        sem.acquire()
        #critical section start
        Crawler.crawl_page(threading.current_thread().name, url)
        queue.task_done()
        #critical section end
        sem.release()
        time.sleep(0.3)


# Basically each queued_link is a new job
def create_jobs():
    for link in files.file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join() # to avoid collision among multiple threads. Blocks until all items in the queue have been gotten and processed.
    crawl()


# iterating through the queue and checking if any urls are left
# if so then crawl them until the whole queue is empty
def crawl():
    queued_links = files.file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print('Total of ' + str(len(queued_links)) + ' links extracted in the queue. Crawling them 1 by 1 now....')
        create_jobs()

project_name = input("Enter the project name: ")
home_page = input("Enter the homepage URL: ")
threads = input("Enter number of threads: ")
threads = int(threads)

DOMAIN_NAME = get_domain_name(home_page)
QUEUE_FILE = project_name + '/queueList.txt'
CRAWLED_FILE = project_name + '/crawledList.txt'
NUMBER_OF_THREADS = threads
queue = Queue() 

# The first spider instance does not need a multithreaded approach.
# We just need to find generate the first queue of urls from the base_url.
Crawler(project_name, home_page, DOMAIN_NAME)
create_workers()
crawl()