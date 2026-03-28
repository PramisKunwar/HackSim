FILESYSTEMS = {
    "home": {"/": {
        "notes.txt": "== Personal Notes ==\nRemember: corp-server is running an old firewall (v2.1).\nTarget: find the employee list and figure out who has admin access.\nNext step: get into bank-server and locate the accounts file.\nStay ghost. Don't leave traces.",
        "tools": {
            "readme.txt": "== HackSim Toolkit ==\nAvailable exploits:\n  firewall_bypass.sh  - bypasses legacy firewalls\n  payload_inject.py   - injects reverse shell payload\n  ghost_mode.sh       - masks your IP signature\n\nUse 'hack <server>' to deploy these tools automatically.",
            "ghost_mode.sh": "#!/bin/bash\n# Ghost Mode - masks IP signature\necho 'Routing traffic through 7 anonymous nodes...'\necho 'Identity masked.'"
        }
    }},
    "corp-server": {"/": {
        "employees.txt": "== APEX Corp - Employee Directory ==\n\nCEO      : John Smith      | Access Level: 5 | Hint: favourite colour\nCTO      : Alice Wang      | Access Level: 5 | Hint: childhood pet name\nHR Lead  : Marcus Bell     | Access Level: 3 | Hint: birth year\nIntern   : Dana Torres     | Access Level: 1 | Hint: 'password123' (seriously)\n\nNOTE: Admin panel located on bank-server. CEO has master credentials.",
        "passwords.txt": "== APEX Corp - Hashed Credentials (DO NOT SHARE) ==\n\nj.smith   : 5f4dcc3b5aa765d61d8327deb882cf99  (MD5)\na.wang    : 7c4a8d09ca3762af61e59520943dc26c  (MD5)\nm.bell    : 25d55ad283aa400af464c76d713c07ad  (MD5)\n\nHint: John's password is his favourite colour + '2024'",
        "internal": {
            "memo.txt": "INTERNAL MEMO - CONFIDENTIAL\nDate: 2047-03-15\n\nAll staff: the new bank integration goes live Friday.\nThe master override code has been stored in bank-server/secret.txt\nOnly share with Level-5 personnel.",
            "server_map.txt": "== APEX Infrastructure Map ==\n\ncorp-server   (this machine)  - HR & employee data\nbank-server                   - financial records & vault\nemail-server                  - executive communications\nshadow-server                 - ??? (unknown, heavily encrypted)"
        }
    }},
    "bank-server": {"/": {
        "accounts.txt": "== NovBank - Account Ledger ==\n\nACC-0001  | John Smith    | $4,200,000  | STATUS: Active\nACC-0002  | Alice Wang    | $   87,500  | STATUS: Active\nACC-0003  | APEX Corp     | $92,400,000 | STATUS: Frozen\nACC-0099  | [REDACTED]    | $???        | STATUS: Hidden\n\nSuspicious transfer detected on ACC-0003 — see secret.txt",
        "secret.txt": "== CLASSIFIED ==\n\nBANK MASTER OVERRIDE PASSWORD: 7391-NOVA-DELTA\n\nThis code grants full read/write access to all accounts.\nAuthorised personnel only. Misuse is a federal offence.\n\nNote from CEO: 'Nobody will ever find this file.' – J.S.",
        "vault": {
            "transfer_log.txt": "== TRANSFER LOG - LAST 30 DAYS ==\n\n2047-03-01  ACC-0003 → OFFSHORE-77  $10,000,000  [FLAGGED]\n2047-03-08  ACC-0003 → OFFSHORE-77  $15,000,000  [FLAGGED]\n2047-03-14  ACC-0003 → OFFSHORE-77  $20,000,000  [FLAGGED]\n\nInvestigation pending. Contact: regulator@novbank.sim"
        }
    }},
    "email-server": {"/": {
        "inbox": {
            "ceo_email.txt": "FROM : j.smith@apexcorp.sim\nTO   : board@apexcorp.sim\nSUBJ : Urgent - Cover Tracks\n\nThe transfers are done. Make sure nobody finds the log files.\nI've stored the master password on the bank server — it's safe there.\nDelete this email after reading.\n\n– J.S.",
            "it_alert.txt": "FROM : security@apexcorp.sim\nTO   : admin@apexcorp.sim\nSUBJ : INTRUSION ALERT\n\nWARNING: Unauthorised access detected on corp-server at 03:42 UTC.\nSource IP masked. Ghost-mode signature detected.\nRecommend immediate password rotation."
        },
        "sent": {
            "offshore_contact.txt": "FROM : j.smith@apexcorp.sim\nTO   : contact@offshore-77.sim\nSUBJ : Packages Delivered\n\nAll three transfers complete. Total: $45M.\nDestroy this thread. The auditors won't look until Q4."
        }
    }},
    "shadow-server": {"/": {
        "WARNING.txt": "╔══════════════════════════════════════════╗\n║   YOU SHOULD NOT BE HERE             ║\n║                                      ║\n║   This server belongs to GHOST NET   ║\n║   The people who built the darknet.  ║\n║                                      ║\n║   We've been watching you, hacker.   ║\n║   Nice work on APEX Corp.            ║\n║                                      ║\n║   – G                                ║\n╚══════════════════════════════════════════╝",
        "recruitment.txt": "== GHOST NET - RECRUITMENT FILE ==\n\nYou've proven you can navigate our world.\nWe've observed your work on corp-server, bank-server, and email-server.\n\nIf you want to go deeper, you know where to find us.\n\nThere is no next level. There is only the void.\n\nOr maybe there is. Keep digging.\n\n– GHOST NET"
    }}
}

LOCKED_SERVERS = {"corp-server", "bank-server", "email-server", "shadow-server"}

HACK_SCRIPTS = {
    "corp-server": ["Scanning open ports on corp-server...", "Port 22 (SSH) — OPEN", "Port 443 (HTTPS) — OPEN", "Loading firewall_bypass.sh...", "Bypassing legacy firewall v2.1... done", "Injecting payload into auth module...", "Privilege escalation... SUCCESS", "Establishing encrypted tunnel..."],
    "bank-server": ["Scanning bank-server infrastructure...", "Detected: NovBank SecureOS v4.7", "Loading payload_inject.py...", "Exploiting CVE-FAKE-2047-0001... done", "Bypassing 2FA token generator...", "Cracking AES-256 session key... (this may take a moment)", "Key cracked: 0xDEADBEEFCAFE", "Root access obtained..."],
    "email-server": ["Scanning email-server...", "Detected: MailOS Enterprise 9.2", "Spoofing admin credentials...", "Injecting OAuth token...", "Bypassing spam filter firewall...", "IMAP root shell obtained..."],
    "shadow-server": ["Scanning shadow-server...", "WARNING: No open ports detected", "Switching to darknet routing...", "Peeling back 12 layers of encryption...", "Something is wrong — the server is scanning YOU back", "Deploying countermeasures...", "Establishing handshake with unknown entity...", "Connection accepted... by choice?"]
}