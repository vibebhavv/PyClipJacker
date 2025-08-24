
# PyclipJacker
A Python-based clipboard clipper (**PyClipJacker**) demo that showcases how clipboard contents can be monitored and replaced.
The example focuses on cryptocurrency wallet addresses, where the tool automatically detects a copied crypto address and replaces it with a predefined one.

This project is intended to raise awareness about clipboard hijacking attacks and help students/researchers understand how attackers might exploit clipboard monitoring.

## Features
- Monitors system clipboard in real-time.
- Detects cryptocurrency addresses using regex patterns.
- Replaces detected addresses with a predefined demo address.
- Easily extendable for other patterns and formats.

## Requirements

- Python 3.x
- pyperclip (for clipboard access)
- re (regex module, comes built-in with Python)

## Installation
```bash
    pip install pyperclip
    git clone https://github.com/vibebhavv/PyClipJacker
    cd PyClipJacker
```

## Usage

Run the script:

`python3 main.py`

Copy any text containing a **crypto wallet address** (e.g., Bitcoin, Litecoin, Monero).

The script will detect it.

The copied address will be replaced with the demo address defined in the script.

## Example

You copy: `**1BoatSLRHtKNngkdXEeobR76b53LETtpyT**`

Clipboard changes to: `**1DemoFakeAddressABCDE1234567890xyz**`

## Educational Value

This project helps illustrate:
- How malware can monitor clipboard activity.
- Why users should double-check crypto addresses before making transactions.
- The importance of endpoint security and anti-malware tools.

## Defensive Measures

To stay safe from real-world clipboard hijacking attacks:

- Always verify pasted crypto addresses before sending funds.
- Use hardware wallets where possible.
- Keep your system updated with anti-malware tools.

## Disclaimer

This tool is for education, awareness, and security research only.
The author does not condone malicious use.
Use responsibly.
