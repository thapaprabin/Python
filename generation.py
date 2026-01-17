print("UNDERSTANDING GENERATIONS:")

import gc 
print("Current Gc thresholds :")
print(f" Generation 0 : {gc.get_threshold()[0]} allocations before colection")
print(f" Generation 1 : {gc.get_threshold()[1]} allocations before colection before gen 1 ")
print(f" Generation 2 : {gc.get_threshold()[2]} allocations before colection before gen 2 ")

#check generation of an object 
print(" Track an object through generations:")

class TrackedObject:
    def __ini__(self, id):
        self.id = id
    def get_generation(self):
        return gc.get_objects()
# forcing collections and see what happens
print(" Force collections at each level :")

survivors=[]
for i in range(1000):
    survivors.append([i]*10)
print(f" Created {len(survivors)}objects ")

#collect generation 0
print("\n Collecting generation 0...")
collected = gc.collect(0)
print(f"Collected :{collected}")

#collect generation 1
print("\n Collecting generation 1...")
collected = gc.collect(1)
print(f"Collected :{collected}")

#collect generation 2
print("\n Collecting generation 2...")
collected = gc.collect(2)
print(f"Collected :{collected}")
#check statistics 
print(" \n GC Statistics : ")
stats = gc.get_stats()
for i, gen_stats in enumerate(stats):
    print(f" Generation {i}:")
    print(f"Collections :{gen_stats['collections']}")
    print(f"Collected :{gen_stats['collected']}")
    print(f"Uncollectable :{gen_stats['uncollectable']}")