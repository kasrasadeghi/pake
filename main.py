#!/bin/python

import os
import subprocess
import sys


def c(command):
    print(f"$ {command}")
    subprocess.call(command.split())


def main():
    if len(sys.argv) > 2:
        command = " ".join(sys.argv[1:])
        evaluate(command)
    elif len(sys.argv) > 1:
        evaluate(sys.argv[1])
    else:
        file = open("pakefile", "r", encoding="utf-8")
        for line in file:
            evaluate(line)


def evaluate(line):
    parts = line.split()
    cmd = parts[0]
    temp = "build"
    if cmd == "temp":
        if len(parts) != 1:
            temp = parts[1]
        print(f"pake: tempdir: {temp}")

        c(f"rm -rf {temp}")
        c(f"mkdir {temp}")
        for file in os.listdir("."):
            if os.path.isfile(file):
                c(f"cp {file} {temp}")

    elif cmd == "cmake":
        os.chdir(temp)
        wd = os.getcwd()
        print("running cmake")
        c("cmake .")
        c("make")
        os.chdir("..")

    elif cmd == "test":
        target = parts[1]
        print(f"pake: testing: {target}")
        c(f"./{temp}/{target}")


if __name__ == "__main__":
    main()
