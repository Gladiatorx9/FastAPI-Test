
from fastapi import FastAPI

from system_file import (
    get_cpu,
    get_memory,
    get_disk,
    get_battery,
    get_network,
    get_system,
    get_system_details
)

app = FastAPI(
    title="System Monitoring API",
    description="API for monitoring system health and resource utilization",
    version="1.0.0"
)


# Health check
@app.get("/")
def home():
    return {"message": "System Monitoring API is running"}


# All metrics
@app.get("/metrics")
def metrics():
    return get_system_details()


# CPU metrics
@app.get("/cpu")
def cpu():
    return get_cpu()


# Memory metrics
@app.get("/memory")
def memory():
    return get_memory()


# Disk metrics
@app.get("/disk")
def disk():
    return get_disk()


# Battery metrics
@app.get("/battery")
def battery():
    return get_battery()


# Network metrics
@app.get("/network")
def network():
    return get_network()


# System information
@app.get("/system")
def system():
    return get_system()
