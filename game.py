import time
import sys
import random
from colors import green, red, yellow, cyan, bold
from utils import slow_print, animated_print, clear_screen
from data import FILESYSTEMS, LOCKED_SERVERS, HACK_SCRIPTS
from server import Server

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
        for l in logo: 
            print(l)
            time.sleep(0.05)
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
        print()
        slow_print(green(f"  Welcome, {self.alias}.") + "  Type " + cyan("help") + " to see available commands.\n")
        self.current_server = self.servers["home"]

    def prompt(self):
        fs = self.current_server
        return f"{bold(green(self.alias))}@{bold(cyan(fs.name))}:{yellow(fs.pwd())}$ "

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
        ]: 
            print(f"  {green(cmd):<30}  {desc}")
        print()

    def cmd_clear(self, _): 
        clear_screen()
        
    def cmd_whoami(self, _): 
        print(f"  {yellow(self.alias)}")
        
    def cmd_ls(self, _): 
        print("  " + self.current_server.ls())
        
    def cmd_cd(self, args):
        if not args: 
            print(red("  Usage: cd <directory>"))
            return
        r = self.current_server.cd(args[0])
        if r: 
            print("  " + r)
            
    def cmd_cat(self, args):
        if not args: 
            print(red("  Usage: cat <filename>"))
            return
        content = self.current_server.cat(args[0])
        print("\n" + "\n".join("  " + l for l in content.split("\n")) + "\n")

    def cmd_scan(self, _):
        print("\n  " + bold("Known servers:"))
        for n in self.servers:
            if n in self.locked: 
                status = red("[LOCKED]  ")
            elif n == self.current_server.name: 
                status = green("[CONNECTED]")
            else: 
                status = yellow("[UNLOCKED]")
            print(f"    {status}  {n}")
        print()

    def cmd_connect(self, args):
        if not args: 
            print(red("  Usage: connect <server>"))
            return
        name = args[0]
        if name not in self.servers: 
            print(red(f"  Error: Server '{name}' not found."))
            return
        if name in self.locked: 
            print(red(f"  Access denied — '{name}' is locked. Use 'hack {name}' first."))
            return
        self.servers[name].reset_path()
        self.current_server = self.servers[name]
        print(green(f"  Connected to {name}."))

    def cmd_disconnect(self, _):
        if self.current_server.name == "home": 
            print(yellow("  Already on home server."))
            return
        self.current_server = self.servers["home"]
        self.servers["home"].reset_path()
        print(green("  Disconnected. Returned to home server."))

    def cmd_hack(self, args):
        if not args: 
            print(red("  Usage: hack <server>"))
            return
        name = args[0]
        if name not in self.servers: 
            print(red(f"  Error: Target '{name}' not found."))
            return
        if name == "home": 
            print(yellow("  You can't hack your own machine."))
            return
        if name not in self.locked: 
            print(yellow(f"  '{name}' is already unlocked. Use 'connect {name}' to access it."))
            return

        print("\n" + bold(yellow(f"  [ INITIATING HACK: {name.upper()} ]")) + "\n")
        for step in HACK_SCRIPTS.get(name, ["Scanning target...", "Locating vulnerabilities...", "Deploying exploit..."]):
            time.sleep(random.uniform(0.4, 0.9))
            slow_print(f"  {cyan('>')} {step}", 0.015)

        print("\n  " + yellow("Cracking: [ "), end='')
        for _ in range(30): 
            sys.stdout.write(green("█"))
            sys.stdout.flush()
            time.sleep(random.uniform(0.03, 0.12))
        print(yellow(" ] 100%"))
        time.sleep(0.3)
        print()
        slow_print(bold(green(f"  ✓ Access granted. '{name}' is now unlocked.")), 0.02)
        print()
        self.locked.discard(name)

    def cmd_exit(self, _):
        print()
        slow_print(yellow("  Closing secure tunnel..."), 0.03)
        time.sleep(0.4)
        slow_print(yellow("  Wiping session logs..."), 0.03)
        time.sleep(0.4)
        slow_print(green("  Stay ghost. Goodbye."), 0.03)
        print()
        sys.exit(0)

    def run(self):
        while True:
            try: 
                raw = input(self.prompt()).strip()
            except (EOFError, KeyboardInterrupt): 
                print()
                self.cmd_exit([])
                break
            if not raw: 
                continue
            parts = raw.split()
            cmd, args = parts[0].lower(), parts[1:]
            dispatch = {
                "help": self.cmd_help, "clear": self.cmd_clear, "whoami": self.cmd_whoami,
                "ls": self.cmd_ls, "cd": self.cmd_cd, "cat": self.cmd_cat,
                "scan": self.cmd_scan, "connect": self.cmd_connect, "disconnect": self.cmd_disconnect,
                "hack": self.cmd_hack, "exit": self.cmd_exit, "quit": self.cmd_exit
            }
            if cmd in dispatch: 
                dispatch[cmd](args)
            else: 
                print(red(f"  Command not found: '{cmd}'") + "  (type " + cyan("help") + " for commands)")