import os
from scapy.all import sniff, wrpcap, Raw, IP, TCP


sniff(filter="ip src https://d.weibo.com/", iface="Realtek PCIe GBE Family Controller", prn=lambda x:x, count=10)


