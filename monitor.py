import psutil

def get_cpu_usage():
    return psutil.cpu_percent()

def get_ram_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

def get_network_stats():
    counters = psutil.net_io_counters()
    gb_recv = counters.bytes_recv / (1024 ** 3)
    gb_sent = counters.bytes_sent / (1024 ** 3)
    return gb_recv, gb_sent

def log_and_print(label,value,unit=""):
    import logging
    message=f"{label}"
    print(message)
    logging.info(message, extra={"label": label, "value": value, "unit": unit})