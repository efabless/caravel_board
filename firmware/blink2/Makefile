# SPDX-FileCopyrightText: 2020 Efabless Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

TOOLCHAIN_PATH = /opt/riscv32imc/bin
# TOOLCHAIN_PATH = /ef/apps/bin/

FIRMWARE_PATH = ..
GCC_PATH?=/ef/apps/bin
GCC_PREFIX?=riscv32-unknown-elf

.SUFFIXES:

PATTERN = blink2

all:  ${PATTERN:=.hex}

hex:  ${PATTERN:=.hex}

%.elf: %.s $(FIRMWARE_PATH)/sections.lds
	${TOOLCHAIN_PATH}/${GCC_PREFIX}-gcc -O0 -march=rv32i -mabi=ilp32 -Wl,-Bstatic,-T,$(FIRMWARE_PATH)/sections.lds,--strip-debug -ffreestanding -nostdlib -o $@ $<
	${TOOLCHAIN_PATH}/riscv32-unknown-elf-objdump -D blink2.elf > blink2.lst

%.hex: %.elf
	${TOOLCHAIN_PATH}/${GCC_PREFIX}-objcopy -O verilog $< $@
	# to fix flash base address
	sed -i '.orig' -e 's/@10000000/@00000000/g' $@

flash: blink2.hex
	python3 ../util/caravel_hkflash.py $<

flash2: blink2.hex
	python3 ../util/caravel_flash.py $<

# ---- Clean ----

clean:
	rm -f *.elf *.hex *.bin *.vvp *.vcd *.log

.PHONY: clean hex all

