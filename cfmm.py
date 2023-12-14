import re
import requests

from bs4 import BeautifulSoup


def get_soup(url: str):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'html.parser')
        else:
            return None
    except Exception as ex:
        print("Error getting url:", url, "Error:", ex)
        return None


def get_post_links(url: str):
    soup = get_soup(url)
    if soup:
        entries_list = soup.find_all(class_='entry-title')
        return [entry.find('a')['href'] for entry in entries_list
                if entry.find('a')['href'].endswith('vpn.html')]
    else:
        print(f"Failed to fetch the page. url : {url}")


def clean_string(input_string, repl=''):
    return re.sub(r'[^\x00-\x7F]+', repl, input_string)


def get_subscription_links(url: str) -> dict:
    soup = get_soup(url)
    if soup:
        entity = soup.find(class_='cm-comment')
        subscriptions = [clean_string(e.text, repl="*") for e in entity.find("div").find_all("div")]
        return {
                'v2ray': subscriptions[0].split('*')[-1],
                'clash.meta': subscriptions[1].split('*')[-1],
                'clash': subscriptions[2].split('*')[-1],
                'sing-box': subscriptions[3].split('*')[-1],
        }
    else:
        print(f"Failed to fetch the page. url : {url}")
        return {}


def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        dict1.setdefault(key, []).append(value)
    return dict1


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


def get_subscription_results():
    url = 'https://www.cfmem.com/'

    # this dict is contained the subscription links of each category
    subscription_categories = {
            'v2ray': [], 'clash.meta': [], 'clash': [], 'sing-box': [],
    }

    for i, lk in enumerate(get_post_links(url)):
        print(i, "working on " + lk)
        subscription_categories = merge_dicts(subscription_categories, get_subscription_links(lk))
        print("-" * 100)

    print(*subscription_categories.items(), sep="\n")
    # this dict is contained the config links of each category
    subscription_results = {}
    print("-" * 100)

    for cat, subscriptions in subscription_categories.items():
        configs = []
        for sub in subscriptions:
            configs.append(base64_safe_decode(requests.get(url=sub).text))
        print(f"subscription {cat} add {len(configs)} configs")
        subscription_results[cat] = configs

    print(*subscription_results.items(), sep="\n")
    return subscription_results


get_subscription_results()
