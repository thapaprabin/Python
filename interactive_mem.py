#!/usr/bin/env python3
import psutil
import time
from datetime import datetime

def safe_memory_monitor():
    """Memory monitor that won't crash"""
    print("🖥️  MAC MEMORY MONITOR")
    print("=" * 50)
    print("Updates every second. Press Ctrl+C to stop\n")
    
    check_count = 0
    
    try:
        while True:
            check_count += 1
            
            try:
                # Get memory info
                memory = psutil.virtual_memory()
                
                # Get swap memory
                swap = psutil.swap_memory()
                
                # Get current time
                current_time = datetime.now().strftime("%H:%M:%S")
                
                # Display in a nice format
                print(f"[{current_time}] Check #{check_count}")
                print(f"  Memory:    {memory.percent:5.1f}% used")
                print(f"  Available: {memory.available//1024//1024:6} MB")
                print(f"  Total:     {memory.total//1024//1024:6} MB")
                print(f"  Swap:      {swap.percent:5.1f}% used")
                
                # Show warning if memory is high
                if memory.percent > 85:
                    print("  ⚠️  WARNING: High memory usage!")
                elif memory.percent > 75:
                    print("  ⚠️  Warning: Memory usage elevated")
                    
                print("-" * 40)
                
            except Exception as e:
                print(f"Error reading memory: {e}")
                print("Will retry in 2 seconds...")
                time.sleep(2)
                continue
                
            time.sleep(1)
            
    except KeyboardInterrupt:
        print(f"\n\n✅ Monitoring complete!")
        print(f"Total checks: {check_count}")

# Run it immediately
if __name__ == "__main__":
    safe_memory_monitor()