# Day 01 - Enhanced TCP Port Scanner

## Overview

This project is part of the **30 Days of Cybersecurity Automation** challenge by VIEH Group.

The objective was to build a simple TCP Port Scanner using Python and Socket Programming. After running the original implementation, I enhanced the scanner by adding service detection, banner grabbing support, and exporting scan results to a text file.

## Features

### Original Features

* Fast TCP port scanning
* Custom target support
* Detects open ports
* Beginner-friendly implementation
* Lightweight and easy to use

### Enhancements Added

* Service detection for common ports
* Basic banner grabbing
* Export scan results to a text file
* Improved output readability

## Technologies Used

* Python
* Socket Programming

## Original Implementation

The original scanner checks a target host for open TCP ports within a specified port range.

### Original Scanner Execution

![Original Scanner](screenshots/scanner.py%20output.png)

The original scanner successfully detected open ports on the target system.

## Enhanced Implementation

The enhanced version includes:

### Service Detection

Identifies common services associated with open ports.

Examples:

* 21 → FTP
* 22 → SSH
* 80 → HTTP
* 443 → HTTPS

### Banner Grabbing

Attempts to retrieve banner information from open services.

### Export Results

Automatically saves discovered open ports and services to a text file.

### Enhanced Scanner Execution

![Enhanced Scanner](screenshots/scannerversion2.py%20output.png)

The enhanced scanner displays detected services and exports scan results to a file.

## Installation

```bash
git clone <repository-url>
cd Day-01-Port-Scanner
```

## Usage

Run the enhanced scanner:

```bash
python scannerversion2.py
```

Enter:

* Target IP or Domain
* Start Port
* End Port

Example:

```text
Enter Target IP/Domain: scanme.nmap.org
Enter Start Port: 1
Enter End Port: 100
```

## Sample Output

```text
Scanning Target: scanme.nmap.org
----------------------------------------
[+] Port 80 is OPEN (HTTP)

Scan Completed.
Results saved in scan_results.txt
```

## Learning Outcomes

Through this project I learned:

* Socket Programming Basics
* TCP Communication
* Port Scanning Concepts
* Network Enumeration Fundamentals
* Service Detection
* Basic Banner Grabbing
* File Handling in Python


## Disclaimer

This project is intended for educational purposes and authorized security testing only.


30 Days of Cybersecurity Automation - Day 01
