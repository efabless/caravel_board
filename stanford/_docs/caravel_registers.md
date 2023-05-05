
Documentation for Caravel Management SoC
========================================

Memory Regions
==========

SRAM is implemented in two byte-addressable blocks of synthesized RAM using DFF cells.

| Region         | Address           | Length         |
|----------------|-------------------|----------------|
| dff            | 0x00000000        | 0x00000400     |
| dff2           | 0x00000400        | 0x00000200     |
| flash          | 0x10000000        | 0x01000000     |
| housekeeping   | 0x26000000        | 0x00100000     |
| user project   | 0x30000000        | 0x00300000     |
| vexriscv csr   | 0xf0000000        | 0x00010000     |
| vexriscv debug | 0xf00f0000        | 0x00000100     |

CTRL
====

Register Listing for CTRL
-------------------------

| Register                    | Address                 | C Macro Name      |
|-----------------------------|-------------------------|-------------------|
| CTRL_RESET                  | 0xf0000000              | reg_reset         |
| CTRL_SCRATCH                | 0xf0000004              |
| CTRL_BUS_ERRORS             | 0xf0000008              |

CTRL_RESET


`Address: 0xf0000000 + 0x0 = 0xf0000000`


<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'soc_rst',  'type': 4, 'bits': 1},{'name': 'cpu_rst',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name    | Description                                                            |
|-------|---------|------------------------------------------------------------------------|
| [0]   | SOC_RST | Write 1 to this register to reset the full SoC (Pulse Reset)           |
| [1]   | CPU_RST | Write 1 to this register to reset the CPU(s) of the SoC (Hold Reset)   |

CTRL_SCRATCH


`Address: 0xf0000000 + 0x4 = 0xf0000004`

Use this register as a scratch space to verify that software read/write accesses
to the Wishbone/CSR bus are working correctly. The initial reset value of
0x1234578 can be used to verify endianness.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'scratch[31:0]', 'attr': 'reset: 305419896', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



CTRL_BUS_ERRORS


`Address: 0xf0000000 + 0x8 = 0xf0000008`

Total number of Wishbone bus errors (timeouts) since start.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'bus_errors[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



SPI_MASTER
==========

Register Listing for SPI_MASTER
-------------------------------

| Register                          | Address                   | C Macro Name                   |
|-----------------------------------|---------------------------|--------------------------------|
| SPI_MASTER_CONTROL                | 0xf0004800                | reg_spimaster_control          |
| SPI_MASTER_STATUS                 | 0xf0004804                | reg_spimaster_status           |
| SPI_MASTER_MOSI                   | 0xf0004808                | reg_spimaster_wdata            |
| SPI_MASTER_MISO                   | 0xf000480c                | reg_spimaster_rdata            |
| SPI_MASTER_CS                     | 0xf0004810                | reg_spimaster_cs               |
| SPI_MASTER_LOOPBACK               | 0xf0004814                | reg_spimaster_clk_divider      |
| SPI_MASTER_CLK_DIVIDER            | 0xf0004818                | reg_spi_enable                 |

SPI_MASTER_CONTROL


`Address: 0xf0004800 + 0x0 = 0xf0004800`

SPI Control.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'start',  'type': 4, 'bits': 1},{'bits': 7},{'name': 'length',  'bits': 8},{'bits': 16}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field  | Name   | Description                                     |
|--------|--------|-------------------------------------------------|
| [0]    | START  | SPI Xfer Start (Write 1 to start Xfer).         |
| [15:8] | LENGTH | SPI Xfer Length (in bits).                      |

SPI_MASTER_STATUS


`Address: 0xf0004800 + 0x4 = 0xf0004804`

SPI Status.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'done',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                                 |
|-------|------|---------------------------------------------|
| [0]   | DONE | SPI Xfer Done (when read as 1).             |

SPI_MASTER_MOSI


`Address: 0xf0004800 + 0x8 = 0xf0004808`

SPI MOSI data (MSB-first serialization).

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mosi[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



SPI_MASTER_MISO


`Address: 0xf0004800 + 0xc = 0xf000480c`

SPI MISO data (MSB-first de-serialization).

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'miso[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



SPI_MASTER_CS


`Address: 0xf0004800 + 0x10 = 0xf0004810`

SPI CS Chip-Select and Mode.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'sel',  'attr': '1', 'bits': 1},{'bits': 15},{'name': 'mode',  'bits': 1},{'bits': 15}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                                                                                                |
|-------|------|------------------------------------------------------------------------------------------------------------|
| [0]   | SEL  | Chip 0 selected for SPI Xfer. Chip ``N`` selected for SPI Xfer.                                            |
| [16]  | MODE | 0 = Normal operation (CS handled by Core). 1 = Manual operation (CS handled by User, direct recopy of ``sel``) |

