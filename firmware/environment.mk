#======================================
# environment.mk
#======================================
# Sets environment variables for
# RISCV compilation

# USERS: CHANGE BELOW FOLLOWING LINE
#----------------------------------------------------

# Set path to RISCV toolchain
TOOLCHAIN_PATH=/usr/local/bin/

# Set prefix of RISCV toolchain
TOOLCHAIN_PREFIX=riscv64
#----------------------------------------------------
# USERS: CHANGE ABOVE PREVIOUS LINE

# Set architecture target based on version
RV_GCC=$(TOOLCHAIN_PATH)$(TOOLCHAIN_PREFIX)-unknown-elf-gcc

# Get version, and see if it's greater than 11.1.0
NEED_ZICSR=$(shell expr `$(RV_GCC) -dumpversion | sed -e 's/\.\([0-9][0-9]\)/\1/g' -e 's/\.\([0-9]\)/0\1/g' -e 's/^[0-9]\{3,4\}$$/&00/'` \>= 110100)

ifeq "$(NEED_ZICSR)" "1"
	TARGET_ARCH=rv32i_zicsr
else
	TARGET_ARCH=rv32i
endif