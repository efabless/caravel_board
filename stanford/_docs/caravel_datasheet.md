# Caravel Datasheet

CTRL_RESET
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'soc_rst',  'type': 4, 'bits': 1},{'name': 'cpu_rst',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

CTRL_SCRATCH
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'scratch[31:0]', 'attr': 'reset: 305419896', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

CTRL_BUS_ERRORS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'bus_errors[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

SPI_MASTER_CONTROL
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'start',  'type': 4, 'bits': 1},{'bits': 7},{'name': 'length',  'bits': 8},{'bits': 16}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

SPI_MASTER_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'done',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

SPI_MASTER_MOSI
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mosi[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

SPI_MASTER_MISO
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'miso[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

SPI_MASTER_CS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'sel',  'attr': '1', 'bits': 1},{'bits': 15},{'name': 'mode',  'bits': 1},{'bits': 15}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

SPI_MASTER_LOOPBACK
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

SPI_MASTER_CLK_DIVIDER
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'clk_divider[15:0]', 'attr': 'reset: 100', 'bits': 16},{'bits': 16},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

QSPI_ENABLED_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

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

UART_RXTX
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'rxtx[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

UART_TXFULL
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'txfull', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

UART_RXEMPTY
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'rxempty', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

UART_EV_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx',  'bits': 1},{'name': 'rx',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

UART_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx',  'bits': 1},{'name': 'rx',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

UART_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx',  'bits': 1},{'name': 'rx',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

UART_TXEMPTY
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'txempty', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

UART_RXFULL
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'rxfull', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

JUNK_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

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

TIMER0_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'zero',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

TIMER0_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'zero',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

FLASH_CORE_MMAP_DUMMY_BITS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mmap_dummy_bits[7:0]', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

FLASH_CORE_MASTER_CS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'master_cs', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

FLASH_CORE_MASTER_PHYCONFIG
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'len',  'bits': 8},{'name': 'width',  'bits': 4},{'bits': 4},{'name': 'mask',  'bits': 8},{'bits': 8}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

FLASH_CORE_MASTER_RXTX
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'master_rxtx[31:0]', 'bits': 32}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

FLASH_CORE_MASTER_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'tx_ready',  'bits': 1},{'name': 'rx_ready',  'bits': 1},{'bits': 30}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

DEBUG_MODE_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

DEBUG_OEB_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

UART_ENABLED_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

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

USER_IRQ_4_IN
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_4_MODE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_4_EDGE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_4_EV_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_4_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_4_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_5_IN
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_5_MODE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_5_EDGE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_5_EV_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_5_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_5_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

FLASH_PHY_CLK_DIVISOR
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'clk_divisor[7:0]', 'attr': 'reset: 1', 'bits': 8},{'bits': 24},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 1 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 1}}"/></p>

USER_IRQ_2_IN
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_2_MODE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_2_EDGE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_2_EV_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_2_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_2_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_3_IN
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_3_MODE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_3_EDGE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_3_EV_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_3_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_3_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

SPI_ENABLED_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_ENA_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out[2:0]', 'bits': 3},{'bits': 29},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

MPRJ_WB_IENA_OUT
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'out', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_1_IN
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_1_MODE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_1_EDGE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_1_EV_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_1_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_1_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_0_IN
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'in', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_0_MODE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'mode', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_0_EDGE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'edge', 'bits': 1},{'bits': 31},], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_0_EV_STATUS
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_0_EV_PENDING
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

USER_IRQ_0_EV_ENABLE
<p><img src="https://svg.wavedrom.com/{'reg': [{'name': 'i0',  'bits': 1},{'bits': 31}], 'config': {'hspace': 400, 'bits': 32, 'lanes': 4 }, 'options': {'hspace': 400, 'bits': 32, 'lanes': 4}}"/></p>

