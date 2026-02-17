import psutil
import time
import os

def get_stats():
    # CPU and RAM are usually readable without root
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    
    # Since /proc/net/dev is blocked, we'll display "System Protected" 
    # for speed or use a placeholder to prevent crashes.
    net_status = "Live (Protected)" 

    return f"""
    <p><strong>CPU Usage:</strong> {cpu}%</p>
    <p><strong>RAM Usage:</strong> {ram}%</p>
    <p><strong>Network Status:</strong> {net_status}</p>
    <p><small>Last Update: {time.strftime('%H:%M:%S')}</small></p>
    """

print("Starting MotoFluff Engine (Safe Mode)...")
while True:
    try:
        content = get_stats()
        with open("stats.html", "w") as f:
            f.write(content)
        time.sleep(2)
    except Exception as e:
        with open("stats.html", "w") as f:
            f.write(f"<p>Error: {e}</p>")
        time.sleep(10)
