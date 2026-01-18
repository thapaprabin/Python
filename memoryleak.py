print("\n == Memory leak in real life example ==")
class LeakyCache:
    def __init__(self):
        self.cache={}
        self.history=[]
    def process_request(self,user_id,data):
        self.cache[user_id]=data
        self.history.append((user_id,data))
        return f"Processed : {user_id}"
#simulating a server running 
print(" Simulating server running ..")
server=LeakyCache()

print("Processing 1000 requests ..")
for i in range(1000):
    server.process_request(f" User_{i}"," x "*1000)
print(f"Csche size :{len(server.cache)}")
print(f"History size :{len(server.history)}")

#adding cleanup 
print("\n Fixed version ")
class Fixedcache:
    def __init__(self,max_history=100):
        self.cache={}
        self.history=[]
        self.max_history=max_history
    
    def process_request(self,user_id,data):
        self.cache[user_id]=data
        self.history.append((user_id,data))
        if len(self.history) > self.max_history:
            self.history.pop(0)
        return f"Processed {user_id}"

fixed_server=Fixedcache(max_history=10)
for i in range(1000):
    fixed_server.process_request(f"User_{i}","x" *1000)

print(f"Fixed cache history size :{len(fixed_server.history)}")

