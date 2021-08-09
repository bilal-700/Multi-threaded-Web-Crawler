# Multi-threaded-Web-Crawler
To crawl web content using Python

## System:
- Linux-Ubuntu (preferred)
- Windows

## Language:
- python3

## For installing Libraries: 
- **Linux-Ubuntu:**
  - `sudo apt install python3-pip`  (if pip not installed)
  - `python3 -m pip install requests`

- **Windows:**
  -	Download get-pip.py  (if pip already installed skip to point-4)
  -	cd to the directory form cmd in which get-pip.py is saved.
  -	Write: `python get-pip.py`
  -	Write: `pip install "link of that package"`

## How to run the code:
After successfully installing all libraries, put all files related to the project into one directory
& run using command:
- `python main.py` 

After this command user have to enter few things like:
-	starting_URL: Website URL from where the crawling starts.
-	directory_name: Folder where queue.txt and crawled.txt will be placed.
-	no_of_threads: The maximum number of threads you want to use. Value may range from 1 to n. where n is the capacity of your system to make threads.

## Main Sketch:
Web crawler will follow the following steps to crawl a 
web URL:
- Parse the required HTML page and find all the strings 
which match a typical "URL" pattern.
- The first set of URLs are put in a file called 
"queueList.txt".
- After that, the contents of the queue are pulled out:
  - They are put in a set and the whole process is 
  repeated till there are no more URLs.
  - Each of the crawled URLs which belong to 
  the same domain name are put in a final file, 
  "crawledList.txt".
- The process is sped up using multithreading.

## Overview of the project: 
<p align="center">
  <img src="https://user-images.githubusercontent.com/84318717/128780058-979d5589-0076-49d6-8762-d6161ab28477.png" width="550" height="300">
</p>

