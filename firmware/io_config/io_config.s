# SPDX-FileCopyrightText: 2020 Efabless Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# SPDX-License-Identifier: Apache-2.0

.section .text

start:

la x11, 0x21000000
li x1, 1
sw x1, 0(x11)   # LED off
sw x0, 4(x11)
sw x0, 8(x11)
sw x0, 12(x11)

li x1, 0x1809        # GPIO_MODE_MGMT_STD_OUTPUT
#li x1, 0x0c03        # GPIO_MODE_MGMT_STD_INPUT_PULLUP

# configure user IO regs
la x2, 0x26000024    # reg_mprj_io_0
sw x1, 0(x2)  # 0
sw x1, 0(x2)  # 1
sw x1, 4(x2)  # 2
sw x1, 8(x2)  # 3
sw x1, 12(x2) # 4
sw x1, 16(x2) # 5
sw x1, 20(x2) # 5
sw x1, 24(x2) # 5
sw x1, 28(x2) # 5
sw x1, 32(x2) # 5
sw x1, 36(x2) # 5
sw x1, 40(x2) # 5
sw x1, 44(x2) # 5
sw x1, 48(x2) # 5
sw x1, 52(x2) # 5
sw x1, 56(x2) # 5
sw x1, 60(x2) # 5
sw x1, 64(x2) # 5
sw x1, 68(x2) # 5
sw x1, 72(x2) # 5
sw x1, 76(x2) # 5
sw x1, 80(x2) # 5
sw x1, 84(x2) # 5
sw x1, 88(x2) # 5
sw x1, 92(x2) # 5
sw x1, 96(x2) # 5
sw x1, 100(x2) # 5
sw x1, 104(x2) # 5
sw x1, 108(x2) # 5
sw x1, 112(x2) # 5
sw x1, 116(x2) # 5
sw x1, 120(x2) # 5
sw x1, 124(x2) # 5
sw x1, 128(x2) # 5
sw x1, 132(x2) # 5
sw x1, 136(x2) # 5
sw x1, 142(x2) # 36
sw x1, 148(x2) # 37

# set data value
li x12, 0xffffffff
la x5, 0x2600000c    # reg_mprj_datal
sw x12, 0(x5)

la x6, 0x26000000    # reg_mprj_xfer
li x1, 1
sw x1, 0(x6)
nop
nop
nop
nop

wait:
#lw x7, 0(x2)
nop
nop
#beq x7, x1, wait
nop
nop

sw x0, 0(x11)   # LED on

nop
nop
nop
nop
nop

done:
beqz zero, done



