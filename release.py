import sys
import os
from metadata import VERSION

versioning={"major": 0,"minor": 1,"patch": 2}
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
bump=sys.argv[1] if n > 1 else "patch"
here = os.path.abspath(os.path.dirname(__file__))
print(here,VERSION)
version = VERSION.split('.')
version[versioning.get(bump,2)]=int(version[versioning.get(bump,2)]) + 1
version='.'.join(map(str, version))
print(f"VERSION :{version}")
newline=f"VERSION = '{version}'"
filelines=None
with open(os.path.join(here, "metadata.py"),'r',encoding="utf-8") as file:
     filelines = file.readlines()
     file.seek(0)
with open(os.path.join(here, "metadata.py"),'w',encoding="utf-8") as file:
    for line in filelines:
        if "VERSION" not in line:
            file.write(line)
    file.write(newline)

     
     