# GPIO Configuration

This directory provides utilities for configuring GPIO for MPW-2.  The utility for building the stream are `gpio_config_builder.py` and it uses `gpio config_def.py` for the definition of the chain and the target configs.

`gpio_config_builder.py` takes two files as input,
* `gpio_config_def.py`
* `gpio_config_io.py`

The `gpio_config_def.py` is obtained from running gpio characterization for your
part on the Nucleo test setup.  This will be the same for all firmware for that 
specific part.

`gpio_config_io.py` provide the specific IO configuration required for your firmware.  This could vary for each
firmware build based on your needs.  IO configuration include MGMT vs USER AREA, input vs output, as well as PU/PD
termination resistors for inputs.

From these inputs, it then generates two files: 
* `gpio_config_data.c`
* `gpio_config_data.py`

`gpio_config_io.c` which can be included into the user program and it includes the routine gpio_config_io() along with the stream that will configure the io.

`debug_io.c` is the firmware example that uses it

## GPIO Config Simulator

TO BE COMPLETED