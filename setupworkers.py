# setupworkers.py
# SOURCES:
# Environment variables: https://www.twilio.com/blog/environment-variables-python
# Popen: https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-script-from-another-script
import os
from subprocess import Popen
from dotenv import load_dotenv

try:
    load_dotenv()
    workerdata = os.environ.get("WORKERS").split(" ")

    print(workerdata)

    if workerdata is None:
        print("Couldn't get worker data from the environment variable, exiting..")
        exit(0)
    else:
        for data in workerdata:
            name = data.split("-")[0]
            port = data.split("-")[1]
            Popen("python worker.py " + name + " " + str(port))

except Exception as ex:
    print("Error loading dotenv, exiting..")
    print(str(ex))
    exit(0)