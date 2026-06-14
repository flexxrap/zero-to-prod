import platform
import socket
import time

from fastapi import FastAPI, Request, Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

app = FastAPI(title="Zero to Prod Demo App")

START_TIME = time.time()

REQUEST_COUNT = Counter(
    "http_requests_total", "Total HTTP requests", ["method", "path", "status"]
)
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds", "Request latency in seconds", ["method", "path"]
)


@app.middleware("http")
async def track_metrics(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    path = request.url.path
    REQUEST_LATENCY.labels(request.method, path).observe(time.time() - start)
    REQUEST_COUNT.labels(request.method, path, response.status_code).inc()
    return response


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.get("/api/info")
def info():
    return {
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "uptime_seconds": round(time.time() - START_TIME, 2),
    }
