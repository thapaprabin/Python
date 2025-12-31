import gc 
print("== Before garbage collection ==")
print(f"GC enabled :{gc.isenabled}")
print(f"Garbage found:{len(gc.garbage)}")

#creating a cycle 
class cycle:
    def __init__(self,name):
        self.name=name
        self.other=None
    def __del__(self):
        print(f"Deleted:{self.name}")
x=cycle("X")
y=cycle("Y")
x.other=y
y.other=x

x=y=None
print("Garbage collection running..")
print("Running gc.collect()")
collected=gc.collect()
print(f"Collected {collected} objects")