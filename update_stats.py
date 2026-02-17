import time

def get_basic_stats():
    # We use ONLY the time and a hardcoded status
    # This avoids touching ANY restricted Android files
    current_time = time.strftime('%H:%M:%S')
    current_date = time.strftime('%Y-%m-%d')
    
    return f"""
    <div style='text-align: center; border: 1px solid #00ff88; padding: 10px;'>
        <p><strong>LAB STATUS:</strong> <span style='color: #00ff88;'>ONLINE</span></p>
        <p><strong>NODE:</strong> Moto G15 Power</p>
        <p><strong>TIME:</strong> {current_time}</p>
        <p><small>Last Pulse: {current_date}</small></p>
    </div>
    """

print("MotoFluff Engine: Starting Minimal Mode...")

while True:
    try:
        content = get_basic_stats()
        with open("stats.html", "w") as f:
            f.write(content)
        time.sleep(10)
    except Exception as e:
        # If even writing a file fails, we'll know here
        print(f"File Error: {e}")
        time.sleep(30)
