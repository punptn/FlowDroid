import os

dir_path = r'/Users/ppunnun/Documents/GitHub/FlowDroid/LeakReports'
print(len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))]))