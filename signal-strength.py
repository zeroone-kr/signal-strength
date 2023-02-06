from scapy.all import *
import argparse

class SignalParser():

    def __init__(self):
        self.interface = None
        self.mac = None
        self.i=0

    def parse(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('interface')
        parser.add_argument('mac')
        args = parser.parse_args()
        self.interface = args.interface
        self.mac = args.mac

    def packet_handler(self, pkt) :
        if pkt.haslayer(Dot11):
            if pkt.type == 0 and pkt.subtype == 8 and pkt.addr2 == self.mac:
                print(f"WiFi signal strength: {pkt.dBm_AntSignal}dBm of TA:{pkt.addr2}, ssid: {pkt.info.decode('utf-8')}")

    def start(self):
        self.parse()
        sniff(iface=self.interface, prn = self.packet_handler) 


if __name__ == '__main__':
    sig = SignalParser()
    sig.start()
