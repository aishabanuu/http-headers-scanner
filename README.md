# HTTP Headers Scanner

A Python-based HTTP Security Header Scanner that checks websites for missing security headers and generates a simple security assessment score.

## Features

- Scan any website URL
- Detect common security headers
- Display header values
- Categorize missing headers by risk level
- Generate an overall security score
- Lightweight and beginner-friendly

## Security Headers Checked

| Header | Purpose |
|----------|----------|
| Strict-Transport-Security | Prevents SSL stripping attacks |
| Content-Security-Policy | Helps prevent XSS attacks |
| X-Frame-Options | Protects against clickjacking |
| X-Content-Type-Options | Prevents MIME sniffing |
| Referrer-Policy | Controls referrer information |
| Permissions-Policy | Restricts browser features |

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/http-headers-scanner.git
cd http-headers-scanner
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run:

```bash
python3 scanner.py
```

Enter a target URL:

```text
Enter URL: https://github.com
```

## Project Structure

```text
http-headers-scanner/
│
├── scanner.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── examples/
│   ├── sample-output.txt
│   └── screenshot.png
│
└── reports/
```

## Skills Demonstrated

- Python Programming
- HTTP Protocol Fundamentals
- Security Header Analysis
- Error Handling
- Risk Classification
- Security Auditing

## Future Improvements

- Export reports to JSON
- Export reports to HTML
- Scan multiple URLs
- Async scanning using httpx.AsyncClient
- Security grading system (A-F)
- Command-line arguments support

## Disclaimer

This project is intended for educational and defensive security purposes only.
