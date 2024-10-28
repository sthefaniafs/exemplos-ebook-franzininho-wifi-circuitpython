import time
import ipaddress
import wifi
import socketpool
import ssl

ssid="suaRedeWiFi"
passwd="suaSenha"

print('Hello World!')

for network in wifi.radio.start_scanning_networks():
    print(network, network.ssid, network.channel)
wifi.radio.stop_scanning_networks()

print("joining network...")
print(wifi.radio.connect(ssid=ssid,password=passwd))
# the above gives "ConnectionError: Unknown failure" if ssid/passwd is wrong

print("my IP addr:", wifi.radio.ipv4_address)

print("pinging 1.1.1.1...")
ip1 = ipaddress.ip_address("1.1.1.1")
print("ip1:",ip1)
print("ping:", wifi.radio.ping(ip1))


while True:
    print("Conectado")
    time.sleep(1)

