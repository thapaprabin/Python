import sys
print("== AUTOMATIC CLEANUP EXAMPLE ==")

#we define a class 
class TrackDeletion:
    def __init__(self,name):
        self.name = name
        print(f" Created :{self.name}")
    def __del__(self):
        print(f"Deleted:{self.name}")

print("\n created and deleted immediately ")
TrackDeletion("Temporary name")

print("\n 2. Keeping object alive by using a variable ")
obj = TrackDeletion("Prabin")
print("The object still remains..")

print("EXAMPLE 3. Multiple references ")
obj1 = TrackDeletion("Shared object ")
obj2 = obj1
print(f"Reference count is :{sys.getrefcount(obj1)}")
del obj1 #obj1 deleted but its reference remains
del obj2 # no reference remains

def create_temp():
    temp=TrackDeletion("Function Object ")
create_temp()
print("Function returned and object deleted")
#If we had a reference to create_temp() 
#it would not be deleted.for eg :func=create_temp()

#WHY: for immediate cleanup closed file 