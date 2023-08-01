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

la s4, 0x21000000
li s1, 1
sw s1, 0(s4)   # LED off
sw zero, 4(s4)
sw zero, 8(s4)
sw zero, 12(s4)

li s1, 0x1809        # GPIO_MODE_MGMT_STD_OUTPUT
#li s1, 0x0c03        # GPIO_MODE_MGMT_STD_INPUT_PULLUP

# configure user IO regs
la s2, 0x26000024    # reg_mprj_io_0
#sw s1, 0(s2)  # 0
#sw s1, 4(s2)  # 1
#sw s1, 8(s2)  # 2
#sw s1, 12(s2) # 3
#sw s1, 16(s2) # 4
#sw s1, 20(s2) # 5
#sw s1, 24(s2) # 7
sw s1, 28(s2) # 8
sw s1, 32(s2) # 9
sw s1, 36(s2) # 10
sw s1, 40(s2) # 11

la s6, 0x26000000    # reg_mprj_xfer
li s1, 1
sw s1, 0(s6)
nop
nop
nop
nop

wait:
lw s7, 0(x6)
nop
nop
bnez s7, wait
nop
nop

# set data value
li s5, 0xffffff80
la s3, 0x2600000c    # reg_mprj_datal
sw s5, 0(s3)

sw zero, 0(s4)   # LED on

nop
nop
nop
nop
nop

done:
beqz zero, done



