from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

# Mock data
mock_stats = {
    "networksCount": 5,
    "devicesCount": 12,
    "bandwidthUsed": 123.45,
    "blockedCount": 2
}

mock_networks = [
    {"ssid": "HomeNetwork", "bssid": "00:1B:63:84:45:E6", "signal": -50, "security": "WPA2"},
    {"ssid": "OfficeGuest", "bssid": "00:1B:63:84:45:E7", "signal": -65, "security": "WPA2"},
    {"ssid": "PublicWiFi", "bssid": "00:1B:63:84:45:E8", "signal": -75, "security": "OPEN"},
]

mock_devices = [
    {"ip": "192.168.1.10", "mac": "A0:B1:C2:D3:E4:F5", "vendor": "Apple, Inc."},
    {"ip": "192.168.1.12", "mac": "A0:B1:C2:D3:E4:F6", "vendor": "Samsung Electronics"},
]

@app.route('/api/stats', methods=['GET'])
def get_stats():
    return jsonify(mock_stats)

@app.route('/api/networks', methods=['GET'])
def get_networks():
    return jsonify(mock_networks)

@app.route('/api/devices', methods=['GET'])
def get_devices():
    return jsonify(mock_devices)

@app.route('/api/scan/start', methods=['POST'])
def start_scan():
    return jsonify({"message": "Scan started"}), 200

@app.route('/api/scan/stop', methods=['POST'])
def stop_scan():
    return jsonify({"message": "Scan stopped"}), 200

@app.route('/api/scan/single', methods=['POST'])
def single_scan():
    return jsonify({"message": "Single scan completed"}), 200

@app.route('/api/export', methods=['GET'])
def export_data():
    return jsonify({"message": "Exporting data"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
