import requests
from bs4 import BeautifulSoup
#
# url = "https://t.me/s/TVCminer"
#
# # Send a GET request to the URL
# response = requests.get(url)
#
# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content of the page
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     # Save the HTML content to a file
#     with open("webpage_content.html", "w", encoding="utf-8") as file:
#         file.write(str(soup))
#     print("Webpage content saved successfully.")
# else:
#     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
from workRequestsChannel import strip_non_ascii

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
     # "v2Rinjector"
     ]
for ch in s:
    print(f"https://t.me/s/{ch}")
# bad :"freeclashyaml",
