"""
HackSim v1.0 - A terminal-based hacking simulation game
All hacking is FAKE and simulated safely using Python data structures.
No real networking, sockets, or OS access is used.
"""

import time
import sys
import os
import random

# ─────────────────────────────────────────────
# FILESYSTEM DATA (pure Python dicts)
# ─────────────────────────────────────────────

FILESYSTEMS = {
    "home": {
        "/": {
            "notes.txt": (
                "== Personal Notes ==\n"
                "Remember: corp-server is running an old firewall (v2.1).\n"
                "Target: find the employee list and figure out who has admin access.\n"
                "Next step: get into bank-server and locate the accounts file.\n"
                "Stay ghost. Don't leave traces."
            ),
            "tools": {
                "readme.txt": (
                    "== HackSim Toolkit ==\n"
                    "Available exploits:\n"
                    "  firewall_bypass.sh  - bypasses legacy firewalls\n"
                    "  payload_inject.py   - injects reverse shell payload\n"
                    "  ghost_mode.sh       - masks your IP signature\n\n"
                    "Use 'hack <server>' to deploy these tools automatically."
                ),
                "ghost_mode.sh": (
                    "#!/bin/bash\n"
                    "# Ghost Mode - masks IP signature\n"
                    "echo 'Routing traffic through 7 anonymous nodes...'\n"
                    "echo 'Identity masked.'"
                ),
            },
        }
    },

    "corp-server": {
        "/": {
            "employees.txt": (
                "== APEX Corp - Employee Directory ==\n\n"
                "CEO      : John Smith      | Access Level: 5 | Hint: favourite colour\n"
                "CTO      : Alice Wang      | Access Level: 5 | Hint: childhood pet name\n"
                "HR Lead  : Marcus Bell     | Access Level: 3 | Hint: birth year\n"
                "Intern   : Dana Torres     | Access Level: 1 | Hint: 'password123' (seriously)\n\n"
                "NOTE: Admin panel located on bank-server. CEO has master credentials."
            ),
            "passwords.txt": (
                "== APEX Corp - Hashed Credentials (DO NOT SHARE) ==\n\n"
                "j.smith   : 5f4dcc3b5aa765d61d8327deb882cf99  (MD5)\n"
                "a.wang    : 7c4a8d09ca3762af61e59520943dc26c  (MD5)\n"
                "m.bell    : 25d55ad283aa400af464c76d713c07ad  (MD5)\n\n"
                "Hint: John's password is his favourite colour + '2024'"
            ),
            "internal": {
                "memo.txt": (
                    "INTERNAL MEMO - CONFIDENTIAL\n"
                    "Date: 2047-03-15\n\n"
                    "All staff: the new bank integration goes live Friday.\n"
                    "The master override code has been stored in bank-server/secret.txt\n"
                    "Only share with Level-5 personnel."
                ),
                "server_map.txt": (
                    "== APEX Infrastructure Map ==\n\n"
                    "corp-server   (this machine)  - HR & employee data\n"
                    "bank-server                   - financial records & vault\n"
                    "email-server                  - executive communications\n"
                    "shadow-server                 - ??? (unknown, heavily encrypted)"
                ),
            },
        }
    },