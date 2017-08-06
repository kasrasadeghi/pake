#!python

import os
import subprocess


def c(command):
    print(f"$ {command}")
    subprocess.call(command.split())


def main():
    file = open("pakefile", "r", encoding="utf-8")
    for line in file:
        evaluate(line)


def evaluate(line):
    parts = line.split()
    cmd = parts[0]
    if cmd == "temp":
        temp = parts[1]
        print(f"pake: tempdir: {temp}")
        
        c(f"rm -rf {temp}")
        c(f"mkdir {temp}")
        for file in os.listdir("."):
            if os.path.isfile(file):
                c(f"cp {file} {temp}")

    elif cmd == "cmake":
        target = parts[1]
        print(f"pake: making target: {target}")

        c(f"cmake --build --target {target} -- -j 4 .")


if __name__ == "__main__":
    main()
