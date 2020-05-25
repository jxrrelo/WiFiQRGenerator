import pyqrcode
import sys


def network_details():
    ssid = input("SSID:")
    password = input("Password:")
    protocol = 'WPA/WPA2'

    qr = pyqrcode.create(F'WIFI:S:{ssid};T:{protocol};P:{password};;')
    generate_qr(qr, ssid)


def generate_qr(qr, ssid):
    filename = ssid + '.png'
    qr.png(filename, scale=5)
    print("QR Code saved as %s" % (filename))


if __name__ == "__main__":
    network_details()
