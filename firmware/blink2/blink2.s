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

la s2, 0x21000000
sw zero, 4(s2)
sw zero, 8(s2)
sw zero, 12(s2)

#sw zero, 0(s2)   # LED on
#sw s1, 0(s2)   # LED off

bigloop:
li s1, 1
sw s1, 0(s2)   # LED off
nop
nop
nop


#li x5, 100
#loop:
#addi x5, x5, -1
#bne x5, zero, loop
call delay

#sw s1, 0(s2)   # LED off
sw zero, 0(s2)   # LED on
nop
nop
nop

#li x3, 100
#loop2:
#addi x3, x3, -1
#bne x3, zero, loop2
call delay

#sw zero, 0(s2)   # LED on
li s1, 1
sw s1, 0(s2)   # LED off

nop
nop
nop

call delay
sw zero, 0(s2)   # LED on

beqz zero, bigloop

done:
beqz zero, done

delay:
li s3, 3000
dloop:
addi s3, s3, -1
bne s3, zero, dloop
ret

