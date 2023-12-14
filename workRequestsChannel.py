import json
import requests
from bs4 import BeautifulSoup

from categorizeV2rayConfigs import pri

s = ["PrivateVPNs",
     "forwardv2ray",
     "VlessConfig",
     "v2raycollector",

     # "PROXYKAAM",
     "Charismatics_channel",
     # "TVCminer",
     # "freeclashyaml",
     # "PROXYKAAM",

     "daemi100",
     "FreeVPNHomes",
     "AliAlma_GSM",
     "V2rayCollectorDonate",
     "v2ray_npv",
     # "Outline_Vpn",
     "v2rayng_org",
     "free_v2rayyy",
     "VlessConfig",
     "DirectVPN",
     "ProxyDaemiOutline",
     "Rnrifci",
     "inikotesla",
     "Mi_PN_Official",
     "proxyforopeta",
     "foxrayiran",
     "iP_CF",
     "reality_daily",
     "Vpnplatform",
     "BigSmoke_Config",
     "vpn_315",
     "nim_ping",
     "AlienVPN402",
     "MTConfig",
     # "v2Rinjector",
     "enjecto",
     "DeamNet_proxy",
     "MehradLearn",
     "httpproxygo",
     "MARAMBASHI",
     "DailyV2RY",
     "PHOENIXVPN_Official",
     "frev2ray",
     "Xvproxy",
     "VmessProtocol",
     "NPV_V2RAY",
     "VPNAMOHELP",
     "Vemessvpn", "proxyymeliii", "iran_v2raying", "AstroVPN_IR",
     "komak_onlinevpn", "helovpn", "servergod2", "VrayHub",
     "v2rayng_anti", "Garnet_Free", "GGv2ray", "Antifilterjadid",
     "Magicvpn_shop", "saveproxy", "v2ray_napster_vpn",
     "MiracleV2ray", "filter_A", "v2rayAri", "v2ray31",
     "asr_proxy", "v2rayMB", "ProxyMY2", "CloudCityy",
     "CUSTOMVPNSERVER", "FreeVpn1302", "zen_cloud", "ten10vpn",
     "v2rayng_napesternetv", "v2ray_hub1", "Nim_TorNet",
     "VPNFolder", "vpn_xw", "VPNGate_Channel", "IRTEACH2",
     "vmess_vless_pro", "vless_vmess", "vmessiran", "ForUvpn",
     ]


def strip_non_ascii(input_string: str, repl=''):
    import string
    cleaned_string = ''.join(char if char.isascii() and char in string.printable else repl for char in input_string)
    return cleaned_string


def load_json(path: str) -> set:
    try:
        with open(path, "r") as file:
            return set(json.load(file))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        # Handle specific exceptions (FileNotFoundError, JSONDecodeError)
        print(f"Error loading JSON from {path}: {e}")
        return set()


def fetch_last_messages(channel_link) -> list:
    try:

        response = requests.get(channel_link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            div_messages = soup.find_all("code")
            return [div.text.strip() for div in div_messages if len(div.text.strip()) > 20]
    except Exception as exc:
        print("error fetching :", exc)
        return []


def main():
    total_configs = 0
    for i, ch in enumerate(s):  # load_json(r"ch.json")):
        last_messages = fetch_last_messages(f"https://t.me/s/{ch}")
        print("-" * 100)
        print(f"get last messages from: https://t.me/s/{ch}")
        last_messages_num = len(last_messages)
        print(i, f"#last_messages  is : {last_messages_num}")
        with open("configs.txt", "w" if i == 0 else "a", encoding="utf-8") as f:

            for message in last_messages:
                f.write(message + '\n')
                print(message)
        total_configs += last_messages_num
    print(f"total  is : {total_configs}")


if __name__ == "__main__":
    main()
    print("*" * 100)

    pri()
