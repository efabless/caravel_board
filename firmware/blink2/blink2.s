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

#sw x0, 0(x11)   # LED on
#sw x1, 0(x11)   # LED off

bigloop:

#li x5, 100
#loop:
#addi x5, x5, -1
#bne x5, zero, loop
call delay

#sw x1, 0(x11)   # LED off
sw x0, 0(x11)   # LED on

#li x3, 100
#loop2:
#addi x3, x3, -1
#bne x3, zero, loop2
call delay

#sw x0, 0(x11)   # LED on
sw x1, 0(x11)   # LED off

nop
nop

call delay
sw x0, 0(x11)   # LED on

#beqz zero, bigloop

done:
beqz zero, done

delay:
li x10, 10
dloop:
addi x10, x10, -1
bne x10, x0, dloop
ret