SPI_MASTER_LOOPBACK


`Address: 0xf0004800 + 0x14 = 0xf0004814`

SPI Loopback Mode.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                                                  |
|-------|------|--------------------------------------------------------------|
| [0]   | MODE | 0 = Normal operation. 1 = Loopback operation (MOSI to MISO). |

SPI_MASTER_CLK_DIVIDER


`Address: 0xf0004800 + 0x18 = 0xf0004818`

SPI Clk Divider.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'clk_divider[15:0]', 'attr': 'reset: 100', 'bits': 16},{'bits': 16},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



QSPI_ENABLED
============

Register Listing for QSPI_ENABLED
---------------------------------

| Register                                   | Address                              |
|--------------------------------------------|--------------------------------------|
| QSPI_ENABLED_OUT  | 0xf0004000  |

QSPI_ENABLED_OUT


`Address: 0xf0004000 + 0x0 = 0xf0004000`

GPIO Output(s) Control.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



Logic Analyzer
==

Register Listing for Logic Analyzer
-----------------------

| Register               | Address                 | C Macro Name          |
|------------------------|-------------------------|-----------------------|
| LA_IEN3                | 0xf0003000              | reg_la3_iena          |
| LA_IEN2                | 0xf0003004              | reg_la2_iena          |
| LA_IEN1                | 0xf0003008              | reg_la1_iena          |
| LA_IEN0                | 0xf000300c              | reg_la0_iena          |
| LA_OE3                 | 0xf0003010              | reg_la3_oenb          |
| LA_OE2                 | 0xf0003014              | reg_la2_oenb          |
| LA_OE1                 | 0xf0003018              | reg_la1_oenb          |
| LA_OE0                 | 0xf000301c              | reg_la0_oenb          |
| LA_IN3                 | 0xf0003020              | reg_la3_data_in       |
| LA_IN2                 | 0xf0003024              | reg_la2_data_in       |
| LA_IN1                 | 0xf0003028              | reg_la1_data_in       |
| LA_IN0                 | 0xf000302c              | reg_la0_data_in       |
| LA_OUT3                | 0xf0003030              | reg_la3_data          |
| LA_OUT2                | 0xf0003034              | reg_la2_data          |
| LA_OUT1                | 0xf0003038              | reg_la1_data          |
| LA_OUT0                | 0xf000303c              | reg_la0_data          |

LA_IEN3


`Address: 0xf0003000 + 0x0 = 0xf0003000`

Bits 96-127 of `LA_IEN`. LA Input Enable

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'ien[127:96]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



LA_IEN2


`Address: 0xf0003000 + 0x4 = 0xf0003004`

Bits 64-95 of `LA_IEN`.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'ien[95:64]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



LA_IEN1


`Address: 0xf0003000 + 0x8 = 0xf0003008`

Bits 32-63 of `LA_IEN`.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'ien[63:32]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



LA_IEN0


`Address: 0xf0003000 + 0xc = 0xf000300c`

Bits 0-31 of `LA_IEN`.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'ien[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



LA_OE3


`Address: 0xf0003000 + 0x10 = 0xf0003010`

Bits 96-127 of `LA_OE`. LA Output Enable

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'oe[127:96]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



LA_OE2


`Address: 0xf0003000 + 0x14 = 0xf0003014`

Bits 64-95 of `LA_OE`.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'oe[95:64]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



LA_OE1


`Address: 0xf0003000 + 0x18 = 0xf0003018`

Bits 32-63 of `LA_OE`.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'oe[63:32]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



LA_OE0


`Address: 0xf0003000 + 0x1c = 0xf000301c`

Bits 0-31 of `LA_OE`.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'oe[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



LA_IN3


`Address: 0xf0003000 + 0x20 = 0xf0003020`

Bits 96-127 of `LA_IN`. LA Input(s) Status.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in[127:96]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



LA_IN2


`Address: 0xf0003000 + 0x24 = 0xf0003024`

Bits 64-95 of `LA_IN`.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in[95:64]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



LA_IN1


`Address: 0xf0003000 + 0x28 = 0xf0003028`

Bits 32-63 of `LA_IN`.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in[63:32]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



LA_IN0


`Address: 0xf0003000 + 0x2c = 0xf000302c`

Bits 0-31 of `LA_IN`.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



LA_OUT3


`Address: 0xf0003000 + 0x30 = 0xf0003030`

