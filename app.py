from flask import Flask, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# 📊 Metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total HTTP Requests')
FAILED_REQUESTS = Counter('app_failed_requests_total', 'Failed Requests')
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency')

# 🛡️ Security metric (very important for your project)
LOGIN_ATTEMPTS = Counter('app_login_attempts_total', 'Login attempts')

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Secure DevSecOps Pipeline Running!"

@app.route("/login")
def login():
    LOGIN_ATTEMPTS.inc()
    user = request.args.get("user")

    # simulate failed login
    if user != "admin":
        FAILED_REQUESTS.inc()
        return "Unauthorized", 401

    return "Welcome Admin"

from flask import Response

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
