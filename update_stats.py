import os
import time

def get_stats():
    # Use the 'dumpsys' or 'termux-battery' logic indirectly
    # This command is usually allowed even when psutil is blocked
    try:
        # We grab the battery info directly from the termux-api bridge
        raw_batt = os.popen('termux-battery-status').read()
        if '"percentage"' in raw_batt:
            # Simple way to find the number without heavy libraries
            percent = raw_batt.split('"percentage": ')[1].split(',')[0]
            temp = raw_batt.split('"temperature": ')[1].split(',')[0]
            # Convert decimal temp (27.5) to clean display
            display_temp = f"{temp}°C"
            display_batt = f"{percent}%"
        else:
            display_batt = "Wait..."
            display_temp = "Wait..."
    except:
        display_batt = "Locked"
        display_temp = "Locked"

    return f"""
    <p><strong>Battery Level:</strong> {display_batt}</p>
    <p><strong>Thermal Reading:</strong> {display_temp}</p>
    <p><strong>Node Status:</strong> ONLINE</p>
    <p><small>Uptime: {time.strftime('%H:%M:%S')}</small></p>
    """

while True:
    with open("stats.html", "w") as f:
        f.write(get_stats())
    time.sleep(10)
