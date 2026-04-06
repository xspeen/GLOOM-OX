#!/usr/bin/env python3
"""
GLOOM-OX v4.0 - ENTERPRISE GRADE UNIVERSAL MEDIA EXTRACTOR
Author: xspeen | Certified Ethical Pentester (CEH)
Launch: 2026
"""

import os
import sys
import time
import signal
import argparse
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from gloom_ox.core.download_manager import DownloadManagerUnleashed
from gloom_ox.ui.banner import display_banner, display_robot_animation
from gloom_ox.ui.robot_assistant import RobotAssistant
from gloom_ox.utils.dependencies import install_dependencies, check_internet
from gloom_ox.utils.paths import cleanup_temp_files, EXP_LINK_DIR
from gloom_ox.config.settings import VERSION, AUTHOR, REPO_URL


def signal_handler(sig, frame):
    """Handle shutdown signals"""
    print("\n\033[1;31m\n[!] Shutdown signal received. Cleaning up...\033[0m")
    cleanup_temp_files()
    print(f"\033[1;32m[+] Thanks for using GLOOM-OX by {AUTHOR}!\033[0m")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


def handle_arguments():
    """Parse and handle command line arguments"""
    parser = argparse.ArgumentParser(
        prog="GLOOM-OX",
        description="Enterprise Grade Universal Media Extractor - NO LIMITS",
        epilog=f"Author: {AUTHOR} | CEH Certified | 2026"
    )
    
    parser.add_argument("url", nargs="?", help="URL to download")
    parser.add_argument("-u", "--update", action="store_true", help="Force update all dependencies")
    parser.add_argument("-d", "--dir", action="store_true", help="Show download directory")
    parser.add_argument("-v", "--version", action="version", version=f"GLOOM-OX v{VERSION}")
    parser.add_argument("-o", "--output", help="Custom output directory")
    parser.add_argument("-q", "--quiet", action="store_true", help="Quiet mode (no banner)")
    parser.add_argument("--no-new-term", action="store_true", help="Don't launch new terminal")
    
    return parser.parse_args()


