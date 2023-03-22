import os

# Specify the directory to search in
directory = "/Users/ppunnun/Documents/GitHub/FlowDroid/LeakReports"

count = 0
# Loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"): # Change this to the file extension you want to search
        # Open the file and search for the word "location"
        with open(os.path.join(directory, filename), "r") as f:
            if "location" in f.read():
                print(filename)
                count = count + 1
        
print("Total number of applications that location info is leaked =", count)