#!/usr/bin/env python3
"""
Cybrary Python for Security - Module 1
Script: 01_system_checker.py
Objective: System Environment & Host Security Auditor
"""

import sys
import os
import platform
import socket

def audit_host():
    print("=" * 55)
    print("      CYBERSECURITY HOST ENVIRONMENT AUDIT REPORT      ")
    print("=" * 55)
    
    # OS and Architecture Details
    print(f"[+] Operating System : {platform.system()} {platform.release()}")
    print(f"[+] Kernel Version   : {platform.version()}")
    print(f"[+] Architecture     : {platform.machine()}")
    print(f"[+] Hostname         : {socket.gethostname()}")
    
    # User Execution Context
    euid = os.geteuid() if hasattr(os, 'geteuid') else 'N/A'
    print(f"[+] Effective User ID: {euid} ({'ROOT/SUDO' if euid == 0 else 'Standard User'})")
    
    # Python Runtime Audit
    print(f"[+] Python Executable: {sys.executable}")
    print(f"[+] Python Version   : {sys.version.split()[0]}")
    print("=" * 55)

if __name__ == "__main__":
    audit_host()
