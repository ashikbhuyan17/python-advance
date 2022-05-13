from os import PRIO_PGRP


subjects =["c","c++","java","python"]
print(subjects[0]) 
print(subjects[2:]) 
print(subjects[-1]) 
print("python" in subjects)
print("swift" in subjects)
print(subjects + ["dart"])

subjects.append("toc")
print("append",subjects)

subjects.insert(2,"doc")
print("insert position",subjects)


subjects.remove("c++")
print("remove",subjects)


subjects.sort()
print("sort",subjects)

pos = subjects.index("c++")
print("positon",pos)