
import psutil
import platform
import socket
import os


# CPU metrics
def get_cpu():
    return {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "cpu_cores": psutil.cpu_count()
    }


# Memory metrics
def get_memory():
    memory = psutil.virtual_memory()

    return {
        "total_gb": round(memory.total / (1024**3), 2),
        "used_gb": round(memory.used / (1024**3), 2),
        "available_gb": round(memory.available / (1024**3), 2),
        "percentage": memory.percent
    }


# Disk metrics
def get_disk():
    disk = psutil.disk_usage(os.path.abspath(os.sep))

    return {
        "total_gb": round(disk.total / (1024**3), 2),
        "used_gb": round(disk.used / (1024**3), 2),
        "free_gb": round(disk.free / (1024**3), 2),
        "percentage": disk.percent
    }


# Battery metrics
def get_battery():
    battery = psutil.sensors_battery()

    if battery is None:
        return {"message": "Battery information unavailable"}

    return {
        "percentage": battery.percent,
        "plugged_in": battery.power_plugged
    }


# Network metrics
def get_network():
    network = psutil.net_io_counters()

    return {
        "bytes_sent": network.bytes_sent,
        "bytes_received": network.bytes_recv
    }


# System information
def get_system():
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_release": platform.release(),
        "processor": platform.processor(),
        "architecture": platform.machine()
    }


# All system metrics
def get_system_details():
    return {
        "cpu": get_cpu(),
        "memory": get_memory(),
        "disk": get_disk(),
        "battery": get_battery(),
        "network": get_network(),
        "system": get_system()
    }
