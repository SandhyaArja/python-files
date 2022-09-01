import os

# Get the current working
# directory (CWD)
#cwd = os.getcwd()
def current():
    print(os.getcwd())
current()
os.chdir("../")
current()

# Print the current working
# directory (CWD)
#print("Current working directory:", cwd)