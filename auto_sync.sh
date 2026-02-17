#!/bin/bash
while true
do
  # Force add the files to ensure they are tracked
  git add index.html stats.html update_stats.py auto_sync.sh
  git commit -m "Moto G15 Telemetry Update"
  git push origin main
  echo "Data sent to GitHub. Cooling down..."
  sleep 30
done

