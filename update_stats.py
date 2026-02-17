import psutil
import time
import os

def get_android_stats():
    # Battery is usually accessible without root
    batt = psutil.sensors_battery()
    percent = batt.percent if batt else "N/A"
    
    # We use time and uptime instead of restricted CPU files
    current_time = time.strftime('%H:%M:%S')
    
    return f"""
    <p><strong>NODE STATUS:</strong> ACTIVE</p>
    <p><strong>Power Level:</strong> {percent}%</p>
    <p><strong>System Time:</strong> {current_time}</p>
    <p><small>Last Pulse: {time.strftime('%Y-%m-%d')}</small></p>
    """

print("MotoFluff Engine: Running in Permission-Safe Mode")

while True:
    try:
        content = get_android_stats()
        with open("stats.html", "w") as f:
            f.write(content)
        # We wait 10 seconds to be gentle on the battery
        time.sleep(10)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(60)
