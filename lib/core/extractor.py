
import os
import sys

def extractthe_mac(file_path="extracted.txt"):

    with open(file_path, "r") as file: 
        payload = file.read() 
        rows = payload.split("\n") 
        sorted_rows = sorted(rows) 
        sorted_payload = "\n".join(sorted_rows) 
        return sorted_payload.split("\n")


