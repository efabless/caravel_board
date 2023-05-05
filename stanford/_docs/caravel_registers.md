| Register                                 | Address                             |
|------------------------------------------|-------------------------------------|
| CTRL_RESET            | 0xf0000000       |
| CTRL_SCRATCH        | 0xf0000004     |
| CTRL_BUS_ERRORS  | 0xf0000008  |
CTRL_RESET
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'soc_rst',  'type': 4, 'bits': 1},{'name': 'cpu_rst',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name    | Description                                                            |
|-------|---------|------------------------------------------------------------------------|
| [0]   | SOC_RST | Write 1 to this register to reset the full SoC (Pulse Reset)         |
| [1]   | CPU_RST | Write 1 to this register to reset the CPU(s) of the SoC (Hold Reset) |
CTRL_SCRATCH
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'scratch[31:0]', 'attr': 'reset: 305419896', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

CTRL_BUS_ERRORS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'bus_errors[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

| Register                                               | Address                                    |
|--------------------------------------------------------|--------------------------------------------|
| SPI_MASTER_CONTROL          | 0xf0004800      |
| SPI_MASTER_STATUS            | 0xf0004804       |
| SPI_MASTER_MOSI                | 0xf0004808         |
| SPI_MASTER_MISO                | 0xf000480c         |
| SPI_MASTER_CS                    | 0xf0004810           |
| SPI_MASTER_LOOPBACK        | 0xf0004814     |
| SPI_MASTER_CLK_DIVIDER  | 0xf0004818  |
SPI_MASTER_CONTROL
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'start',  'type': 4, 'bits': 1},{'bits': 7},{'name': 'length',  'bits': 8},{'bits': 16}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field  | Name   | Description                                 |
|--------|--------|---------------------------------------------|
| [0]    | START  | SPI Xfer Start (Write 1 to start Xfer). |
| [15:8] | LENGTH | SPI Xfer Length (in bits).                  |
SPI_MASTER_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'done',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                         |
|-------|------|-------------------------------------|
| [0]   | DONE | SPI Xfer Done (when read as 1). |
SPI_MASTER_MOSI
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mosi[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

SPI_MASTER_MISO
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'miso[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

SPI_MASTER_CS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'sel',  'attr': '1', 'bits': 1},{'bits': 15},{'name': 'mode',  'bits': 1},{'bits': 15}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                                                                                               |
|-------|------|-----------------------------------------------------------------------------------------------------------|
| [0]   | SEL  |                                                                                                           |
|       |      |                                                                                                           |
|       |      |  -------------- -----------------------------------                                                       |
|       |      | | Value        | Description                       |                                                      |
|       |      |                                                                                                           |
|       |      | | 0b0..001 | Chip 0 selected for SPI Xfer. |                                                      |
|       |      |  -------------- -----------------------------------                                                       |
|       |      | | 0b1..000 | Chip N selected for SPI Xfer. |                                                      |
|       |      |  -------------- -----------------------------------                                                       |
| [16]  | MODE |                                                                                                           |
|       |      |                                                                                                           |
|       |      |  --------- ---------------------------------------------------------------------------------------------  |
|       |      | | Value   | Description                                                                                 | |
|       |      |                                                                                                           |
|       |      | | 0b0 | Normal operation (CS handled by Core).                                                      | |
|       |      |  --------- ---------------------------------------------------------------------------------------------  |
|       |      | | 0b1 | Manual operation (CS handled by User, direct recopy of sel), useful for Bulk transfers. | |
|       |      |  --------- ---------------------------------------------------------------------------------------------  |
SPI_MASTER_LOOPBACK
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                                      |
|-------|------|--------------------------------------------------|
| [0]   | MODE |                                                  |
|       |      |                                                  |
|       |      |  --------- ------------------------------------  |
|       |      | | Value   | Description                        | |
|       |      |                                                  |
|       |      | | 0b0 | Normal operation.                  | |
|       |      |  --------- ------------------------------------  |
|       |      | | 0b1 | Loopback operation (MOSI to MISO). | |
|       |      |  --------- ------------------------------------  |
SPI_MASTER_CLK_DIVIDER
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'clk_divider[15:0]', 'attr': 'reset: 100', 'bits': 16},{'bits': 16},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

| Register                                   | Address                              |
|--------------------------------------------|--------------------------------------|
| QSPI_ENABLED_OUT  | 0xf0004000  |
QSPI_ENABLED_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Register                 | Address                     |
|--------------------------|-----------------------------|
| LA_IEN3  | 0xf0003000  |
| LA_IEN2  | 0xf0003004  |
| LA_IEN1  | 0xf0003008  |
| LA_IEN0  | 0xf000300c  |
| LA_OE3    | 0xf0003010   |
| LA_OE2    | 0xf0003014   |
| LA_OE1    | 0xf0003018   |
| LA_OE0    | 0xf000301c   |
| LA_IN3    | 0xf0003020   |
| LA_IN2    | 0xf0003024   |
| LA_IN1    | 0xf0003028   |
| LA_IN0    | 0xf000302c   |
| LA_OUT3  | 0xf0003030  |
| LA_OUT2  | 0xf0003034  |
| LA_OUT1  | 0xf0003038  |
| LA_OUT0  | 0xf000303c  |
LA_IEN3
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'ien[127:96]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

