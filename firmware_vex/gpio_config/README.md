# GPIO Configuration

This directory provides utilities for configuring GPIO for MPW-2.  The utility for building the stream are `gpio_config_builder.py` and it uses `gpio config_def.py` for the definition of the chain and the target configs.

`gpio_config_builder.py` creates two files: 
* `gpio_config_data.c`
* `gpio_config_data.py`

`gpio_config_io.c` which can be included into the user program and it includes the routine gpio_config_io() along with the stream that will configure the io.

`debug_io.c` is the firmware example that uses it

## GPIO Config Simulator

TO BE COMPLETED