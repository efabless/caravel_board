# number of IO in the configuration stream for each chain
NUM_IO = 19

# defines these values for IO configurations
C_MGMT_OUT = 0
C_MGMT_IN = 1
C_USER_BIDIR = 2
C_DISABLE = 3
C_ALL_ONES = 4
C_USER_BIDIR_WPU = 5
C_USER_BIDIR_WPD = 6
C_USER_IN_NOPULL = 7
C_USER_OUT = 8

config_h = [
    C_USER_OUT,  #37
    C_USER_OUT,  #36
    C_USER_OUT,  #35
    C_USER_OUT,  #34
    C_USER_OUT,  #33
    C_USER_OUT,  #32
    C_USER_OUT,  #31
    C_USER_OUT,  #30
    C_USER_OUT,  #29
    C_USER_OUT,  #28
    C_USER_OUT,  #27
    C_USER_OUT,  #26
    C_USER_OUT,  #25
    C_USER_OUT,  #24
    C_USER_OUT,  #23
    C_USER_OUT,  #22
    C_USER_OUT,  #21
    C_USER_OUT,  #20
    C_USER_OUT,  #19
]

del config_h[NUM_IO:]

config_l = [
    C_USER_OUT,   #0
    C_USER_OUT,   #1
    C_USER_OUT,   #2
    C_USER_OUT,   #3
    C_USER_OUT,   #4
    C_USER_OUT,   #5
    C_USER_OUT,   #6
    C_USER_OUT,   #7
    C_USER_OUT,   #8
    C_USER_OUT,   #9
    C_USER_OUT,   #10
    C_USER_OUT,   #11
    C_USER_OUT,   #12
    C_USER_OUT,   #13
    C_DISABLE,   #14
    C_DISABLE,   #15
    C_DISABLE,   #16
    C_DISABLE,   #17
    C_DISABLE,   #18
]

del config_l[NUM_IO:]