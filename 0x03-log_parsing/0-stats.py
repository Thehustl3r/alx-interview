#!/usr/bin/python3
"""0-stas"""
import sys
import re


count = 0
data = {'ip': '',
        'date': '',
        'request': '',
        'status': 0,
        'size': 0}
data_list = []
status_arr = ['200', '301', '400', '401', '403', '404', '405', '500']
try:
    for line in sys.stdin:
        line.strip()
        if count == 10:
            sorted_list = sorted(data_list, key=lambda x: x['status'])
            total_size = sum(item['size'] for item in sorted_list)
            print(f"File size: {total_size}")
            # for data in data_list:
            #     print(data)
            for stat in status_arr:
                count = sum(1 for item in data_list if item['status'] == stat)
                if count != 0:
                    print(f"{stat}: {count}")
            data_list = []
            count = 0

        # print(line)
        log = line.split()
        # print(len(log))

        if len(log) == 9:
            data = {
                'ip': log[0],
                'date': log[2],
                'request': log[3] + log[4],
                'status': log[7],
                'size': int(log[8]),
            }
            data_list.append(data)
        count += 1

except KeyboardInterrupt:
    sorted_list = sorted(data_list, key=lambda x: x['status'])
    total_size = sum(item['size'] for item in sorted_list)
    print(f"File size: {total_size}")
    for stat in status_arr:
        count = sum(1 for item in data_list if item['status'] == stat)
        if count != 0:
            print(f"{stat}: {count}")
    sys.exit()