LA_IEN2
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'ien[95:64]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

LA_IEN1
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'ien[63:32]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

LA_IEN0
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'ien[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

LA_OE3
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'oe[127:96]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

LA_OE2
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'oe[95:64]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

LA_OE1
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'oe[63:32]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

LA_OE0
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'oe[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

LA_IN3
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in[127:96]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

LA_IN2
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in[95:64]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

LA_IN1
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in[63:32]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

LA_IN0
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

LA_OUT3
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[127:96]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

LA_OUT2
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[95:64]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

LA_OUT1
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[63:32]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

LA_OUT0
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

| Register                                 | Address                             |
|------------------------------------------|-------------------------------------|
| UART_RXTX              | 0xf0005800        |
| UART_TXFULL          | 0xf0005804      |
| UART_RXEMPTY        | 0xf0005808     |
| UART_EV_STATUS    | 0xf000580c   |
| UART_EV_PENDING  | 0xf0005810  |
| UART_EV_ENABLE    | 0xf0005814   |
| UART_TXEMPTY        | 0xf0005818     |
| UART_RXFULL          | 0xf000581c      |
UART_RXTX
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'rxtx[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

UART_TXFULL
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'txfull', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

UART_RXEMPTY
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'rxempty', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

UART_EV_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx',  'bits': 1},{'name': 'rx',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description               |
|-------|------|---------------------------|
| [0]   | TX   | Level of the tx event |
| [1]   | RX   | Level of the rx event |
UART_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx',  'bits': 1},{'name': 'rx',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                                                                  |
|-------|------|------------------------------------------------------------------------------|
| [0]   | TX   | 1 if a tx event occurred. This Event is triggered on a **falling** edge. |
| [1]   | RX   | 1 if a rx event occurred. This Event is triggered on a **falling** edge. |
UART_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx',  'bits': 1},{'name': 'rx',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                              |
|-------|------|------------------------------------------|
| [0]   | TX   | Write a 1 to enable the tx Event |
| [1]   | RX   | Write a 1 to enable the rx Event |
UART_TXEMPTY
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'txempty', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

UART_RXFULL
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'rxfull', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Register                   | Address                      |
|----------------------------|------------------------------|
| JUNK_OUT  | 0xf0003000  |
JUNK_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Register                                         | Address                                 |
|--------------------------------------------------|-----------------------------------------|
| TIMER0_LOAD                  | 0xf0005000          |
| TIMER0_RELOAD              | 0xf0005004        |
| TIMER0_EN                      | 0xf0005008            |
| TIMER0_UPDATE_VALUE  | 0xf000500c  |
| TIMER0_VALUE                | 0xf0005010         |
| TIMER0_EV_STATUS        | 0xf0005014     |
| TIMER0_EV_PENDING      | 0xf0005018    |
| TIMER0_EV_ENABLE        | 0xf000501c     |
TIMER0_LOAD
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'load[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

TIMER0_RELOAD
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'reload[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

TIMER0_EN
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'en', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

TIMER0_UPDATE_VALUE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'update_value', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

TIMER0_VALUE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'value[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

TIMER0_EV_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'zero',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                 |
|-------|------|-----------------------------|
| [0]   | ZERO | Level of the zero event |
TIMER0_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'zero',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                                                                    |
|-------|------|--------------------------------------------------------------------------------|
| [0]   | ZERO | 1 if a zero event occurred. This Event is triggered on a **falling** edge. |
TIMER0_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'zero',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                                |
|-------|------|--------------------------------------------|
| [0]   | ZERO | Write a 1 to enable the zero Event |
| Register                                                         | Address                                         |
|------------------------------------------------------------------|-------------------------------------------------|
| FLASH_CORE_MMAP_DUMMY_BITS    | 0xf0001800   |
| FLASH_CORE_MASTER_CS                | 0xf0001804         |
| FLASH_CORE_MASTER_PHYCONFIG  | 0xf0001808  |
| FLASH_CORE_MASTER_RXTX            | 0xf000180c       |
| FLASH_CORE_MASTER_STATUS        | 0xf0001810     |
FLASH_CORE_MMAP_DUMMY_BITS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mmap_dummy_bits[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

FLASH_CORE_MASTER_CS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'master_cs', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

FLASH_CORE_MASTER_PHYCONFIG
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'len',  'bits': 8},{'name': 'width',  'bits': 4},{'bits': 4},{'name': 'mask',  'bits': 8},{'bits': 8}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field   | Name  | Description                                                                 |
|---------|-------|-----------------------------------------------------------------------------|
| [7:0]   | LEN   | SPI Xfer length (in bits).                                                  |
| [11:8]  | WIDTH | SPI Xfer width (1/2/4/8).                                                   |
| [23:16] | MASK  | SPI DQ output enable mask (set bits to 1 to enable output drivers on DQ |
|         |       | lines).                                                                     |
FLASH_CORE_MASTER_RXTX
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'master_rxtx[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

