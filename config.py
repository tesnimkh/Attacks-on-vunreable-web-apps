from flask import Flask, request, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import re
import json

app = Flask(__name__)

with open("firewall.json", "r") as f:
    firewall_rules = json.load(f)

limiter = Limiter(
    app,
    default_limits=["500 per day", "50 per hour"],
    key_func=get_remote_address  # Use remote IP address as the key for rate limiting
)

@app.before_request
def firewall():
    firewall_ip = "YOUR_FIREWALL_IP_ADDRESS_OR_IP_RANGE"

    for rule in firewall_rules:
        if "regex" in rule and re.search(rule["regex"], request.path):
            app.logger.warning(
                f"Malicious request blocked: {request.remote_addr} - {request.path}"
            )
            abort(403)
        elif "ip_blacklist" in rule and request.remote_addr in rule.get("ip_blacklist", []):
            app.logger.warning(
                f"Blocked request from blacklisted IP: {request.remote_addr} - {request.path}"
            )
            abort(403)
        elif "requests_per_minute" in rule:
            limit = f"{rule['requests_per_minute']} per minute"
            if "ip_whitelist" in rule and request.remote_addr not in rule["ip_whitelist"]:
                continue
            limiter.limit(limit)(request)

    # Apply firewall rules specific to your firewall solution
    # Example for iptables:
    import subprocess
    subprocess.run(["iptables", "-A", "INPUT", "-s", firewall_ip, "-p", "tcp", "--dport", "5000", "-j", "ACCEPT"])

if __name__ == "__main__":
    app.run()
