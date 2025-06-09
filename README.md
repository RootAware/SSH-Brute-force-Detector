# SSH Brute-force Detector

A lightweight Python script designed to detect SSH brute-force attacks by analyzing Linux SSH authentication logs. This tool helps SOC analysts and system administrators identify suspicious IP addresses attempting repeated failed logins within a short time frame.

---

## Features

- Parses SSH authentication logs (e.g., `/var/log/auth.log` or custom log files).
- Detects IP addresses with multiple failed login attempts within a configurable time window.
- Outputs clear alerts with details including IP address, number of attempts, and time range.
- Easy to configure and extend.

---

## Requirements

- Python 3.6 or higher

---

## Setup & Usage

1. **Download or clone the repository:**

```bash
git clone https://github.com/yourusername/ssh-bruteforce-detector.git
cd ssh-bruteforce-detector
```

2. **How It works:**

- The script reads the SSH authentication log file line by line.
- It uses a regular expression to identify lines indicating failed SSH login attempts and extract the IP address and timestamp.
- For each IP, it keeps track of all failed login attempt times.
- It then scans these timestamps to detect if the number of failed attempts exceeds a configurable threshold within a set time window (default: 5 attempts in 1 minute).
- When such a pattern is detected, it prints an alert with the IP address, number of attempts, and the relevant time period.

This method helps detect brute-force attack patterns by focusing on rapid repeated failures from the same IP.



