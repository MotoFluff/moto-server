import psutil
import time

def get_classic_stats():
    # Attempting Battery - This usually works on Moto G series
    try:
        batt = psutil.sensors_battery()
        batt_percent = f"{batt.percent}%" if batt else "N/A"
    except:
        batt_percent = "Access Denied"

    # Attempting Temp - Using your specific 2.7 -> 27 degree fix
    try:
        temps = psutil.sensors_temperatures()
        if 'battery' in temps:
            raw_temp = temps['battery'][0].current
            # Glitch fix: if it says 2.7, make it 27
            temp_display = f"{raw_temp * 10 if raw_temp < 10 else raw_temp}°C"
        else:
            temp_display = "N/A"
    except:
        temp_display = "Protected"

    return f"""
    <p><strong>Battery:</strong> {batt_percent}</p>
    <p><strong>Temperature:</strong> {temp_display}</p>
    <p><small>Updated: {time.strftime('%H:%M:%S')}</small></p>
    """

print("Reverting to Classic Mode...")
while True:
    try:
        content = get_classic_stats()
        with open("stats.html", "w") as f:
            f.write(content)
        time.sleep(10)
    except:
        time.sleep(10)
