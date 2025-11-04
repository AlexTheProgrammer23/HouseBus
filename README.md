[![Shopify](https://img.shields.io/badge/Go_to-Shopify_Store-brightgreen)](housenet.store)

# HouseBus

HouseBus is an open hardware + open firmware platform for resilient, local-first home infrastructure.

## What it does

- Detects loss of power and automatically switches critical loads (like emergency lights) to backup.
- Keeps devices talking to each other over a wired RS-485 bus called HouseBus.
- Exposes status, alarms, and sensor data to a central Hub that can show it on an HDMI screen, send alerts to Home Assistant, and log events — all without needing the cloud or the internet.

## Why this exists

Most “smart home” gear dies the second power or Wi-Fi drops.
Housebus is meant to:
- keep emergency loads alive,
- coordinate them,
- and report what’s happening,
even when the rest of the house is dark.

The system is meant to be safe, cheap, modifiable, and installable by normal humans.

## Core pieces

### 1. Hub Baseboard
The Hub Baseboard is the brain carrier that will host:
- a Raspberry Pi 4 (Supervisor: UI, logging, Home Assistant bridge, HDMI output)
- a Raspberry Pi Pico (Field Controller: real-time polling, alarm control, RS-485 bus master)
- power entry + switchover
- RJ45 HouseBus connector

The Hub Baseboard is responsible for:
- talking to every device on the bus
- sounding a local alarm / indicator if something is in emergency mode
- telling the Pi 4 what's going on so it can display and log it

### 2. Components
A "Component" is any module on the HouseBus that does a job(s).
Planned Components:
- Powerfail Light (turns on emergency lighting when main power is gone)
- Sensor Node (reports temperature / humidity / air quality)
- Relay Node (remotely switch loads)
- Door/Window Sense Node (reports open/closed)

Each Component:
- has a unique ID
- connects over RS-485 (A/B/GND)
- responds to simple text commands like `STATE?`
- can generate an alarm (for example, “backup lighting active in hallway”)

### 3. HouseBus
HouseBus is a multi-drop RS-485 bus with power distribution.
RJ45 pinout (not Ethernet)                                                                                                                                                                       1: 1:RS485_A  
2: RS485_B  
3: GND

The Raspberry Pi Pico is the bus master. It polls all Components and caches their status.

The Raspberry Pi 4 asks the Pico for a summary and pushes it to Home Assistant / dashboard.

## Repo layout

- `hardware/` → Schematics, PCBs, BOMs for Hub and Components.
- `firmware/` → Code for the Pico Field Controller, the Pi 4 Supervisor, and reference Component firmwares.
- `docs/` → Protocol, roadmap, and system architecture.

## Status / timeline

- [ ] Hub Baseboard Rev A schematic
- [ ] Hub Baseboard Rev A PCB layout
- [ ] Pico polling firmware skeleton
- [ ] Pi 4 supervisor script with USB serial + MQTT
- [ ] Powerfail Light Component Rev A schematic
- [ ] Public first test report

This project is currently in virtual design / simulation.
No production hardware exists yet.

## Status (v0.1 Prototype)  
- Hub Baseboard Rev A: design in progress  
- Firmware: Pico skeleton ready  

## License

MIT License. See `LICENSE`.
Hardware is released under the same terms unless noted in that folder.