FLASH_CORE_MASTER_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx_ready',  'bits': 1},{'name': 'rx_ready',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name     | Description           |
|-------|----------|-----------------------|
| [0]   | TX_READY | TX FIFO is not full.  |
| [1]   | RX_READY | RX FIFO is not empty. |
| Register                               | Address                            |
|----------------------------------------|------------------------------------|
| DEBUG_MODE_OUT  | 0xf0000800  |
DEBUG_MODE_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Register                             | Address                           |
|--------------------------------------|-----------------------------------|
| DEBUG_OEB_OUT  | 0xf0001000  |
DEBUG_OEB_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Register                                   | Address                              |
|--------------------------------------------|--------------------------------------|
| UART_ENABLED_OUT  | 0xf0006000  |
UART_ENABLED_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Interrupt | Module                         |
|-----------|--------------------------------|
| 0         | :doc:TIMER0          |
| 1         | :doc:UART              |
| 2         | :doc:USER_IRQ_0  |
| 3         | :doc:USER_IRQ_1  |
| 4         | :doc:USER_IRQ_2  |
| 5         | :doc:USER_IRQ_3  |
| 6         | :doc:USER_IRQ_4  |
| 7         | :doc:USER_IRQ_5  |
| Register                       | Address                        |
|--------------------------------|--------------------------------|
| GPIO_MODE1  | 0xf0002800  |
| GPIO_MODE0  | 0xf0002804  |
| GPIO_IEN      | 0xf0002808    |
| GPIO_OE        | 0xf000280c     |
| GPIO_IN        | 0xf0002810     |
| GPIO_OUT      | 0xf0002814    |
GPIO_MODE1
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode1', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

GPIO_MODE0
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode0', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

GPIO_IEN
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'ien', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

GPIO_OE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'oe', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

GPIO_IN
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

GPIO_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Register                                             | Address                                   |
|------------------------------------------------------|-------------------------------------------|
| USER_IRQ_4_IN                  | 0xf0008800          |
| USER_IRQ_4_MODE              | 0xf0008804        |
| USER_IRQ_4_EDGE              | 0xf0008808        |
| USER_IRQ_4_EV_STATUS    | 0xf000880c   |
| USER_IRQ_4_EV_PENDING  | 0xf0008810  |
| USER_IRQ_4_EV_ENABLE    | 0xf0008814   |
USER_IRQ_4_IN
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_4_MODE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_4_EDGE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_4_EV_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description               |
|-------|------|---------------------------|
| [0]   | I0   | Level of the i0 event |
USER_IRQ_4_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                                                                  |
|-------|------|------------------------------------------------------------------------------|
| [0]   | I0   | 1 if a i0 event occurred. This Event is triggered on a **falling** edge. |
USER_IRQ_4_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                              |
|-------|------|------------------------------------------|
| [0]   | I0   | Write a 1 to enable the i0 Event |
| Register                                             | Address                                   |
|------------------------------------------------------|-------------------------------------------|
| USER_IRQ_5_IN                  | 0xf0009000          |
| USER_IRQ_5_MODE              | 0xf0009004        |
| USER_IRQ_5_EDGE              | 0xf0009008        |
| USER_IRQ_5_EV_STATUS    | 0xf000900c   |
| USER_IRQ_5_EV_PENDING  | 0xf0009010  |
| USER_IRQ_5_EV_ENABLE    | 0xf0009014   |
USER_IRQ_5_IN
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_5_MODE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_5_EDGE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_5_EV_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description               |
|-------|------|---------------------------|
| [0]   | I0   | Level of the i0 event |
USER_IRQ_5_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                                                                  |
|-------|------|------------------------------------------------------------------------------|
| [0]   | I0   | 1 if a i0 event occurred. This Event is triggered on a **falling** edge. |
USER_IRQ_5_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                              |
|-------|------|------------------------------------------|
| [0]   | I0   | Write a 1 to enable the i0 Event |
| Register                                             | Address                                   |
|------------------------------------------------------|-------------------------------------------|
| FLASH_PHY_CLK_DIVISOR  | 0xf0002000  |
FLASH_PHY_CLK_DIVISOR
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'clk_divisor[7:0]', 'attr': 'reset: 1', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

