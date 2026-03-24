#!/usr/bin/env python3
"""
Monitor Flask app logs in real-time
"""

import time
import subprocess
import sys

def monitor_logs():
    print("Monitoring Flask logs...")
    print("Try sending a chat message now.")
    print("Press Ctrl+C to stop monitoring.")
    print("="*50)
    
    try:
        # Start the Flask app with output capture
        process = subprocess.Popen(
            [sys.executable, 'app.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        
        while True:
            output = process.stdout.readline()
            if output:
                print(f"[LOG] {output.strip()}")
            
            # Check if process ended
            if process.poll() is not None:
                break
                
    except KeyboardInterrupt:
        print("\nStopping monitor...")
        process.terminate()

if __name__ == "__main__":
    monitor_logs()
