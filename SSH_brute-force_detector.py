import re
from datetime import datetime, timedelta
from collections import defaultdict

# === Configuration ===
LOG_FILE = 'sample_auth.log'       # Change to '/var/log/auth.log' on real testing
THRESHOLD = 5                     # Failed attempts to trigger alert
TIME_WINDOW = timedelta(minutes=1) # Time window for attempts

log_pattern = re.compile(
    r'(?P<month>\w+)\s+(?P<day>\d+)\s(?P<time>\d+:\d+:\d+).*Failed password.*from (?P<ip>\d+\.\d+\.\d+\.\d+)'
)

def parse_datetime(month, day, time_str):
    year = datetime.now().year
    dt_str = f"{month} {day} {year} {time_str}"
    return datetime.strptime(dt_str, "%b %d %Y %H:%M:%S")

failed_logins = defaultdict(list)

def main():
    with open(LOG_FILE, 'r') as f:
        for line in f:
            match = log_pattern.search(line)
            if match:
                dt = parse_datetime(match['month'], match['day'], match['time'])
                ip = match['ip']
                failed_logins[ip].append(dt)

    print("🔍 Detected Brute-force Attempts:")

    for ip, times in failed_logins.items():
        times.sort()
        start_idx = 0
        for end_idx in range(len(times)):
            while times[end_idx] - times[start_idx] > TIME_WINDOW:
                start_idx += 1
            if (end_idx - start_idx + 1) >= THRESHOLD:
                print(f"⚠️ Brute-force detected from IP {ip}")
                print(f"  Attempts: {end_idx - start_idx + 1}")
                print(f"  Time window: {times[start_idx]} to {times[end_idx]}")
                break

if __name__ == "__main__":
    main()
