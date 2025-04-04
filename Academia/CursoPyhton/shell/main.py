#!/usr/bin/env python3
import signal
import sys
from forwardshell import ForwardShell 

def def_handler(sig, frame):
    print(f"\n\n[!]Saliendo...\n")
    my_fordwarshell.remove_data()
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

if __name__ == '__main__':
    my_fordwarshell = ForwardShell()
    my_fordwarshell.run()