def main_interface():
    """Main interactive user interface"""
    args = handle_arguments()
    
    # Quiet mode check
    if not args.quiet:
        display_banner()
        display_robot_animation()
    
    # Initialize robot assistant
    robot = RobotAssistant()
    robot.speak("GLOOM-OX activated. Enterprise mode engaged.")
    
    # Check internet
    if not check_internet():
        print("\033[1;31m[!] NO INTERNET CONNECTION - Check your network\033[0m")
        robot.speak("No internet connection detected. Please check your network.")
        time.sleep(2)
        return 1
    
    # Install/update dependencies
    print("\n")
    install_dependencies()
    robot.speak("Dependencies ready. System fully operational.")
    
    # Initialize manager
    manager = DownloadManagerUnleashed()
    
    # Handle command line URL
    if args.url:
        print(f"\033[1;33m[+] Direct download: {args.url}\033[0m")
        robot.speak(f"Processing download request")
        file_path, title = manager.download(args.url)
        
        if file_path:
            print(f"\033[1;32m[✓] Downloaded: {file_path}\033[0m")
            robot.speak(f"Download complete: {title[:50] if title else 'Unknown'}")
            return 0
        else:
            print("\033[1;31m[!] Download failed\033[0m")
            robot.speak("Download failed. Please check the URL.")
            return 1
    
    # Handle other arguments
    if args.update:
        install_dependencies()
        return 0
    
    if args.dir:
        print(f"\033[1;36m[+] Download directory: {EXP_LINK_DIR}\033[0m")
        files = os.listdir(EXP_LINK_DIR) if os.path.exists(EXP_LINK_DIR) else []
        if files:
            for f in sorted(files, key=lambda x: os.path.getmtime(os.path.join(EXP_LINK_DIR, x)), reverse=True)[:10]:
                size = os.path.getsize(os.path.join(EXP_LINK_DIR, f))
                print(f"  {f[:50]:50} | {size//1024}KB")
        return 0
    
    # Interactive mode
    while True:
        print("\n" + "\033[1;35m" + "═"*70 + "\033[0m")
        print("\033[1;33m[+] Enter media URL (commands: clear, dir, history, update, robot, exit):\033[0m")
        print("\033[1;31m[!] NO LIMITS: YouTube, Shorts, Instagram, Pinterest, TikTok, Private, Premium\033[0m")
        print("\033[1;37m" + "─"*70 + "\033[0m")
        
        try:
            user_input = input("\033[1;32m[GLOOM-OX] >> \033[0m").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\033[1;31m[!] Shutting down...\033[0m")
            break
        
        # Handle commands
        if user_input.lower() == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')
            display_banner()
            continue
        elif user_input.lower() == 'dir':
            print(f"\033[1;36m[+] Download directory: {EXP_LINK_DIR}\033[0m")
            files = os.listdir(EXP_LINK_DIR) if os.path.exists(EXP_LINK_DIR) else []
            if files:
                for f in sorted(files, key=lambda x: os.path.getmtime(os.path.join(EXP_LINK_DIR, x)), reverse=True)[:10]:
                    size = os.path.getsize(os.path.join(EXP_LINK_DIR, f))
                    print(f"  {f[:50]:50} | {size//1024}KB")
            else:
                print("  No files yet")
            continue
        elif user_input.lower() == 'history':
            print("\033[1;36m[+] Download History:\033[0m")
            if manager.history:
                for item in manager.history[-5:]:
                    print(f"  {item.get('title', 'Unknown')[:40]:40} | {os.path.basename(item.get('file', 'Unknown'))}")
            else:
                print("  No history yet")
            continue
        elif user_input.lower() == 'update':
            install_dependencies()
            continue
        elif user_input.lower() == 'robot':
            robot.interactive_mode()
            continue
        elif user_input.lower() in ['exit', 'quit', 'q']:
            print("\033[1;31m[!] Closing GLOOM-OX...\033[0m")
            robot.speak("GLOOM-OX shutting down. Goodbye.")
            break
        
        # Download
        if user_input:
            start_time = time.time()
            robot.speak("Processing your request")
            file_path, title = manager.download(user_input)
            
            if file_path:
                elapsed = time.time() - start_time
                
                print("\n" + "\033[1;35m" + "═"*70 + "\033[0m")
                print("\033[1;32m╔══════════════════════════════════════════════════════════╗")
                print("║              DOWNLOAD COMPLETE - ENTERPRISE MODE!         ║")
                print(f"║               GLOOM-OX v{VERSION} 🔓                         ║")
                print("╚══════════════════════════════════════════════════════════╝\033[0m")
                print(f"\033[1;36m[✓] Title: {title[:60] if title else 'Unknown'}\033[0m")
                print(f"\033[1;36m[✓] File: {os.path.basename(file_path)}\033[0m")
                print(f"\033[1;36m[✓] Time: {elapsed:.1f} seconds\033[0m")
                print(f"\033[1;36m[✓] Author: {AUTHOR} | CEH Certified\033[0m")
                
                robot.speak(f"Download complete. Saved to downloads folder.")
            else:
                print("\033[1;31m[!] DOWNLOAD FAILED - Attempting bypass...\033[0m")
                robot.speak("Download failed. Activating bypass protocols.")
                
                # Try with robot assistance
                file_path, title = manager.download_with_bypass(user_input)
                if file_path:
                    print("\033[1;32m[✓] Bypass successful!\033[0m")
                    robot.speak("Bypass successful. Content downloaded.")
                else:
                    print("\033[1;31m[!] All bypass methods exhausted\033[0m")
                    robot.speak("Unable to download. The content may be heavily protected.")
            
            input("\n\033[1;33m[!] Press Enter to continue...\033[0m")
            os.system('cls' if os.name == 'nt' else 'clear')
            display_banner()
    
    cleanup_temp_files()
    return 0


def run():
    """Entry point for the package"""
    return main_interface()


if __name__ == "__main__":
    sys.exit(run())
