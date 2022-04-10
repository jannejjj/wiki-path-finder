# main.py
# SOURCES:
# Tree: https://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python
# Threading: https://realpython.com/intro-to-python-threading/
import xmlrpc.client
from dotenv import load_dotenv
import os
import random
import threading
import time
import concurrent.futures

load_dotenv()

workerdata = os.environ.get("WORKERS").split(" ")
ports = []
for worker in workerdata:
    ports.append(worker.split("-")[1])

# Start each worker, looks horrible I know
worker_1 = xmlrpc.client.ServerProxy("http://localhost:" + ports[0])
worker_2 = xmlrpc.client.ServerProxy("http://localhost:" + ports[1])
worker_3 = xmlrpc.client.ServerProxy("http://localhost:" + ports[2])
worker_4 = xmlrpc.client.ServerProxy("http://localhost:" + ports[3])
worker_5 = xmlrpc.client.ServerProxy("http://localhost:" + ports[4])
worker_6 = xmlrpc.client.ServerProxy("http://localhost:" + ports[5])
worker_7 = xmlrpc.client.ServerProxy("http://localhost:" + ports[6])
worker_8 = xmlrpc.client.ServerProxy("http://localhost:" + ports[7])
worker_9 = xmlrpc.client.ServerProxy("http://localhost:" + ports[8])
worker_10 = xmlrpc.client.ServerProxy("http://localhost:" + ports[9])
worker_11 = xmlrpc.client.ServerProxy("http://localhost:" + ports[10])
worker_12 = xmlrpc.client.ServerProxy("http://localhost:" + ports[11])
worker_13 = xmlrpc.client.ServerProxy("http://localhost:" + ports[12])
worker_14 = xmlrpc.client.ServerProxy("http://localhost:" + ports[13])
worker_15 = xmlrpc.client.ServerProxy("http://localhost:" + ports[14])
worker_16 = xmlrpc.client.ServerProxy("http://localhost:" + ports[15])
worker_17 = xmlrpc.client.ServerProxy("http://localhost:" + ports[16])
worker_18 = xmlrpc.client.ServerProxy("http://localhost:" + ports[17])
worker_19 = xmlrpc.client.ServerProxy("http://localhost:" + ports[18])
worker_20 = xmlrpc.client.ServerProxy("http://localhost:" + ports[19])
worker_21 = xmlrpc.client.ServerProxy("http://localhost:" + ports[20])
worker_22 = xmlrpc.client.ServerProxy("http://localhost:" + ports[21])
worker_23 = xmlrpc.client.ServerProxy("http://localhost:" + ports[22])
worker_24 = xmlrpc.client.ServerProxy("http://localhost:" + ports[23])
worker_25 = xmlrpc.client.ServerProxy("http://localhost:" + ports[24])
worker_26 = xmlrpc.client.ServerProxy("http://localhost:" + ports[25])
worker_27 = xmlrpc.client.ServerProxy("http://localhost:" + ports[26])
worker_28 = xmlrpc.client.ServerProxy("http://localhost:" + ports[27])
worker_29 = xmlrpc.client.ServerProxy("http://localhost:" + ports[28])
worker_30 = xmlrpc.client.ServerProxy("http://localhost:" + ports[29])
worker_31 = xmlrpc.client.ServerProxy("http://localhost:" + ports[30])
worker_32 = xmlrpc.client.ServerProxy("http://localhost:" + ports[31])
worker_33 = xmlrpc.client.ServerProxy("http://localhost:" + ports[32])
worker_34 = xmlrpc.client.ServerProxy("http://localhost:" + ports[33])
worker_35 = xmlrpc.client.ServerProxy("http://localhost:" + ports[34])
worker_36 = xmlrpc.client.ServerProxy("http://localhost:" + ports[35])
worker_37 = xmlrpc.client.ServerProxy("http://localhost:" + ports[36])
worker_38 = xmlrpc.client.ServerProxy("http://localhost:" + ports[37])
worker_39 = xmlrpc.client.ServerProxy("http://localhost:" + ports[38])
worker_40 = xmlrpc.client.ServerProxy("http://localhost:" + ports[39])
workers = [worker_1, worker_2, worker_3, worker_4, worker_5,
           worker_6, worker_7, worker_8, worker_9, worker_10,
           worker_11, worker_12, worker_13, worker_14, worker_15,
           worker_16, worker_17, worker_18, worker_19, worker_20,
           worker_21, worker_22, worker_23, worker_24, worker_25,
           worker_26, worker_27, worker_28, worker_29, worker_30,
           worker_31, worker_32, worker_33, worker_34, worker_35,
           worker_36, worker_37, worker_38, worker_39, worker_40]


# Define tree
class Node:
    def __init__(self, title, depth):
        self.parent = None
        self.depth = depth
        self.title = title
        self.checked = False


# Get user input
startpage = input("Enter starting page (type 'exit' to exit) : ")
endpage = input("Enter ending page (type 'exit' to exit): ")

if (startpage == "exit") or (endpage == "exit"):
    print("Thank you for using the program.")
    exit(0)

# Initialize tree with starting page
start = Node(startpage, 0)
start.checked = True
links = [start]

# Get links from the starting page
startpage_links = worker_1.find_links(startpage)

# Add startpage links to tree
for link in startpage_links:
    if ("Category:" not in link)\
            and ("Wikipedia:" not in link)\
            and ("Template:" not in link)\
            and ("Template talk:" not in link)\
            and ("Help:" not in link):

        if link == endpage:
            links.append("FOUND")

        node = Node(link, 1)
        node.parent = start
        links.append(node)


def handle_exit():
    end = Node
    for l in links:
        if type(l) == str:
            continue
        elif l.title == endpage:
            end = l
            break

    end_depth = end.depth
    route = []
    cur = end
    while cur is not None:
        parent = cur.parent
        route.append(cur)
        cur = parent

    print(f'\nStarted from {startpage} and found page {endpage} at depth {end_depth}.')
    print("The route was:")
    for i in reversed(route):
        print(i.title)
    print("Thank you for using the program.")
    exit(0)


def filter_link(string):
    if ("Template:" in string) or ("Help:" in string) or ("Category:" in string) or ("Wikipedia:" in string):
        return True
    else:
        return False


def search_link(link_to_be_searched, worker_to_be_used, depth):

    res = worker_to_be_used.find_links(link_to_be_searched.title)
    if not res:  # This happens when a page contains a link to another page that doesn't exist yet
        exit(0)
    else:
        for item in res:
            # If page is not a category link etc
            if not filter_link(item):
                if item == endpage:
                    links.append("FOUND")
                new_depth = depth+1
                new_item = Node(item, new_depth)
                new_item.parent = link_to_be_searched
                links.append(new_item)

        exit(0)


working_list = []
working_list_titles = []
depth_of_search = 0
print("Searching...")
while True:

    if "FOUND" in links:
        handle_exit()
        break

    if len(working_list) == 0:
        if depth_of_search != 0:
            print("Increasing depth of search...")
        depth_of_search += 1
        for link in links:
            if (link.depth == depth_of_search) and (link.title not in working_list_titles):
                working_list.append(link)
                working_list_titles.append(link.title)

    for worker in workers:
        if len(working_list) == 0:
            break

        link = random.choice(working_list)
        if not link.checked:
            working_list.remove(link)
            working_list_titles.remove(link.title)
            link.checked = True
            t = threading.Thread(target=search_link, args=(link, worker, depth_of_search))
            t.start()
            # To prevent trying to request a worker that's busy
            time.sleep(0.09)
