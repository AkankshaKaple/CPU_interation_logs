import json
from flask import Flask
from flask import request
import csv

app = Flask(__name__)


@app.route('/data', methods=['GET'])
def datashow():
    import csv
    with open('CpuLogData.csv', 'rt')as f:
        data = csv.reader(f)
        row1 = []
        for row in data:
            row1.append(row)
    return row1


@app.route('/', methods=['GET'])
def abc():
    return """
    <pre>
    sudo apt install python-pip;pip install psutil;pip install requests;
    </pre>
    <pre>
    
    
import psutil as ps
import datetime
import json
import requests
import os

log_values = [('Datetime', 'now'),
              ('cpu_count', ''),
              ('cpu_times', 'user'),
              ('cpu_times', 'idle'),
              ('cpu_percent', ''),
              ('Process', 'cpu_affinity'),
              ('cpu_stats', 'soft_interrupts'),
              ('cpu_stats', 'syscalls'),
              ('cpu_stats', 'interrupts'),
              # ('cpu_freq', 'current'),
              # ('cpu_freq', 'min'),
              # ('cpu_freq', 'max'),
              ('getloadavg', ''),
              ('virtual_memory', 'total'),
              ('virtual_memory', 'used'),
              ('virtual_memory', 'free'),
              ('virtual_memory', 'active'),
              ('virtual_memory', 'inactive'),
              ('virtual_memory', 'buffers'),
              ('virtual_memory', 'cached'),
              ('virtual_memory', 'shared'),
              ('virtual_memory', 'available'),
              ('disk_usage', 'total'),
              ('disk_usage', 'used'),
              ('disk_usage', 'free'),
              ('disk_io_counters', 'read_count'),
              ('disk_io_counters', 'write_count'),
              ('disk_io_counters', 'read_bytes'),
              ('disk_io_counters', 'write_bytes'),
              ('disk_io_counters', 'read_time'),
              ('disk_io_counters', 'write_time'),
              ('disk_io_counters', 'busy_time'),
              ('net_io_counters', 'bytes_sent'),
              ('net_io_counters', 'bytes_recv'),
              ('net_io_counters', 'packets_sent'),
              ('net_io_counters', 'packets_recv'),
              ('net_io_counters', 'errin'),
              ('net_io_counters', 'errout'),
              ('net_io_counters', 'dropin'),
              ('net_io_counters', 'dropout'),
              ('boot_time', ''),
              ('users', 'name')

              ]
log_data_lists = []
for function in log_values:
    if function[0] == 'Datetime':
        log_data_lists.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    elif function[0] == 'disk_usage':
        function_value = "ps." + function[0] + "('/')." + function[1]
        log_data_lists.append(eval(function_value))
    elif function[0] == 'users':
        function_value = "ps." + function[0] + "()[0]." + function[1]
        log_data_lists.append(eval(function_value))
    elif function[0] == 'boot_time':
        log_data_lists.append(str(-(datetime.datetime.fromtimestamp(ps.boot_time()) - datetime.datetime.now())))
    elif function[0] == 'Process':
        function_value = "len(ps." + function[0] + "()." + function[1] + "())"
        log_data_lists.append(eval(function_value))
    elif function[0] == 'getloadavg':
        function_value = "os." + function[0] + "()"
        for value in range(len(eval(function_value))):
            log_data_lists.append(eval(function_value)[value])
    elif len(function[1]):
        function_value = "ps." + function[0] + "()." + function[1]
        log_data_lists.append(eval(function_value))
    else:
        function_value = "ps." + function[0] + "()"
        log_data_lists.append(eval(function_value))
log_file_key_value = ['DateTime',
                      'Cpu Count',
                      'Cpu Working Time',
                      'Cpu idle Time',
                      'cpu_percent',
                      'Usage Cpu Count ',
                      'number of software interrupts since boot',
                      'number of system calls since boot',
                      'number of interrupts since boot',
                      # 'CPU frequency_current',
                      # 'CPU frequency_min',
                      # 'CPU frequency_max',
                      'cpu avg load over 1 min',
                      'cpu avg load over 5 min',
                      'cpu avg load over 15 min',
                      'system_total_memory',
                      'system_used_memory',
                      'system_free_memory',
                      'system_active_memory',
                      'system_inactive_memory',
                      'system_buffers_memory',
                      'system_cached_memory',
                      'system_shared_memory',
                      'system_avalible_memory',
                      'disk_total_memory',
                      'disk_used_memory',
                      'disk_free_memory',
                      'disk_read_count',
                      'disk_write_count',
                      'disk_read_bytes',
                      'disk_write_bytes',
                      'time spent reading from disk',
                      'time spent writing to disk',
                      'time spent doing actual I/Os',
                      'number of bytes sent',
                      'number of bytes received',
                      'number of packets sent',
                      'number of packets recived',
                      'total number of errors while receiving',
                      'total number of errors while sending',
                      'total number of incoming packets which were dropped',
                      'total number of outgoing packets which were dropped',
                      'boot_time',
                      'user_name', 'keyboard', 'mouse']
log_json = {}
for value in range(len(log_data_lists)):
    log_json.update({log_file_key_value[value]: log_data_lists[value]})

temp = {}

data_json = (json.dumps(log_json))
url = "http://192.168.0.38"

path = url + "/save_logs"
PARAMS = {'cpu_log': data_json}
r = requests.post(path, data=PARAMS)
</pre>    """


@app.route('/save_logs', methods=['POST'])
def save_logs():
    cpu_log = (request.form['cpu_log'])
    data_keys = ['DateTime', 'Cpu Count', 'Cpu Working Time', 'Cpu idle Time', 'cpu_percent', 'Usage Cpu Count ', 'number of software interrupts since boot', 'number of system calls since boot', 'number of interrupts since boot', 'cpu avg load over 1 min', 'cpu avg load over 5 min', 'cpu avg load over 15 min', 'system_total_memory', 'system_used_memory', 'system_free_memory', 'system_active_memory', 'system_inactive_memory', 'system_buffers_memory', 'system_cached_memory', 'system_shared_memory', 'system_avalible_memory', 'disk_total_memory', 'disk_used_memory', 'disk_free_memory', 'disk_read_count', 'disk_write_count', 'disk_read_bytes', 'disk_write_bytes', 'time spent reading from disk', 'time spent writing to disk', 'time spent doing actual I/Os', 'number of bytes sent', 'number of bytes received', 'number of packets sent', 'number of packets recived', 'total number of errors while receiving', 'total number of errors while sending', 'total number of incoming packets which were dropped', 'total number of outgoing packets which were dropped', 'boot_time', 'user_name', 'keyboard', 'mouse']
    data = json.loads(cpu_log)
    temp = []
    for value in data_keys:
        temp.append(data[value])
    print(temp)
    data = list(data.values())
    with open("CpuLogData.csv", "a") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(temp)
    return cpu_log


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
