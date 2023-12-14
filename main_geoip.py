import geoip2.database
import wget

#
url = 'https://git.io/GeoLite2-Country.mmdb'
filename = 'geoip-lite-country.mmdb'
wget.download(url, filename)

mmdb_path = filename

print("oi po")  # Open the MaxMind database
with geoip2.database.Reader(mmdb_path) as reader:
    #     # Replace '8.8.8.8' with the IP address you want to look up
    #     ip_address = '8.8.8.8'
    #     response = reader.city(ip_address)
    #
    #     # Access location information
    print(f'IP: ')
#     print(f'Country: {response.country.name}')
#     print(f'City: {response.city.name}')
#     print(f'Latitude: {response.location.latitude}')
#     print(f'Longitude: {response.location.longitude}')
