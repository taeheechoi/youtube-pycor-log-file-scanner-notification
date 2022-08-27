# Epicor Automation using Python - Searching specific words or sentences in the large log files and send a notification for findings. 

<!-- ABOUT THE PROJECT -->

## About The Project

This project is for the Youtube channel Pycor where developers can learn how to integrate with Epicor ERP software in Python. 

The intention of this project is to help developers to search specific words or sentences quickly in the large log files generated by heavy process such as MRP in Epicor then send a notification to chat platform for findings.  

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Python 3.10
- Python Packages: requests (2.28.1), Python-dotenv (0.20.0)
- VS Code

### Installation
[YouTube](https://youtu.be/8-LRXVoPPPw)
1. Clone the repo
   ```sh
   git clone https://github.com/taeheechoi/youtube-pycor-log-file-scanner-notification.git .
   ```
2. Create a virtual environment and activate it
   ```sh
   python -m venv venv
   venv\scripts\activate
   ```
3. Install packages
   ```sh
   pip install -r requirements.txt
   ```
4. Rename .env-example to .env and configure it
   ```
   WEBHOOK_URL=Your webhook url
   ```
5. Create log folder for logging results

6. Update run.bat
   ```sh
   C:\project-folder\venv\Scripts\python.exe main.py
   ```
## Acknowledgments

- [Python pathlib](https://docs.python.org/3/library/pathlib.html)
- [Python mmap](https://docs.python.org/3/library/mmap.html)
