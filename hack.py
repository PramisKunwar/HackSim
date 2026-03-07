import time, sys, os, random

# ANSI color helpers
C = {'green': '92', 'red': '91', 'yellow': '93', 'cyan': '96', 'bold': '1'}
def color(t, c): return f"\033[{c}m{t}\033[0m"
green = lambda t: color(t, C['green'])
red = lambda t: color(t, C['red'])
yellow = lambda t: color(t, C['yellow'])
cyan = lambda t: color(t, C['cyan'])
bold = lambda t: color(t, C['bold'])

def slow_print(t, d=0.03):
    for ch in t: sys.stdout.write(ch); sys.stdout.flush(); time.sleep(d)
    print()

def animated_print(lines, d=0.6):
    for l in lines: slow_print(l, 0.02); time.sleep(d)

def clear_screen(): os.system('cls' if os.name == 'nt' else 'clear')

# ---------- FAKE FILESYSTEM DATA ----------
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

# ---------- SERVER CLASS (with integrated filesystem) ----------
class Server:
    def __init__(self, name, fs_tree):
        self.name = name
        self.tree = fs_tree
        self.cwd_path = []  # empty = root

    def _resolve(self, path_parts):
        node = self.tree["/"]
        for p in path_parts:
            if isinstance(node, dict) and p in node: node = node[p]
            else: return None
        return node

    def pwd(self): return '/' + '/'.join(self.cwd_path) if self.cwd_path else '/'

    def ls(self):
        node = self._resolve(self.cwd_path)
        if not isinstance(node, dict): return red("Error: cannot list.")
        items = [cyan(n+'/') if isinstance(c,dict) else green(n) for n,c in node.items()]
        return '  '.join(items) if items else '(empty)'

    def cd(self, target):
        if target == '..':
            if self.cwd_path: self.cwd_path.pop()
            return ''
        node = self._resolve(self.cwd_path)
        if target not in node or not isinstance(node[target], dict):
            return red(f"cd: {target}: Not a directory")
        self.cwd_path.append(target)
        return ''

    def cat(self, fname):
        node = self._resolve(self.cwd_path)
        if fname not in node: return red(f"cat: {fname}: No such file")
        if isinstance(node[fname], dict): return red(f"cat: {fname}: Is a directory")
        return node[fname]

    def reset_path(self): self.cwd_path = []

