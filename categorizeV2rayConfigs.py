import re
from urllib.parse import urlparse


def base64_safe_decode(original_string: str) -> str:
    import base64
    import binascii
    if original_string.isascii():
        try:
            decoded_bytes = base64.b64decode(original_string)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except binascii.Error:
            pass
    return original_string


SCHEMES = ["vmess", "vless", "trojan", "ss", "ws", "socks5"]


def categorize_v2ray_configs(file_path):
    with open(file_path, "r", encoding="UTF-8") as file:
        configs = file.readlines()

    categorized_configs = {
            "vmess": set(),
            "vless": set(),
            "trojan": set(),
            "shadowsocks": set(),
            "http": set(),
            "socks": set(),
            "unknown": set(),
    }

    for config in configs:
        if not any(c in str(config) for c in [".html", "hysteria", "hiddify"]):
            try:
                uri = urlparse(config)
                config = str(config).strip().split("#")[0] + "#AmirHDevo:GitHub"
                if uri.scheme == "vmess":
                    categorized_configs["vmess"].add(config)
                elif uri.scheme == "vless":
                    categorized_configs["vless"].add(config)
                elif uri.scheme == "trojan":
                    categorized_configs["trojan"].add(config)
                elif uri.scheme == "ss":
                    categorized_configs["shadowsocks"].add(config)
                elif uri.scheme == "ws":
                    categorized_configs["http"].add(config)
                elif uri.scheme == "socks5":
                    categorized_configs["socks"].add(config)
                else:
                    print(f"unknown config : {config}")
                    categorized_configs["unknown"].add(config)
            except Exception as e:
                print(f"Error processing config: {e}")
        else:
            print(f"bad config: {config}")
    return categorized_configs


def pri():
    categorized_configs = categorize_v2ray_configs(file_path="./configs.txt")

    # Access categorized configurations
    vmess_configs = categorized_configs["vmess"]
    vless_configs = categorized_configs["vless"]
    trojan_configs = categorized_configs["trojan"]
    shadowsocks_configs = categorized_configs["shadowsocks"]
    http_configs = categorized_configs["http"]
    socks_configs = categorized_configs["socks"]
    unknown_configs = categorized_configs["unknown"]
    # Print variables and their lengths
    print("vmess_configs:", len(vmess_configs))
    print("vless_configs:", len(vless_configs))
    print("trojan_configs:", len(trojan_configs))
    print("shadowsocks_configs:", len(shadowsocks_configs))
    print("http_configs:", len(http_configs))
    print("socks_configs:", len(socks_configs))
    print("unknown_configs:", len(unknown_configs))
    import json

    # Assuming categorized_configs is a dictionary with keys 'vmess', 'vless', etc.
    categorized_configs = {
            "vmess": vmess_configs,
            "vless": vless_configs,
            "trojan": trojan_configs,
            "shadowsocks": shadowsocks_configs,
            "http": http_configs,
            "socks": socks_configs,

    }
    # Create a dictionary to store the data
    data = {}
    # Iterate over each category and create the required structure
    for category, config_list in categorized_configs.items():
        data[category] = {
                "config": [
                        {"index": i, "value": value} for i, value in enumerate(config_list)
                ],
        }
    # Save the data to a JSON file
    with open("configurations.json", "w") as json_file:
        json.dump(data, json_file, indent=2)
    total = 0
    with open("configurations.txt", "w", encoding="utf-8") as txt_file:
        for category_data in data.values():
            config_list = category_data.get("config", [])
            for item in config_list:
                value = item.get("value", "")
                txt_file.write(f"{value}\n")
                total += 1

    print(f"Data saved to configurations.json total :{total}")


pri()
