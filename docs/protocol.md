# HouseBus Protocol (Draft A)

## Physical layer
- RS-485 half-duplex bus (A/B/GND/shared on RJ45)
- Pico is the bus master

## Frame format (ASCII, human debuggable)

### Poll request from Pico to Component
`<DST>,<SRC>,STATE?,\n`

Example:
`03,00,STATE?,\n`
- `03` = Component ID
- `00` = Hub/Pico ID

### Component reply
`<DST>,<SRC>,STATE,MAINS=0,BACKUP=1,ALARM=1,SILENCE=0,BATT=4.87\n`

Example:
`00,03,STATE,MAINS=0,BACKUP=1,ALARM=1,SILENCE=0,BATT=4.87\n`

Required keys:
- `MAINS`    1 = main power OK, 0 = lost
- `BACKUP`   1 = running in emergency mode
- `ALARM`    1 = local alarm active
- `SILENCE`  1 = alarm locally acknowledged
- `BATT`     backup / bus voltage (or '-' if not applicable)

### Command from Pico to Component
`03,00,SILENCE,\n`

Meaning "acknowledge / hush alarm".

---

## Pico <-> Pi 4 link

The Pi 4 opens the Pico as /dev/ttyACM0 and uses these commands:

- `GET ALL\n`
  Pico responds with one line per Component:
  `ID=03;MAINS=0;BACKUP=1;ALARM=1;BATT=4.87;LAST=2025-10-31T20:14:22Z`
  Ends with:
  `END\n`

- `CMD ID=03,SILENCE\n`
  Pico forwards a SILENCE command to Component 03 and responds with:
  `ACK ID=03,SILENCE=1\n`
