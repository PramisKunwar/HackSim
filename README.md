# HackSim v1.0

> A terminal-based hacking simulation game written in Python.  
> **Everything is fake. No real networking, sockets, or OS access is used.**

---

```
  ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██╗███╗   ███╗
  ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██║████╗ ████║
  ███████║███████║██║     █████╔╝ ███████╗██║██╔████╔██║
  ██╔══██║██╔══██║██║     ██╔═██╗ ╚════██║██║██║╚██╔╝██║
  ██║  ██║██║  ██║╚██████╗██║  ██╗███████║██║██║ ╚═╝ ██║
  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝     ╚═╝
```

---

## What is HackSim?

HackSim is a beginner-friendly, single-file Python game that puts you inside a simulated hacker's terminal. You connect to fictional servers, explore fake file systems, and piece together a story of corporate fraud — all without touching real networks or system resources.

Inspired by games like **Hacknet** and classic hacker movies, HackSim is designed to be immersive, readable, and safe to run anywhere.

---

## Requirements

- Python 3.7 or higher
- No external libraries — uses only the Python standard library (`time`, `sys`, `os`, `random`)
- Works on **Linux**, **macOS**, and **Windows** (any terminal that supports ANSI colour codes)

---

## Getting Started

```bash
# Clone or download the repo, then run:
python hacksim.py
```

On startup you'll see an animated boot screen, followed by a prompt to enter your hacker alias. After that you're dropped straight into the terminal.

```
Enter your hacker alias: neo

  Welcome, neo.  Type help to see available commands.

neo@home:/$ 
```

---

## Commands

| Command | Description |
|---|---|
| `help` | Show the command reference |
| `clear` | Clear the screen |
| `whoami` | Display your hacker alias |
| `scan` | List all known servers and their lock status |
| `connect <server>` | Connect to an unlocked server |
| `disconnect` | Return to your home server |
| `hack <server>` | Run a fake exploit sequence to unlock a locked server |
| `ls` | List files and folders in the current directory |
| `cd <dir>` | Change into a directory (`cd ..` to go up) |
| `cat <file>` | Read the contents of a file |
| `exit` / `quit` | Quit the game |

---

## Servers

The game has **5 servers** to explore, each with its own file system and lore. Only `home` is accessible at the start — the rest must be hacked first.

```
home          
corp-server  
bank-server   
email-server  
shadow-server 
```

**Suggested playthrough order:**
1. Read `notes.txt` on `home`
2. `hack corp-server` → read `employees.txt`, `passwords.txt`, and `internal/memo.txt`
3. `hack bank-server` → read `accounts.txt`, `secret.txt`, and `vault/transfer_log.txt`
4. `hack email-server` → read everything in `inbox/` and `sent/`
5. `hack shadow-server` → see who's been watching you

---

## Project Structure

The entire game lives in a single file: `hacksim.py`.

Internally it is organised into three classes and a set of helper utilities:

**`FileSystem`** — Wraps a Python dictionary tree. Handles `ls`, `cd`, and `cat` operations, tracking the current working directory as a list of path segments.

**`Server`** — A thin container that holds a server's name and its `FileSystem` instance. Provides a `reset_path()` method used when switching servers.

**`Game`** — The main controller. Owns all `Server` instances, tracks which servers are locked, manages the current connection, runs the boot/login sequence, and dispatches every command the player types.

All filesystem content is stored as nested Python dictionaries at the top of the file in `FILESYSTEMS`, making it straightforward to add new servers or files without touching any game logic.

---


## Safety Notice

HackSim uses **zero real hacking techniques**. It does not:

- Open network sockets or make HTTP requests
- Access, read, or modify any files on your actual system
- Execute shell commands or subprocesses
- Contain malware, exploits, or any harmful code

All servers, files, credentials, company names, and dollar amounts are entirely fictional.

---

## License

This project is made for hack club.

---
