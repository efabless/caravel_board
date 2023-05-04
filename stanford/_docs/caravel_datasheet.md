# Caravel Datasheet

CTRL_RESET
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'soc_rst',  'type': 4, 'bits': 1},{'name': 'cpu_rst',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

CTRL_SCRATCH
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'scratch[31:0]', 'attr': 'reset: 305419896', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

CTRL_BUS_ERRORS
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'bus_errors[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

SPI_MASTER_CONTROL
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'start',  'type': 4, 'bits': 1},{'bits': 7},{'name': 'length',  'bits': 8},{'bits': 16}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

SPI_MASTER_STATUS
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'done',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

SPI_MASTER_MOSI
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'mosi[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

SPI_MASTER_MISO
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'miso[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

SPI_MASTER_CS
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'sel',  'attr': '1', 'bits': 1},{'bits': 15},{'name': 'mode',  'bits': 1},{'bits': 15}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

SPI_MASTER_LOOPBACK
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

SPI_MASTER_CLK_DIVIDER
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'clk_divider[15:0]', 'attr': 'reset: 100', 'bits': 16},{'bits': 16},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

QSPI_ENABLED_OUT
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

LA_IEN3
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'ien[127:96]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

LA_IEN2
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'ien[95:64]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

LA_IEN1
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'ien[63:32]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

LA_IEN0
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'ien[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

LA_OE3
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'oe[127:96]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

LA_OE2
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'oe[95:64]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

LA_OE1
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'oe[63:32]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

LA_OE0
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'oe[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

LA_IN3
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'in[127:96]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

LA_IN2
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'in[95:64]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

LA_IN1
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'in[63:32]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

LA_IN0
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'in[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

LA_OUT3
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[127:96]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

LA_OUT2
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[95:64]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

LA_OUT1
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[63:32]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

LA_OUT0
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

UART_RXTX
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'rxtx[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

UART_TXFULL
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'txfull', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

UART_RXEMPTY
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'rxempty', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

UART_EV_STATUS
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx',  'bits': 1},{'name': 'rx',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

UART_EV_PENDING
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx',  'bits': 1},{'name': 'rx',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

UART_EV_ENABLE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx',  'bits': 1},{'name': 'rx',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

UART_TXEMPTY
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'txempty', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

UART_RXFULL
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'rxfull', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

JUNK_OUT
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

TIMER0_LOAD
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'load[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

TIMER0_RELOAD
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'reload[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

TIMER0_EN
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'en', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

TIMER0_UPDATE_VALUE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'update_value', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

TIMER0_VALUE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'value[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

TIMER0_EV_STATUS
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'zero',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

TIMER0_EV_PENDING
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'zero',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

TIMER0_EV_ENABLE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'zero',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

FLASH_CORE_MMAP_DUMMY_BITS
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'mmap_dummy_bits[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

FLASH_CORE_MASTER_CS
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'master_cs', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

FLASH_CORE_MASTER_PHYCONFIG
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'len',  'bits': 8},{'name': 'width',  'bits': 4},{'bits': 4},{'name': 'mask',  'bits': 8},{'bits': 8}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

FLASH_CORE_MASTER_RXTX
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'master_rxtx[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

FLASH_CORE_MASTER_STATUS
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx_ready',  'bits': 1},{'name': 'rx_ready',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

DEBUG_MODE_OUT
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

DEBUG_OEB_OUT
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

UART_ENABLED_OUT
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

GPIO_MODE1
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode1', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

GPIO_MODE0
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode0', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

GPIO_IEN
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'ien', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

GPIO_OE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'oe', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

GPIO_IN
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

GPIO_OUT
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_4_IN
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_4_MODE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_4_EDGE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_4_EV_STATUS
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_4_EV_PENDING
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_4_EV_ENABLE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_5_IN
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_5_MODE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_5_EDGE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_5_EV_STATUS
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_5_EV_PENDING
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_5_EV_ENABLE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

FLASH_PHY_CLK_DIVISOR
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'clk_divisor[7:0]', 'attr': 'reset: 1', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/>

USER_IRQ_2_IN
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_2_MODE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_2_EDGE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_2_EV_STATUS
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_2_EV_PENDING
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_2_EV_ENABLE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_3_IN
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_3_MODE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_3_EDGE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_3_EV_STATUS
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_3_EV_PENDING
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_3_EV_ENABLE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

SPI_ENABLED_OUT
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_ENA_OUT
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[2:0]', 'bits': 3},{'bits': 29},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

MPRJ_WB_IENA_OUT
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_1_IN
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_1_MODE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_1_EDGE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_1_EV_STATUS
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_1_EV_PENDING
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_1_EV_ENABLE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_0_IN
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_0_MODE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_0_EDGE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_0_EV_STATUS
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_0_EV_PENDING
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>

USER_IRQ_0_EV_ENABLE
<img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/>
