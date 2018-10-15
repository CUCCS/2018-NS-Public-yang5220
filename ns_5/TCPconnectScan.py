#! /user/bin/python
# based on three-way handshark
 
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import*

dst_ip="192.168.94.4"
# generate a random number
src_port=RandShort()
dst_port=80

# sr1 work om layer 3 and only receive the first pakage
# flags="S" SYN "AR" ACK+RST

tcp_connect_scan_resp=sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)
if(str(type(tcp_connect_scan_resp))=="<type'NoneType'>"):
    print "Closed"
elif(tcp_connect_scan_resp.haslayer(TCP)):
    if (tcp_connect_scan_resp.getlayer(TCP).flags==0x12):#falgs==0x12:SYN ACK
        # receive ACK and SYN, send the RST+ACK
        send_rst=sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=10)
        print"Open"
    elif(tcp_connect_scan_resp.getlayer(TCP).flags==0x14):#flags==0x14:RST ACK
        print"Closed"