Bits 96-127 of `LA_OUT`. LA Ouptut(s) Control.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[127:96]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



LA_OUT2


`Address: 0xf0003000 + 0x34 = 0xf0003034`

Bits 64-95 of `LA_OUT`.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[95:64]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



LA_OUT1


`Address: 0xf0003000 + 0x38 = 0xf0003038`

Bits 32-63 of `LA_OUT`.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[63:32]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



LA_OUT0


`Address: 0xf0003000 + 0x3c = 0xf000303c`

Bits 0-31 of `LA_OUT`.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



UART
====

Register Listing for UART
-------------------------

| Register                   | Address              | C Macro Name       |
|----------------------------|----------------------|--------------------|
| UART_RXTX                  | 0xf0005800           | reg_uart_data      |
| UART_TXFULL                | 0xf0005804           | reg_uart_txfull    |
| UART_RXEMPTY               | 0xf0005808           |
| UART_EV_STATUS             | 0xf000580c           |
| UART_EV_PENDING            | 0xf0005810           |
| UART_EV_ENABLE             | 0xf0005814           | reg_uart_irq_en    |
| UART_TXEMPTY               | 0xf0005818           |
| UART_RXFULL                | 0xf000581c           |

UART_RXTX


`Address: 0xf0005800 + 0x0 = 0xf0005800`


<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'rxtx[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



UART_TXFULL


`Address: 0xf0005800 + 0x4 = 0xf0005804`

TX FIFO Full.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'txfull', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



UART_RXEMPTY


`Address: 0xf0005800 + 0x8 = 0xf0005808`

RX FIFO Empty.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'rxempty', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



UART_EV_STATUS


`Address: 0xf0005800 + 0xc = 0xf000580c`

This register contains the current raw level of the rx event trigger.  Writes to
this register have no effect.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx',  'bits': 1},{'name': 'rx',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description               |
|-------|------|---------------------------|
| [0]   | TX   | Level of the tx event |
| [1]   | RX   | Level of the rx event |

UART_EV_PENDING


`Address: 0xf0005800 + 0x10 = 0xf0005810`

When a  rx event occurs, the corresponding bit will be set in this register.  To
clear the Event, set the corresponding bit in this register.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx',  'bits': 1},{'name': 'rx',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                                                                  |
|-------|------|------------------------------------------------------------------------------|
| [0]   | TX   | 1 if a tx event occurred. This Event is triggered on a **falling** edge. |
| [1]   | RX   | 1 if a rx event occurred. This Event is triggered on a **falling** edge. |

UART_EV_ENABLE


`Address: 0xf0005800 + 0x14 = 0xf0005814`

This register enables the corresponding rx events.  Write a ``0`` to this
register to disable individual events.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx',  'bits': 1},{'name': 'rx',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                              |
|-------|------|------------------------------------------|
| [0]   | TX   | Write a 1 to enable the tx Event |
| [1]   | RX   | Write a 1 to enable the rx Event |

UART_TXEMPTY


`Address: 0xf0005800 + 0x18 = 0xf0005818`

TX FIFO Empty.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'txempty', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



UART_RXFULL


`Address: 0xf0005800 + 0x1c = 0xf000581c`

RX FIFO Full.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'rxfull', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>


TIMER0
======

Timer
-----

Provides a generic Timer core.

The Timer is implemented as a countdown timer that can be used in various modes:

- Polling : Returns current countdown value to software
- One-Shot: Loads itself and stops when value reaches ``0``
- Periodic: (Re-)Loads itself when value reaches ``0``

``en`` register allows the user to enable/disable the Timer. When the Timer is enabled, it is
automatically loaded with the value of `load` register.

When the Timer reaches ``0``, it is automatically reloaded with value of `reload` register.

The user can latch the current countdown value by writing to ``update_value`` register, it will
update ``value`` register with current countdown value.

To use the Timer in One-Shot mode, the user needs to:

- Disable the timer
- Set the ``load`` register to the expected duration
- (Re-)Enable the Timer

To use the Timer in Periodic mode, the user needs to:

- Disable the Timer
- Set the ``load`` register to 0
- Set the ``reload`` register to the expected period
- Enable the Timer

For both modes, the CPU can be advertised by an IRQ that the duration/period has elapsed. (The
CPU can also do software polling with ``update_value`` and ``value`` to know the elapsed duration)


Register Listing for TIMER0
---------------------------

