# WiFiQRGenerator
Apart from being able to join a WiFi network selected from a list and by entering its password manually, this programs allows a user to generate a QR Code of any WiFi network as long as its credentials are present. Easily shareable with friends and family or customers over a business.

## Installation:
```bash
pip install pyqrcode
```

## Usage:
```bash
python3 wifi_qr.py
```

```python
import pyqrcode
import sys

SSID: <Network SSID>
Password: <Password>
<WPA/WPA2>

#Resulting QR Code is saved to local directory as <SSID>.png
```
