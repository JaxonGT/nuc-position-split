import os, sys

path = "."

for file in os.listdir(path):
    if file.endswith(".fas"):

        headers = []
        lines = []
        doubles = []
        singles = []

        f = open(file, "r")
        for line in f:
            if line.startswith(">"):
                headers.append(line)
            else:
                lines.append(line)

        f.close()

        for n in range(len(lines)):
            doubles.append("")
            singles.append("")

        for i in range(0, len(lines[0]), 3):
            if i+2 < len(lines[0]):
                for j in range(len(lines)):
                    doubles[j] = doubles[j] + lines[j][i] + lines[j][i+1]
                    singles[j] = singles[j] + lines[j][i+2]

        
        for m in range(len(doubles)):
            doubles[m] = doubles[m] + '\n'
            singles[m] = singles[m] + '\n'

        fdoubles = open(file.replace(".fas","_doubles.fas"), "w")
        fsingles = open(file.replace(".fas","_singles.fas"), "w")

        for k in range(len(headers)):
            fdoubles.write(headers[k])
            fsingles.write(headers[k])
            fdoubles.write(doubles[k])
            fsingles.write(singles[k])
            
        fdoubles.close()
        fsingles.close()