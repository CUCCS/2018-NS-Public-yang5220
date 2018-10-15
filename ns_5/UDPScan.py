import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import*

dst_ip="192.168.94.4"
src_port=RandShort()
#dst_port=68
dst_port=9999
dst_timeout=10

def udp_scan(dst_ip,dst_port,dst_timeout):
    udp_scan_resp=sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout)
    if(str(type(udp_scan_resp))=="<type 'NoneType'>"):# the state is unsure
        retrans=[]
        # scan 3 times to sure the state of the port
        for count in range(0,3):
            retrans.append(sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout))
        for item in retrans:
            if(str(type(item))!="<type 'NoneType'>"):
                udp_scan(dst_ip,dst_port,dst_timeout)
        return "Open|Filtered"
    elif(udp_scan_resp.haslayer(UDP)):
        return "Open"
    elif(udp_scan_resp.haslayer(ICMP)):
        if(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code)==3):
            return "Closed"
        elif(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code) in [1,2,9,10,13]):
            return "Filtered"
print( dst_port,udp_scan(dst_ip,dst_port,dst_timeout))
