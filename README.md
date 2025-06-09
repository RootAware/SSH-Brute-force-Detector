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
