# pico-field-controller main.py (draft)
# Role: RS-485 master, poll components, cache state, talk to Pi over USB

import time
import sys

# TODO: import machine, set up UART0 for RS485 transceiver, etc.

STATE_TABLE = {}  # { "03": { "MAINS":0, "BACKUP":1, ... , "LAST":"timestamp" }, ... }

COMPONENT_IDS = ["03"]  # temp hardcode until discovery exists

def poll_component(cid):
    # send "cid,00,STATE?,\n" over RS485 UART
    # wait reply
    # parse and update STATE_TABLE[cid]
    pass  # TODO

def handle_usb_command(line):
    line = line.strip()

    if line == "GET ALL":
        for cid, data in STATE_TABLE.items():
            # build response line
            out = [
                f"ID={cid}",
                f"MAINS={data.get('MAINS','?')}",
                f"BACKUP={data.get('BACKUP','?')}",
                f"ALARM={data.get('ALARM','?')}",
                f"BATT={data.get('BATT','?')}",
                f"LAST={data.get('LAST','?')}",
            ]
            print(";".join(out))
        print("END")
        return

    if line.startswith("CMD "):
        # Example: CMD ID=03,SILENCE
        # parse target ID and command, send RS485 command,
        # wait for ack, print "ACK ID=03,SILENCE=1"
        pass  # TODO

while True:
    # 1. Poll components on a schedule
    for cid in COMPONENT_IDS:
        poll_component(cid)

    # 2. Check USB stdin for Pi commands
    # (Pi 4 will write to /dev/ttyACM0, which becomes stdin/stdout here)
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        cmd = sys.stdin.readline()
        handle_usb_command(cmd)

    # 3. Decide if alarm LED/buzzer should be on
    # (any ALARM=1 or BACKUP=1 triggers local alert output pin)
    # TODO

    time.sleep(0.1)
