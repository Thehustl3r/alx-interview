#!/usr/bin/python3
"""0-stas"""
import sys
import signal


def signal_handler(sig, frame):
    """handle system interupt"""
    print_statistics()
    sys.exit(0)


def print_statistics():
    """print statics"""
    print(f"File size: {total_size}")
    print(f"File size: {total_size}")

    for code in sorted(status_code.keys()):
        print(f"{code}: {status_code[code]}")


line_count = 0
status_code = {}
total_size = 0
# signal.signal(signal.SIGINT, lambda sig, frame: asyncio
# .create_task(signal_handler(sig, frame)))

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line.strip()
        parts = line.split()
        # print(len(parts))

        if len(parts) != 9:
            continue

        status = int(parts[7])
        if status not in [200, 301, 400, 401, 403, 404, 405, 500]:
            continue
        status_code[status] = status_code.get(status, 0) + 1

        total_size += int(parts[8])
        line_count += 1
        if line_count == 10:
            print_statistics()
            line_count = 0

    if line_count !=10:
        print_statistics()

except KeyboardInterrupt:
    # asyncio.run(signal_handler(signal.SIGINT, None))
    signal_handler(signal.SIGINT, None)
