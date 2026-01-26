import psutil
import time 

def simple_monitor():
    print("Memory Monitor ")
    print("-"* 50)
    

    try:
        while True:
            mem=psutil.virtual_memory()
            print(f"\rUsed: {mem.percent:5.1f}% | "
      f"Available: {mem.available//(1024**2):8,} MB | "
      f"Total: {mem.total//(1024**3):4} GB", end="", flush=True)
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n\n STOPPED ")
if __name__=="__main__":
    simple_monitor()