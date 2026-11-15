import argparse
import importlib.util
import os
import shutil
import site
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

KDPH_URL = "https://raw.githubusercontent.com/Knexyce/kdph/main/kdph.py"
OPENKP_URL = "https://raw.githubusercontent.com/Knexyce/openkp/main/openkp.py"
DECRYPT_KEY = "HallwayNetworkSolarLogitGrid"

def download(url, destination):
    request = urllib.request.Request(url, headers={"User-Agent": "Strikethrough"})
    with urllib.request.urlopen(request, timeout=60) as response:
        Path(destination).write_bytes(response.read())

def run(command):
    try:
        return subprocess.run(command, check=False).returncode
    except KeyboardInterrupt:
        return 130
    except OSError as e:
        print(f"Error at '{e}'.")
        return 1

def site_packages():
    return Path(site.getusersitepackages()).expanduser().resolve()

def find_skywatch():
    spec = importlib.util.find_spec("skywatch")
    if spec is None:
        return None
    if spec.submodule_search_locations:
        return Path(next(iter(spec.submodule_search_locations))).resolve()
    if spec.origin:
        return Path(spec.origin).resolve().parent
    return None

def remove_skywatch():
    location = find_skywatch()
    if location is None:
        return True
    print(f"Removing existing installation at '{location}'.")
    try:
        shutil.rmtree(location)
        return True
    except OSError as e:
        print(f"Error removing Skywatch at '{e}'.")
        return False

def install(path=None):
    destination = Path(path).expanduser().resolve() if path else site_packages()
    try:
        destination.mkdir(parents=True, exist_ok=True)
        if not os.access(destination, os.W_OK):
            print(f"Error: Installation directory is not writable: {destination}")
            return 1
    except OSError as e:
        print(f"Installation error due to '{e}'.")
        return 1
    print(f"Installing Skywatch to '{destination}'...")
    if not remove_skywatch():
        return 1
    try:
        with tempfile.TemporaryDirectory(prefix="strikethrough-") as temp:
            script = Path(temp) / "kdph.py"
            download(KDPH_URL, script)
            result = run([
                sys.executable, str(script), "getpkg",
                "-a", "k-auto", "-p", "skywatch", "-l", str(destination),
                "-k", DECRYPT_KEY
            ])
            if result:
                print("Skywatch installation failed.")
                return result
        print("Skywatch installed successfully.")
        return 0
    except Exception as e:
        print(f"Installation error due to '{e}'.")
        return 1

def decrypt_only(path):
    destination = Path(path).expanduser().resolve()
    destination.mkdir(parents=True, exist_ok=True)
    try:
        with tempfile.TemporaryDirectory(prefix="strikethrough-") as temp:
            script = Path(temp) / "openkp.py"
            download(OPENKP_URL, script)
            result = run([
                sys.executable, str(script), "-a", "k-auto",
                "-p", "skywatch", "-l", str(destination),
                "-k", DECRYPT_KEY
            ])
            if result:
                print("Skywatch decryption failed.")
                return result
        print(f"Skywatch source extracted to '{destination}'.")
        return 0
    except Exception as e:
        print(f"Decryption error at '{e}'.")
        return 1

def skywatch(*args):
    return run([sys.executable, "-m", "skywatch", *args])

def is_alive():
    try:
        from skywatch.console.for_admin import api
        lock = api.LOCK_PATH
        if not lock.exists():
            print("Skywatch is not running.")
            return 1
        try:
            pid = int(lock.read_text(encoding="utf-8").strip())
        except (ValueError, OSError):
            print("Error: Invalid active lock file.")
            return 1
        if api.process_exists(pid):
            print(f"Skywatch is running at process '{pid}'.")
            return 0
        print("Skywatch is not running.")
        return 1
    except ImportError:
        print("Skywatch is not installed.")
        return 1
    except Exception as e:
        print(f"Error checking Skywatch status at '{e}'.")
        return 1

def main():
    parser = argparse.ArgumentParser(
        prog="scli",
        description="Strikethrough CLI; Skywatch's command-line interface."
    )
    commands = parser.add_subparsers(dest="command", required=True)
    p = commands.add_parser("install", help="Install or reinstall Skywatch.")
    p.add_argument("path", nargs="?", help="Optional installation directory.")
    p = commands.add_parser("decrypt_only", help="Decrypt Skywatch without executing build code.")
    p.add_argument("path", help="Destination directory.")
    commands.add_parser("launch", help="Launch Skywatch.")
    p = commands.add_parser("configure", help="Configure Skywatch.")
    p.add_argument("value", help="Configuration in 'key=value' format.")
    p = commands.add_parser("send", help="Send an administrative message.")
    p.add_argument("message", help="Message to send.")
    commands.add_parser("quit", help="Request Skywatch to quit.")
    commands.add_parser("terminate", help="Directly terminate Skywatch.")
    p = commands.add_parser("erase_session", help="Delete a chat session.")
    p.add_argument("session_name")
    p = commands.add_parser("logs", help="View an execution log.")
    p.add_argument("identifier", help="Log number or 'current'.")
    commands.add_parser("print_config", help="Print Skywatch configuration.")
    commands.add_parser("is_alive", help="Check whether Skywatch is running.")
    args = parser.parse_args()
    if args.command == "install":
        return install(args.path)
    if args.command == "decrypt_only":
        return decrypt_only(args.path)
    if args.command == "launch":
        if find_skywatch() is None:
            install()
        return skywatch("-l")
    if args.command == "configure":
        return skywatch("-c", args.value)
    if args.command == "send":
        return skywatch("-s", args.message)
    if args.command == "quit":
        return skywatch("-q")
    if args.command == "terminate":
        return skywatch("-t")
    if args.command == "erase_session":
        return skywatch("-d", args.session_name)
    if args.command == "logs":
        if args.identifier == "current":
            return skywatch("-v", "-e")
        if args.identifier.isdigit():
            return skywatch("-v", "-n", args.identifier)
        parser.error("Log identifier must be a number or 'current'.")
    if args.command == "print_config":
        return skywatch("-v", "-m")
    if args.command == "is_alive":
        return is_alive()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