# ---------- MAIN GAME CLASS ----------
class Game:
    def __init__(self):
        self.alias = ''
        self.servers = {name: Server(name, tree) for name, tree in FILESYSTEMS.items()}
        self.locked = set(LOCKED_SERVERS)
        self.current_server = None

    def boot(self):
        clear_screen()
        logo = [
            bold(green("  ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██╗███╗   ███╗")),
            bold(green("  ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██║████╗ ████║")),
            bold(green("  ███████║███████║██║     █████╔╝ ███████╗██║██╔████╔██║")),
            bold(green("  ██╔══██║██╔══██║██║     ██╔═██╗ ╚════██║██║██║╚██╔╝██║")),
            bold(green("  ██║  ██║██║  ██║╚██████╗██║  ██╗███████║██║██║ ╚═╝ ██║")),
            bold(green("  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝     ╚═╝")),
            "",
            cyan("                   HackSim v1.0 — Hacking Simulator"),
            yellow("          [ All systems, targets, and exploits are FICTIONAL ]"),
            "",
        ]
        for l in logo: print(l); time.sleep(0.05)
        animated_print([
            "Initializing hacking interface...",
            "Loading exploit modules........... OK",
            "Configuring anonymous routing...... OK",
            "Connecting to darknet.............. OK",
            "Establishing secure shell.......... OK",
            "",
            green("  Access granted."),
            ""
        ], 0.35)

    def login(self):
        self.alias = input(yellow("Enter your hacker alias: ")).strip() or 'ghost'
        print(); slow_print(green(f"  Welcome, {self.alias}.") + "  Type " + cyan("help") + " to see available commands.\n")
        self.current_server = self.servers["home"]

    def prompt(self):
        fs = self.current_server
        return f"{bold(green(self.alias))}@{bold(cyan(fs.name))}:{yellow(fs.pwd())}$ "

    def run(self):
        while True:
            try: raw = input(self.prompt()).strip()
            except (EOFError, KeyboardInterrupt): print(); self.cmd_exit([]); break
            if not raw: continue
            parts = raw.split()
            cmd, args = parts[0].lower(), parts[1:]
            dispatch = {
                "help": self.cmd_help, "clear": self.cmd_clear, "whoami": self.cmd_whoami,
                "ls": self.cmd_ls, "cd": self.cmd_cd, "cat": self.cmd_cat,
                "scan": self.cmd_scan, "connect": self.cmd_connect, "disconnect": self.cmd_disconnect,
                "hack": self.cmd_hack, "exit": self.cmd_exit, "quit": self.cmd_exit
            }
            if cmd in dispatch: dispatch[cmd](args)
            else: print(red(f"  Command not found: '{cmd}'") + "  (type " + cyan("help") + " for commands)")

    # ----- commands -----
    def cmd_help(self, _):
        print("\n" + bold(cyan("  ╔══════════════════════════════════════════╗")))
        print(bold(cyan("  ║          HackSim Command Reference       ║")))
        print(bold(cyan("  ╚══════════════════════════════════════════╝")))
        for cmd, desc in [
            ("help", "Show this help message"), ("clear", "Clear the screen"),
            ("whoami", "Display your hacker alias"), ("scan", "List all known servers"),
            ("connect <server>", "Connect to an unlocked server"), ("disconnect", "Return to home server"),
            ("hack <server>", "Attempt to hack a locked server"), ("ls", "List files in current directory"),
            ("cd <dir>", "Change directory (use '..' to go up)"), ("cat <file>", "Read a file"),
            ("exit", "Quit HackSim")
        ]: print(f"  {green(cmd):<30}  {desc}")
        print()

    def cmd_clear(self, _): clear_screen()
    def cmd_whoami(self, _): print(f"  {yellow(self.alias)}")
    def cmd_ls(self, _): print("  " + self.current_server.ls())
    def cmd_cd(self, args):
        if not args: print(red("  Usage: cd <directory>")); return
        r = self.current_server.cd(args[0])
        if r: print("  " + r)
    def cmd_cat(self, args):
        if not args: print(red("  Usage: cat <filename>")); return
        content = self.current_server.cat(args[0])
        print("\n" + "\n".join("  " + l for l in content.split("\n")) + "\n")

    def cmd_scan(self, _):
        print("\n  " + bold("Known servers:"))
        for n in self.servers:
            if n in self.locked: status = red("[LOCKED]  ")
            elif n == self.current_server.name: status = green("[CONNECTED]")
            else: status = yellow("[UNLOCKED]")
            print(f"    {status}  {n}")
        print()

    def cmd_connect(self, args):
        if not args: print(red("  Usage: connect <server>")); return
        name = args[0]
        if name not in self.servers: print(red(f"  Error: Server '{name}' not found.")); return
        if name in self.locked: print(red(f"  Access denied — '{name}' is locked. Use 'hack {name}' first.")); return
        self.servers[name].reset_path()
        self.current_server = self.servers[name]
        print(green(f"  Connected to {name}."))

    def cmd_disconnect(self, _):
        if self.current_server.name == "home": print(yellow("  Already on home server.")); return
        self.current_server = self.servers["home"]
        self.servers["home"].reset_path()
        print(green("  Disconnected. Returned to home server."))

    def cmd_hack(self, args):
        if not args: print(red("  Usage: hack <server>")); return
        name = args[0]
        if name not in self.servers: print(red(f"  Error: Target '{name}' not found.")); return
        if name == "home": print(yellow("  You can't hack your own machine.")); return
        if name not in self.locked: print(yellow(f"  '{name}' is already unlocked. Use 'connect {name}' to access it.")); return

        print("\n" + bold(yellow(f"  [ INITIATING HACK: {name.upper()} ]")) + "\n")
        for step in HACK_SCRIPTS.get(name, ["Scanning target...", "Locating vulnerabilities...", "Deploying exploit..."]):
            time.sleep(random.uniform(0.4, 0.9))
            slow_print(f"  {cyan('>')} {step}", 0.015)

        print("\n  " + yellow("Cracking: [ "), end='')
        for _ in range(30): sys.stdout.write(green("█")); sys.stdout.flush(); time.sleep(random.uniform(0.03, 0.12))
        print(yellow(" ] 100%"))
        time.sleep(0.3)
        print(); slow_print(bold(green(f"  ✓ Access granted. '{name}' is now unlocked.")), 0.02); print()
        self.locked.discard(name)

    def cmd_exit(self, _):
        print(); slow_print(yellow("  Closing secure tunnel..."), 0.03); time.sleep(0.4)
        slow_print(yellow("  Wiping session logs..."), 0.03); time.sleep(0.4)
        slow_print(green("  Stay ghost. Goodbye."), 0.03); print()
        sys.exit(0)

def main():
    game = Game()
    game.boot()
    game.login()
    game.run()

if __name__ == "__main__": main()