| Register                                             | Address                                   |
|------------------------------------------------------|-------------------------------------------|
| USER_IRQ_2_IN                  | 0xf0007800          |
| USER_IRQ_2_MODE              | 0xf0007804        |
| USER_IRQ_2_EDGE              | 0xf0007808        |
| USER_IRQ_2_EV_STATUS    | 0xf000780c   |
| USER_IRQ_2_EV_PENDING  | 0xf0007810  |
| USER_IRQ_2_EV_ENABLE    | 0xf0007814   |
USER_IRQ_2_IN
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_2_MODE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_2_EDGE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_2_EV_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description               |
|-------|------|---------------------------|
| [0]   | I0   | Level of the i0 event |
USER_IRQ_2_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                                                                  |
|-------|------|------------------------------------------------------------------------------|
| [0]   | I0   | 1 if a i0 event occurred. This Event is triggered on a **falling** edge. |
USER_IRQ_2_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                              |
|-------|------|------------------------------------------|
| [0]   | I0   | Write a 1 to enable the i0 Event |
| Register                                             | Address                                   |
|------------------------------------------------------|-------------------------------------------|
| USER_IRQ_3_IN                  | 0xf0008000          |
| USER_IRQ_3_MODE              | 0xf0008004        |
| USER_IRQ_3_EDGE              | 0xf0008008        |
| USER_IRQ_3_EV_STATUS    | 0xf000800c   |
| USER_IRQ_3_EV_PENDING  | 0xf0008010  |
| USER_IRQ_3_EV_ENABLE    | 0xf0008014   |
USER_IRQ_3_IN
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_3_MODE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_3_EDGE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_3_EV_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description               |
|-------|------|---------------------------|
| [0]   | I0   | Level of the i0 event |
USER_IRQ_3_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                                                                  |
|-------|------|------------------------------------------------------------------------------|
| [0]   | I0   | 1 if a i0 event occurred. This Event is triggered on a **falling** edge. |
USER_IRQ_3_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                              |
|-------|------|------------------------------------------|
| [0]   | I0   | Write a 1 to enable the i0 Event |
| Register                                 | Address                             |
|------------------------------------------|-------------------------------------|
| SPI_ENABLED_OUT  | 0xf0004000  |
SPI_ENABLED_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Register                                   | Address                              |
|--------------------------------------------|--------------------------------------|
| USER_IRQ_ENA_OUT  | 0xf0009800  |
USER_IRQ_ENA_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[2:0]', 'bits': 3},{'bits': 29},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Register                                   | Address                              |
|--------------------------------------------|--------------------------------------|
| MPRJ_WB_IENA_OUT  | 0xf0003800  |
MPRJ_WB_IENA_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Register                                             | Address                                   |
|------------------------------------------------------|-------------------------------------------|
| USER_IRQ_1_IN                  | 0xf0007000          |
| USER_IRQ_1_MODE              | 0xf0007004        |
| USER_IRQ_1_EDGE              | 0xf0007008        |
| USER_IRQ_1_EV_STATUS    | 0xf000700c   |
| USER_IRQ_1_EV_PENDING  | 0xf0007010  |
| USER_IRQ_1_EV_ENABLE    | 0xf0007014   |
USER_IRQ_1_IN
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_1_MODE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_1_EDGE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_1_EV_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description               |
|-------|------|---------------------------|
| [0]   | I0   | Level of the i0 event |
USER_IRQ_1_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                                                                  |
|-------|------|------------------------------------------------------------------------------|
| [0]   | I0   | 1 if a i0 event occurred. This Event is triggered on a **falling** edge. |
USER_IRQ_1_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                              |
|-------|------|------------------------------------------|
| [0]   | I0   | Write a 1 to enable the i0 Event |
| Register                                             | Address                                   |
|------------------------------------------------------|-------------------------------------------|
| USER_IRQ_0_IN                  | 0xf0006800          |
| USER_IRQ_0_MODE              | 0xf0006804        |
| USER_IRQ_0_EDGE              | 0xf0006808        |
| USER_IRQ_0_EV_STATUS    | 0xf000680c   |
| USER_IRQ_0_EV_PENDING  | 0xf0006810  |
| USER_IRQ_0_EV_ENABLE    | 0xf0006814   |
USER_IRQ_0_IN
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_0_MODE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_0_EDGE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_0_EV_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description               |
|-------|------|---------------------------|
| [0]   | I0   | Level of the i0 event |
USER_IRQ_0_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                                                                  |
|-------|------|------------------------------------------------------------------------------|
| [0]   | I0   | 1 if a i0 event occurred. This Event is triggered on a **falling** edge. |
USER_IRQ_0_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

| Field | Name | Description                              |
|-------|------|------------------------------------------|
| [0]   | I0   | Write a 1 to enable the i0 Event |
