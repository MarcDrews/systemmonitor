import json
import logging
from monitor import get_cpu_usage, get_ram_usage, get_disk_usage, get_network_stats, log_and_print


class Jsonformatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'time': self.formatTime(record),
            'level': record.levelname,
            "message": record.getMessage(),
            "label": getattr(record, "label", None),
            "value": getattr(record, "value", None),
            "unit": getattr(record, "unit", None),
            }
        return json.dumps(log_record)

log_file = '/home/drew/python-projects/systemmonitor/logs/systemmonitor.log'

handler = logging.FileHandler(log_file)

handler.setFormatter(Jsonformatter())

logging.basicConfig( 
    level=logging.INFO,
    handlers=[handler])

def main():
    logging.info("System Monitor Started")
    cpu= get_cpu_usage()
    ram= get_ram_usage()
    disk= get_disk_usage()
    net_in, net_out= get_network_stats()

    log_and_print("CPU Usage", cpu, "%")
    log_and_print("RAM Usage", ram, "%")
    log_and_print("Disk Usage", disk, "%")
    log_and_print("Network Received", f"{net_in:.2f}", " GB")
    log_and_print("Network Sent", f"{net_out:.2f}", " GB")

    logging.info("System Monitor Finished")


if __name__ == "__main__":
    main()



"""logging.basicConfig(
    filename='/home/drew/python-projects/systemmonitor/logs/systemmonitor.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s')
"""

""" def main():
    logging.info("System Monitor Started")
    cpu = get_cpu_usage()
    print(f"CPU Usage: {cpu}%")
    logging.info(f"CPU Usage: {cpu}")
    ram = get_ram_usage()
    print(f"RAM Usage: {ram}%")
    logging.info(f"RAM Usage: {ram}")
   logging.info("System Monitor Finished")
"""
# bytes_recv = psutil.net_io_counters().bytes_recv

#gb_recv = bytes_recv / (1024 ** 3)

#bytes_sent = psutil.net_io_counters().bytes_sent

#gb_sent = bytes_sent / (1024 ** 3)

#logging.info(f"CPU Usage: {psutil.cpu_percent()}")
#logging.info(f"RAM Usage: {psutil.virtual_memory().percent}")
#logging.info(f"Disk Usage:{psutil.disk_usage('/').percent}")
#logging.info(f"Network Stats: {psutil.net_io_counters()}")
#logging.info(f"Bytes Received: {bytes_recv} ({gb_recv:.2f} GB)")
#logging.info(f"Bytes Sent: {bytes_sent} ({gb_sent:.2f} GB)")