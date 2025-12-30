import sys
print("++ Circular reference example ++")

class Node:
    def __init__(self,name) -> None:
        self.name=name
        self.friend=None
        print(f"Created Node : {self.name}")
    def __del__(self):
        print(f"Deleted Node : {self.name}")    
print("== NO CYCLES EXAMPLE ==")   
a=Node("Samyak") 
b=Node("Sharvin")

print("Creating a cyclic friendship ")
jajbin=Node("Jajbin")
jenish=Node("Jenish")
shreedha=Node("Shreedha")

#cycle 
jajbin.friend=jenish
jenish.friend=shreedha
shreedha.friend=jajbin

print("-- REFERENCE COUNT --")
print(f"Reference count if jajbin : {sys.getrefcount(jajbin)-1}")
print(f"Reference count if jenish : {sys.getrefcount(jenish)-1}")
print(f"Reference count if shreedha : {sys.getrefcount(shreedha)-1}")

jajbin =None
jenish=None
shreedha = None

#using garbage collector for removing cycle 
import gc 
print(f" Garbage collector called : {gc.collect}") 
