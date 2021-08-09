# Multi-threaded-Web-Crawler
To crawl web content using Python

System:
•	Linux-Ubuntu (preferred)
•	Windows

Language:
•	python3

For installing Libararies: 
Linux-Ubuntu: 
•	sudo apt install python3-pip  (if pip not installed)
•	python3 -m pip install requests
Windows:
•	Download get-pip.py  (if pip already installed skip to point-4)
•	cd to the directory form cmd in which get-pip.py is saved.
•	Write: python get-pip.py
•	Write: pip install "link of that package"

How to run the code:
After successfully installing all the libraries, put all files related to the project into one directory. And run using following command:
USAGE:
> python main.py 
After this command user will enter:
•	starting_URL: Website URL from where the crawling starts.
•	directory_name: Folder where queue.txt and crawled.txt will be placed.
•	no_of_threads: The maximum number of threads you want to use. Value may range from 1 to n. where n is the capacity of your system to making threads.

Main Sketch:
Web crawler will follow the following steps to crawl a 
web URL:
1) Parse the required HTML page and find all the strings 
which match a typical "URL" pattern.
2) The first set of URLs are put in a file called 
"queueList.txt".
3) After that, the contents of the queue are pulled out:
a. They are put in a set and the whole process is 
repeated till there are no more URLs.
b. Each of the crawled URLs which belong to 
the same domain name are put in a final file, 
"crawledList.txt".
4) The process is sped up using multithreading.
5) The threads are always in order because we added 
semaphores from the library threading.