| Register                  | Address              | C Macro Name               |
|---------------------------|----------------------|----------------------------|
| TIMER0_LOAD               | 0xf0005000           | reg_timer0_data            |
| TIMER0_RELOAD             | 0xf0005004           | reg_timer0_data_periodic   |
| TIMER0_EN                 | 0xf0005008           | reg_timer0_config          |
| TIMER0_UPDATE_VALUE       | 0xf000500c           | reg_timer0_update          |
| TIMER0_VALUE              | 0xf0005010           | reg_timer0_value           |
| TIMER0_EV_STATUS          | 0xf0005014           | 
| TIMER0_EV_PENDING         | 0xf0005018           |
| TIMER0_EV_ENABLE          | 0xf000501c           | reg_timer0_irq_en          |

TIMER0_LOAD


`Address: 0xf0005000 + 0x0 = 0xf0005000`

Load value when Timer is (re-)enabled. In One-Shot mode, the value written to
this register specifies the Timer's duration in clock cycles.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'load[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



TIMER0_RELOAD


`Address: 0xf0005000 + 0x4 = 0xf0005004`

Reload value when Timer reaches ``0``. In Periodic mode, the value written to
this register specify the Timer's period in clock cycles.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'reload[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



TIMER0_EN


`Address: 0xf0005000 + 0x8 = 0xf0005008`

Enable flag of the Timer. Set this flag to ``1`` to enable/start the Timer.  Set
to ``0`` to disable the Timer.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'en', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



TIMER0_UPDATE_VALUE


`Address: 0xf0005000 + 0xc = 0xf000500c`

Update trigger for the current countdown value. A write to this register latches
the current countdown value to ``value`` register.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'update_value', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



TIMER0_VALUE


`Address: 0xf0005000 + 0x10 = 0xf0005010`

Latched countdown value. This value is updated by writing to ``update_value``.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'value[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



TIMER0_EV_STATUS


`Address: 0xf0005000 + 0x14 = 0xf0005014`

This register contains the current raw level of the zero event trigger.  Writes
to this register have no effect.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'zero',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                 |
|-------|------|-----------------------------|
| [0]   | ZERO | Level of the zero event |

TIMER0_EV_PENDING


`Address: 0xf0005000 + 0x18 = 0xf0005018`

When a  zero event occurs, the corresponding bit will be set in this register.
To clear the Event, set the corresponding bit in this register.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'zero',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                                                                    |
|-------|------|--------------------------------------------------------------------------------|
| [0]   | ZERO | 1 if a zero event occurred. This Event is triggered on a **falling** edge. |

TIMER0_EV_ENABLE


`Address: 0xf0005000 + 0x1c = 0xf000501c`

This register enables the corresponding zero events.  Write a ``0`` to this
register to disable individual events.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'zero',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                                |
|-------|------|--------------------------------------------|
| [0]   | ZERO | Write a 1 to enable the zero Event |

FLASH_CORE
==========

Register Listing for FLASH_CORE
-------------------------------

| Register                                                         | Address                                         |
|------------------------------------------------------------------|-------------------------------------------------|
| FLASH_CORE_MMAP_DUMMY_BITS    | 0xf0001800   |
| FLASH_CORE_MASTER_CS                | 0xf0001804         |
| FLASH_CORE_MASTER_PHYCONFIG  | 0xf0001808  |
| FLASH_CORE_MASTER_RXTX            | 0xf000180c       |
| FLASH_CORE_MASTER_STATUS        | 0xf0001810     |

FLASH_CORE_MMAP_DUMMY_BITS


`Address: 0xf0001800 + 0x0 = 0xf0001800`


<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mmap_dummy_bits[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



FLASH_CORE_MASTER_CS


`Address: 0xf0001800 + 0x4 = 0xf0001804`


<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'master_cs', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



FLASH_CORE_MASTER_PHYCONFIG


`Address: 0xf0001800 + 0x8 = 0xf0001808`

SPI PHY settings.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'len',  'bits': 8},{'name': 'width',  'bits': 4},{'bits': 4},{'name': 'mask',  'bits': 8},{'bits': 8}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field   | Name  | Description                                                                 |
|---------|-------|-----------------------------------------------------------------------------|
| [7:0]   | LEN   | SPI Xfer length (in bits).                                                  |
| [11:8]  | WIDTH | SPI Xfer width (1/2/4/8).                                                   |
| [23:16] | MASK  | SPI DQ output enable mask (set bits to 1 to enable output drivers on DQ lines).|

FLASH_CORE_MASTER_RXTX


`Address: 0xf0001800 + 0xc = 0xf000180c`


<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'master_rxtx[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



FLASH_CORE_MASTER_STATUS


`Address: 0xf0001800 + 0x10 = 0xf0001810`


<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx_ready',  'bits': 1},{'name': 'rx_ready',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name     | Description           |
|-------|----------|-----------------------|
| [0]   | TX_READY | TX FIFO is not full.  |
| [1]   | RX_READY | RX FIFO is not empty. |

DEBUG_MODE
==========

Register Listing for DEBUG_MODE
-------------------------------

| Register                               | Address                            |
|----------------------------------------|------------------------------------|
| DEBUG_MODE_OUT  | 0xf0000800  |

DEBUG_MODE_OUT


`Address: 0xf0000800 + 0x0 = 0xf0000800`

GPIO Output(s) Control.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



DEBUG_OEB
=========

Register Listing for DEBUG_OEB
------------------------------

| Register                             | Address                           |
|--------------------------------------|-----------------------------------|
| DEBUG_OEB_OUT  | 0xf0001000  |

DEBUG_OEB_OUT


`Address: 0xf0001000 + 0x0 = 0xf0001000`

GPIO Output(s) Control.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



UART_ENABLED
============

Register Listing for UART_ENABLED
---------------------------------

| Register                 | Address               | C Macro Name     |
|--------------------------|-----------------------|------------------|
| UART_ENABLED_OUT         | 0xf0006000            | reg_uart_enable  |

UART_ENABLED_OUT


`Address: 0xf0006000 + 0x0 = 0xf0006000`

GPIO Output(s) Control.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



Interrupt Controller
====================

This device has an ``EventManager``-based interrupt system.  Individual modules
generate `events` which are wired into a central interrupt controller.

When an interrupt occurs, you should look the interrupt number up in the CPU-
specific interrupt table and then call the relevant module.

Assigned Interrupts
-------------------

The following interrupts are assigned on this system:

| Interrupt | Module                         |
|-----------|--------------------------------|
| 0         | TIMER0          |
| 1         | UART              |
| 2         | USER_IRQ_0  |
| 3         | USER_IRQ_1  |
| 4         | USER_IRQ_2  |
| 5         | USER_IRQ_3  |
| 6         | USER_IRQ_4  |
| 7         | USER_IRQ_5  |

Management GPIO
==============

Register Listing for GPIO
-------------------------

| Register           | Address               | C Macro Name              |
|--------------------|-----------------------|---------------------------|
| GPIO_MODE1         | 0xf0002800            | reg_gpio_mode1            |
| GPIO_MODE0         | 0xf0002804            | reg_gpio_mode0            |
| GPIO_IEN           | 0xf0002808            | reg_gpio_ien              |
| GPIO_OE            | 0xf000280c            | reg_gpio_oe               |
| GPIO_IN            | 0xf0002810            | reg_gpio_in               |
| GPIO_OUT           | 0xf0002814            | reg_gpio_out              |

GPIO_MODE1


`Address: 0xf0002800 + 0x0 = 0xf0002800`

GPIO Tristate(s) Control.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode1', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



GPIO_MODE0


`Address: 0xf0002800 + 0x4 = 0xf0002804`

GPIO Tristate(s) Control.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode0', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



GPIO_IEN


`Address: 0xf0002800 + 0x8 = 0xf0002808`

GPIO Tristate(s) Control.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'ien', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



GPIO_OE


`Address: 0xf0002800 + 0xc = 0xf000280c`

GPIO Tristate(s) Control.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'oe', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



GPIO_IN


`Address: 0xf0002800 + 0x10 = 0xf0002810`

GPIO Input(s) Status.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



GPIO_OUT


`Address: 0xf0002800 + 0x14 = 0xf0002814`

GPIO Ouptut(s) Control.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_4
==========

Register Listing for USER_IRQ_4
-------------------------------

| Register                             | Address                     | C Macro Name              |
|--------------------------------------|-----------------------------|---------------------------|
| USER_IRQ_4_IN                        | 0xf0008800                  |
| USER_IRQ_4_MODE                      | 0xf0008804                  |
| USER_IRQ_4_EDGE                      | 0xf0008808                  |
| USER_IRQ_4_EV_STATUS                 | 0xf000880c                  |
| USER_IRQ_4_EV_PENDING                | 0xf0008810                  |
| USER_IRQ_4_EV_ENABLE                 | 0xf0008814                  | reg_user4_irq_en          |

USER_IRQ_4_IN


`Address: 0xf0008800 + 0x0 = 0xf0008800`

GPIO Input(s) Status.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_4_MODE


`Address: 0xf0008800 + 0x4 = 0xf0008804`

GPIO IRQ Mode: 0: Edge, 1: Change.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_4_EDGE


`Address: 0xf0008800 + 0x8 = 0xf0008808`

GPIO IRQ Edge (when in Edge mode): 0: Rising Edge, 1: Falling Edge.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_4_EV_STATUS


`Address: 0xf0008800 + 0xc = 0xf000880c`

This register contains the current raw level of the i0 event trigger.  Writes to
this register have no effect.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description               |
|-------|------|---------------------------|
| [0]   | I0   | Level of the i0 event |

USER_IRQ_4_EV_PENDING


`Address: 0xf0008800 + 0x10 = 0xf0008810`

When a  i0 event occurs, the corresponding bit will be set in this register.  To
clear the Event, set the corresponding bit in this register.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                                                                  |
|-------|------|------------------------------------------------------------------------------|
| [0]   | I0   | 1 if a i0 event occurred. This Event is triggered on a **falling** edge. |

USER_IRQ_4_EV_ENABLE


`Address: 0xf0008800 + 0x14 = 0xf0008814`

This register enables the corresponding i0 events.  Write a ``0`` to this
register to disable individual events.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                              |
|-------|------|------------------------------------------|
| [0]   | I0   | Write a 1 to enable the i0 Event |

USER_IRQ_5
==========

Register Listing for USER_IRQ_5
-------------------------------

| Register                            | Address                    | C Macro Name           |
|-------------------------------------|----------------------------|------------------------|
| USER_IRQ_5_IN                       | 0xf0009000                 |
| USER_IRQ_5_MODE                     | 0xf0009004                 |
| USER_IRQ_5_EDGE                     | 0xf0009008                 |
| USER_IRQ_5_EV_STATUS                | 0xf000900c                 |
| USER_IRQ_5_EV_PENDING               | 0xf0009010                 |
| USER_IRQ_5_EV_ENABLE                | 0xf0009014                 | reg_user5_irq_en       |

USER_IRQ_5_IN


`Address: 0xf0009000 + 0x0 = 0xf0009000`

GPIO Input(s) Status.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_5_MODE


`Address: 0xf0009000 + 0x4 = 0xf0009004`

GPIO IRQ Mode: 0: Edge, 1: Change.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_5_EDGE


`Address: 0xf0009000 + 0x8 = 0xf0009008`

GPIO IRQ Edge (when in Edge mode): 0: Rising Edge, 1: Falling Edge.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_5_EV_STATUS


`Address: 0xf0009000 + 0xc = 0xf000900c`

This register contains the current raw level of the i0 event trigger.  Writes to
this register have no effect.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description               |
|-------|------|---------------------------|
| [0]   | I0   | Level of the i0 event |

USER_IRQ_5_EV_PENDING


`Address: 0xf0009000 + 0x10 = 0xf0009010`

When a  i0 event occurs, the corresponding bit will be set in this register.  To
clear the Event, set the corresponding bit in this register.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                                                                  |
|-------|------|------------------------------------------------------------------------------|
| [0]   | I0   | 1 if a i0 event occurred. This Event is triggered on a **falling** edge. |

USER_IRQ_5_EV_ENABLE


`Address: 0xf0009000 + 0x14 = 0xf0009014`

This register enables the corresponding i0 events.  Write a ``0`` to this
register to disable individual events.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                              |
|-------|------|------------------------------------------|
| [0]   | I0   | Write a 1 to enable the i0 Event |

FLASH_PHY
=========

Register Listing for FLASH_PHY
------------------------------

| Register                                             | Address                                   |
|------------------------------------------------------|-------------------------------------------|
| FLASH_PHY_CLK_DIVISOR  | 0xf0002000  |

FLASH_PHY_CLK_DIVISOR


`Address: 0xf0002000 + 0x0 = 0xf0002000`


<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'clk_divisor[7:0]', 'attr': 'reset: 1', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>



USER_IRQ_2
==========

Register Listing for USER_IRQ_2
-------------------------------

| Register                       | Address                 | C Macro Name           |
|--------------------------------|-------------------------|------------------------|
| USER_IRQ_2_IN                  | 0xf0007800              |
| USER_IRQ_2_MODE                | 0xf0007804              |
| USER_IRQ_2_EDGE                | 0xf0007808              |
| USER_IRQ_2_EV_STATUS           | 0xf000780c              |
| USER_IRQ_2_EV_PENDING          | 0xf0007810              |
| USER_IRQ_2_EV_ENABLE           | 0xf0007814              | reg_user2_irq_en       |

USER_IRQ_2_IN


`Address: 0xf0007800 + 0x0 = 0xf0007800`

GPIO Input(s) Status.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_2_MODE


`Address: 0xf0007800 + 0x4 = 0xf0007804`

GPIO IRQ Mode: 0: Edge, 1: Change.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_2_EDGE


`Address: 0xf0007800 + 0x8 = 0xf0007808`

GPIO IRQ Edge (when in Edge mode): 0: Rising Edge, 1: Falling Edge.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_2_EV_STATUS


`Address: 0xf0007800 + 0xc = 0xf000780c`

This register contains the current raw level of the i0 event trigger.  Writes to
this register have no effect.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description               |
|-------|------|---------------------------|
| [0]   | I0   | Level of the i0 event |

USER_IRQ_2_EV_PENDING


`Address: 0xf0007800 + 0x10 = 0xf0007810`

When a  i0 event occurs, the corresponding bit will be set in this register.  To
clear the Event, set the corresponding bit in this register.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                                                                  |
|-------|------|------------------------------------------------------------------------------|
| [0]   | I0   | 1 if a i0 event occurred. This Event is triggered on a **falling** edge. |

USER_IRQ_2_EV_ENABLE


`Address: 0xf0007800 + 0x14 = 0xf0007814`

This register enables the corresponding i0 events.  Write a ``0`` to this
register to disable individual events.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                              |
|-------|------|------------------------------------------|
| [0]   | I0   | Write a 1 to enable the i0 Event |

USER_IRQ_3
==========

Register Listing for USER_IRQ_3
-------------------------------

| Register                          | Address                    | C Macro Name        |
|-----------------------------------|----------------------------|---------------------|
| USER_IRQ_3_IN                     | 0xf0008000                 |
| USER_IRQ_3_MODE                   | 0xf0008004                 |
| USER_IRQ_3_EDGE                   | 0xf0008008                 |
| USER_IRQ_3_EV_STATUS              | 0xf000800c                 |
| USER_IRQ_3_EV_PENDING             | 0xf0008010                 |
| USER_IRQ_3_EV_ENABLE              | 0xf0008014                 | reg_user3_irq_en    |

USER_IRQ_3_IN


`Address: 0xf0008000 + 0x0 = 0xf0008000`

GPIO Input(s) Status.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_3_MODE


`Address: 0xf0008000 + 0x4 = 0xf0008004`

GPIO IRQ Mode: 0: Edge, 1: Change.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_3_EDGE


`Address: 0xf0008000 + 0x8 = 0xf0008008`

GPIO IRQ Edge (when in Edge mode): 0: Rising Edge, 1: Falling Edge.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_3_EV_STATUS


`Address: 0xf0008000 + 0xc = 0xf000800c`

This register contains the current raw level of the i0 event trigger.  Writes to
this register have no effect.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description               |
|-------|------|---------------------------|
| [0]   | I0   | Level of the i0 event |

USER_IRQ_3_EV_PENDING


`Address: 0xf0008000 + 0x10 = 0xf0008010`

When a  i0 event occurs, the corresponding bit will be set in this register.  To
clear the Event, set the corresponding bit in this register.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                                                                  |
|-------|------|------------------------------------------------------------------------------|
| [0]   | I0   | 1 if a i0 event occurred. This Event is triggered on a **falling** edge. |

USER_IRQ_3_EV_ENABLE


`Address: 0xf0008000 + 0x14 = 0xf0008014`

This register enables the corresponding i0 events.  Write a ``0`` to this
register to disable individual events.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                              |
|-------|------|------------------------------------------|
| [0]   | I0   | Write a 1 to enable the i0 Event |

SPI_ENABLED
===========

Register Listing for SPI_ENABLED
--------------------------------

| Register                | Address                 | C Macro Name     |
|-------------------------|-------------------------|------------------|
| SPI_ENABLED_OUT         | 0xf0004000              | reg_spi_enable   |

SPI_ENABLED_OUT


`Address: 0xf0004000 + 0x0 = 0xf0004000`

GPIO Output(s) Control.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_ENA
============

Register Listing for USER_IRQ_ENA
---------------------------------

| Register                                   | Address                              |
|--------------------------------------------|--------------------------------------|
| USER_IRQ_ENA_OUT  | 0xf0009800  |

USER_IRQ_ENA_OUT


`Address: 0xf0009800 + 0x0 = 0xf0009800`

GPIO Output(s) Control.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[2:0]', 'bits': 3},{'bits': 29},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



MPRJ_WB_IENA
============

Register Listing for MPRJ_WB_IENA
---------------------------------

| Register                  | Address                 | C Macro Name        |
|---------------------------|-------------------------|---------------------|
| MPRJ_WB_IENA_OUT          | 0xf0003800              | reg_wb_enable       |

MPRJ_WB_IENA_OUT


`Address: 0xf0003800 + 0x0 = 0xf0003800`

GPIO Output(s) Control.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_1
==========

Register Listing for USER_IRQ_1
-------------------------------

| Register                         | Address              | C Macro Name            |
|----------------------------------|----------------------|-------------------------|
| USER_IRQ_1_IN                    | 0xf0007000           |  
| USER_IRQ_1_MODE                  | 0xf0007004           |
| USER_IRQ_1_EDGE                  | 0xf0007008           |
| USER_IRQ_1_EV_STATUS             | 0xf000700c           |
| USER_IRQ_1_EV_PENDING            | 0xf0007010           |
| USER_IRQ_1_EV_ENABLE             | 0xf0007014           | reg_user1_irq_en        |

USER_IRQ_1_IN


`Address: 0xf0007000 + 0x0 = 0xf0007000`

GPIO Input(s) Status.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_1_MODE


`Address: 0xf0007000 + 0x4 = 0xf0007004`

GPIO IRQ Mode: 0: Edge, 1: Change.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_1_EDGE


`Address: 0xf0007000 + 0x8 = 0xf0007008`

GPIO IRQ Edge (when in Edge mode): 0: Rising Edge, 1: Falling Edge.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_1_EV_STATUS


`Address: 0xf0007000 + 0xc = 0xf000700c`

This register contains the current raw level of the i0 event trigger.  Writes to
this register have no effect.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description               |
|-------|------|---------------------------|
| [0]   | I0   | Level of the i0 event |

USER_IRQ_1_EV_PENDING


`Address: 0xf0007000 + 0x10 = 0xf0007010`

When a  i0 event occurs, the corresponding bit will be set in this register.  To
clear the Event, set the corresponding bit in this register.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                                                                  |
|-------|------|------------------------------------------------------------------------------|
| [0]   | I0   | 1 if a i0 event occurred. This Event is triggered on a **falling** edge. |

USER_IRQ_1_EV_ENABLE


`Address: 0xf0007000 + 0x14 = 0xf0007014`

This register enables the corresponding i0 events.  Write a ``0`` to this
register to disable individual events.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                              |
|-------|------|------------------------------------------|
| [0]   | I0   | Write a 1 to enable the i0 Event |

USER_IRQ_0
==========

Register Listing for USER_IRQ_0
-------------------------------

| Register                              | Address                   | C Macro Name          |
|---------------------------------------|---------------------------|-----------------------|
| USER_IRQ_0_IN                         | 0xf0006800                |
| USER_IRQ_0_MODE                       | 0xf0006804                |
| USER_IRQ_0_EDGE                       | 0xf0006808                |
| USER_IRQ_0_EV_STATUS                  | 0xf000680c                |
| USER_IRQ_0_EV_PENDING                 | 0xf0006810                |
| USER_IRQ_0_EV_ENABLE                  | 0xf0006814                | reg_user0_irq_en      |

USER_IRQ_0_IN


`Address: 0xf0006800 + 0x0 = 0xf0006800`

GPIO Input(s) Status.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_0_MODE


`Address: 0xf0006800 + 0x4 = 0xf0006804`

GPIO IRQ Mode: 0: Edge, 1: Change.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_0_EDGE


`Address: 0xf0006800 + 0x8 = 0xf0006808`

GPIO IRQ Edge (when in Edge mode): 0: Rising Edge, 1: Falling Edge.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



USER_IRQ_0_EV_STATUS


`Address: 0xf0006800 + 0xc = 0xf000680c`

This register contains the current raw level of the i0 event trigger.  Writes to
this register have no effect.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description               |
|-------|------|---------------------------|
| [0]   | I0   | Level of the i0 event |

USER_IRQ_0_EV_PENDING


`Address: 0xf0006800 + 0x10 = 0xf0006810`

When a  i0 event occurs, the corresponding bit will be set in this register.  To
clear the Event, set the corresponding bit in this register.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                                                                  |
|-------|------|------------------------------------------------------------------------------|
| [0]   | I0   | 1 if a i0 event occurred. This Event is triggered on a **falling** edge. |

USER_IRQ_0_EV_ENABLE


`Address: 0xf0006800 + 0x14 = 0xf0006814`

This register enables the corresponding i0 events.  Write a ``0`` to this
register to disable individual events.

<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>



| Field | Name | Description                              |
|-------|------|------------------------------------------|
| [0]   | I0   | Write a 1 to enable the i0 Event |

