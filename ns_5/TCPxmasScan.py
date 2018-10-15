import logging 
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import*

dst_ip="192.168.94.4"
src_port=RandShort()
dst_port=80

xmas_scan_resp=sr1(IP(dst=dst_ip)/TCP(dport=dst_port,flags="FPU"),timeout=10)
if(str(type(xmas_scan_resp))=="<type 'NoneType'>"):
    print"reruen null Open|Filtered"
elif(xmas_scan_resp.haslayer(TCP)):
    if(xmas_scan_resp.getlayer(TCP).flags==0x14):# flags:RST ACK
        print"return RST Closed"
elif(xmas_scan_resp.haslayer(ICMP)):
    if(int(xmas_scan_resp.getlayer(ICMP).type)==3 and int(xmas_scan_resp.getlayer(ICMP).code in [1,2,3,9,10,13])):
        print"return icmp.type=3 Filtered"

