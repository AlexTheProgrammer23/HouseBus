# System Architecture

## High level

Housebus is built from three logical layers:

1. Components
   - Individually addressable modules on an RS-485 bus
   - Example: a hallway emergency light that turns on during an outage

2. Hub Baseboard
   - Custom PCB that holds:
     - Raspberry Pi Pico (Field Controller)
     - RS-485 transceiver + RJ45 HouseBus port
     - Power distribution and switchover logic
     - Buzzer + LED + Silence button
   - Optional: Raspberry Pi 4 header for the Supervisor

3. Supervisor (Raspberry Pi 4)
   - Talks to the Pico over USB serial
   - Logs events
   - Provides HDMI dashboard (local status map)
   - Bridges data into Home Assistant / MQTT

## Data flow

Component <-> (RS-485) <-> Pico (Field Controller)
Pico <-> (USB Serial) <-> Pi 4 Supervisor
Pi 4 -> MQTT / dashboard / logging

## Design goals

- Survive power loss
- Announce emergencies locally (buzzer, LED) even if Pi 4 crashes
- Work without the internet
- Stay modular and cheap to extend
