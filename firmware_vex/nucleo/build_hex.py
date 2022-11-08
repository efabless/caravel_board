import os, io

filenames_h = ["config_io_o_h_1.hex", "config_io_o_h_2.hex"]
filenames_l = ["config_io_o_l_1.hex", "config_io_o_l_2.hex"]

print("starting config_io_o_h.hex")

with open("config_io_o_h.hex", "w") as outfile:
    for names in filenames_h:
        with open(names) as infile:
            outfile.write(infile.read())
            print(".")
        os.remove(names)
outfile.close()

print("starting config_io_o_l.hex")

with open("config_io_o_l.hex", "w") as outfile:
    for names in filenames_l:
        with open(names) as infile:
            outfile.write(infile.read())
        print(".")
        os.remove(names)
outfile.close()

print("done.")
