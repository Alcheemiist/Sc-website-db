
import os

directory = "./data-transform/"

list_dirs = list_dirs= os.listdir(directory)

for file in list_dirs:
    with open(directory+file, "r") as f:
        lines = f.read()
        
    for line in lines:
        if "\t" in line:
            line = lines.replace("\t", " ")
    
    with open(directory+file, "w") as f:
        f.write(line)
    print("Done with file: " + file)