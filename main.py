import requests
from datetime import datetime
from requests.exceptions import ConnectTimeout

# Display WJNX.nl
def display_banner():
    banner = r"""
 __      __  __    _  __   __  _   _  _   _  _   _
 __      __       ____.  _______    ____  ___
/  \    /  \     |    |  \      \   \   \/  /
\   \/\/   /     |    |  /   |   \   \     / 
 \        /  /\__|    | /    |    \  /     \ 
  \__/\  /   \________| \____|__  / /___/\  \
       \/                       \/        \_/

         WJNX.nl Security.txt Scanner
    """
    print(banner)

def load_domains(file_path):
    with open(file_path, 'r') as file:
        domains = [line.strip() for line in file if line.strip()]
    return domains

def check_security_txt(domain):
    urls = [
        f"{domain}/.well-known/security.txt",
        f"{domain}/security.txt"
    ]

    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"Found security.txt for {domain} at {url}")
                return url
        except ConnectTimeout:
            print(f"This URL is no longer available: {url}")
            return "URL no longer available"
        except requests.RequestException as e:
            print(f"Error accessing {url}: {e}")

    print(f"No security.txt found for {domain}")
    return None

def scan_domains(domains):
    results = {}
    for domain in domains:
        print(f"Scanning {domain}...")
        found_url = check_security_txt(domain)
        results[domain] = found_url if found_url else "Not found"
    return results

# Display the WJNX.nl
display_banner()

# Load domains from a text file
domains_to_scan = load_domains("domains.txt")
results = scan_domains(domains_to_scan)

# Generate a filename with the current date
date_str = datetime.now().strftime("%Y-%m-%d")
filename = f"scan_results_{date_str}.txt"

# Save results to the generated filename
with open(filename, "w") as file:
    for domain, status in results.items():
        file.write(f"{domain}: {status}\n")
        print(f"{domain}: {status}")  # Optional: prints each result to the console as well

print(f"Results saved to {filename}")
print(display_banner())