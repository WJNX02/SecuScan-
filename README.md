# SecuScan

**SecuScan** is a Python tool designed to scan a list of domains for the presence of a `security.txt` file. The `security.txt` file is commonly used by websites to provide contact information for security researchers, helping them to responsibly disclose security issues.


## Features

- Checks for `security.txt` at standard locations: 
- `https://domain.com/.well-known/security.txt` 
- `https://domain.com/security.txt` 
- Logs results for each domain, indicating if the file was found, not found, or if the URL is unavailable. 
- Saves output to a results file named `scan_results_YYYY-MM-DD.txt` with the current date.

## Requirements
- Python 3.x 
- `requests` library
You can install the `requests` library by running: 
`bash pip install requests`

## Usage

1. Place your domains in `domains.txt`, one per line.
2. Run the script:
    `python main.py` 
3. The tool will generate a result file (e.g., `scan_results_2024-11-14.txt`) with the scan output.

## Example
For domain.txt list like:
`example.com testsite.com`

The output in `scan_results_YYYY-MM-DD.txt` will look like:
`example.com: Found at https://example.com/.well-known/security.txt`
`testsite.com: No security.txt found`

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

## License
This project is open-source and available under the MIT License.

## Open a file
For more information or to check out more projects, visit [WJNX](https://wjnx.nl).

