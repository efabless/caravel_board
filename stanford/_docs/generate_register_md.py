#!/usr/bin/env python3

import os
import subprocess
import argparse
import sys
import re

def usage():
    print('extract_wavedrom.py')


if __name__ == '__main__':

    dir_path = r'source'

    # list to store files
    files = []
    wd_flag = False
    wd_code = ""

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            files.append(path)
    print(files)

    outfile = open("caravel_registers.md", "w")

    for filename in files:
        print(filename)
        with open( "source/"+filename, "r" ) as f:
            line = f.readline()
            while line != '':
                line = line.strip()

                if line.startswith("|"):
                    line = line.replace(":ref:","").replace("`","").replace('=',' ').replace('+',' ').replace(":doc:","")
                    line = re.sub(r"<\w*>","",line)
                    print(line)
                    outfile.write(line + "\n")

                elif line.startswith("+="):
                    line = line.replace('=','-').replace('+','|')
                    print(line)
                    outfile.write(line + "\n")

                elif line.startswith("+-"):
                    pass
                    # line = line.replace('+','|')
                    # print(line)
                    # outfile.write("\n")

                elif line.startswith("`Address:"):
                    print(line)
                    outfile.write(line + "\n")

                elif line.startswith(".. wavedrom::"):
                    wd_code =" "
                    # while not line.startswith(':caption:'):
                    #     line = f.readline().strip()
                    # line = line.replace(':caption: ','')
                    # print(line)
                    # outfile.write(line + "\n")
                    while not line.startswith('{'):
                        line = f.readline().strip()
                    while not line.startswith('}'):
                        line = f.readline().strip()
                        line = line.replace('"',"'")
                        wd_code += line.strip()
                    # print("end")
                    wd_code = '<p><img src="https://svg.wavedrom.com/{' + wd_code.strip() + '"/></p>\n'
                    print(wd_code + "\n")
                    outfile.write(wd_code + "\n")

                elif line.startswith("^^^"):
                    outfile.write("\n")

                else:
                    outfile.write(line + "\n")

                line = f.readline()

    outfile.close()

            # reader = csv.reader(f, delimiter=",", skipinitialspace=True)
            # for i, line in enumerate(reader):
            #     if i != 0 and line[2] != 'TEST':
            #         if os.path.splitext(line[10].split('>')[1])[1] == '.gz':
            #             # p3 = subprocess.Popen( "gunzip -c", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True  )
            #             p2 = subprocess.Popen( "gunzip -c | shasum", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True  )
            #             p1 = subprocess.Popen( line[10].split('>')[0], stdout=p2.stdin, stderr=subprocess.PIPE, shell=True )
            #         else:
            #             p2 = subprocess.Popen( "shasum", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True  )
            #             p1 = subprocess.Popen( line[10].split('>')[0], stdout=p2.stdin, stderr=subprocess.PIPE, shell=True )
            #         stdout, stderr = p2.communicate()
            #         output = stdout.decode('utf-8')
            #         if output:
            #             hash = output.split(' ')[0]
            #         if hash == line[9]:
            #             check = '-- Matched-- '
            #         else:
            #             check = '** Error **'
            #
            #         print("{:02}:  slot = {}, project = {:<15}, id = {}, shasum = {} | {}".format(i, line[1], line[2][:15], line[3][1:], line[9], check))






