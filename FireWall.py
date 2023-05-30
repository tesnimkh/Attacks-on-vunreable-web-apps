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
    default_limits=["500 per day", "50 per hour"]
)


@app.route("/")
def home():
    return "<h1>Welcome to the Web Application Firewall Demo!</h1>"


@app.before_request
def firewall():
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


if __name__ == "__main__":
    app.run()
