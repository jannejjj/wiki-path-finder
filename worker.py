from xmlrpc.server import SimpleXMLRPCServer
import sys

name = sys.argv[1]
port = sys.argv[2]

server = SimpleXMLRPCServer(("localhost", int(port)))
print(name + " starting...")

api_url = "https://en.wikipedia.org/w/api.php"


def find_links(page):
    print(name + " looking for links on page " + page)

    params = {
        "action": "parse",
        "page": page,
        "format": "json",
        "prop": "links",
    }
    try:
        json = requests.get(url=api_url, params=params).json()
        links = json["parse"]["links"]

        pages = []
        for link in links:
            pages.append(link["*"])
        return pages
    except Exception as ex:
        print("Error while trying to get links: " + str(ex))
        return False


print(sys.argv[1] + " started.")
server.register_function(find_links, "find_links")
try:
    server.serve_forever()
except Exception as ex:
    print("Serve_forever exception")



