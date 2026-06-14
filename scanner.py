import httpx

SECURITY_HEADERS = {
    "Strict-Transport-Security":
        "Protects against SSL stripping",

    "Content-Security-Policy":
        "Prevents XSS attacks",

    "X-Frame-Options":
        "Protects against clickjacking",

    "X-Content-Type-Options":
        "Prevents MIME sniffing",

    "Referrer-Policy":
        "Controls referrer information",

    "Permissions-Policy":
        "Restricts browser features"
}

HIGH_RISK = [
    "Content-Security-Policy",
    "Strict-Transport-Security"
]

MEDIUM_RISK = [
    "X-Frame-Options",
    "X-Content-Type-Options"
]


def scan_headers(url):
    try:
        response = httpx.get(
            url,
            timeout=10,
            follow_redirects=True
        )

        headers = response.headers

        print(f"\nScanning: {url}")
        print("=" * 50)

        score = 0
        total = len(SECURITY_HEADERS)

        for header, description in SECURITY_HEADERS.items():

            if header in headers:
                print(f"[+] {header}: {headers[header]}")
                score += 1

            else:
                if header in HIGH_RISK:
                    print(f"[HIGH RISK] Missing: {header}")

                elif header in MEDIUM_RISK:
                    print(f"[MEDIUM RISK] Missing: {header}")

                else:
                    print(f"[LOW RISK] Missing: {header}")

        percentage = (score / total) * 100

        print("\nAudit Score")
        print("=" * 50)
        print(f"{score}/{total}")
        print(f"{percentage:.1f}%")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    target = input("Enter URL: ")
    scan_headers(target)
