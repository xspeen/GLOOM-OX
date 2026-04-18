# gloom_ox.py as a module
import sys
import os

__version__ = "5.2.0"
__author__ = "xspeen"

def main():
    """Main entry point for console script"""
    # Import and run the main script
    script_path = os.path.join(os.path.dirname(__file__), "gloom-ox.py")
    if os.path.exists(script_path):
        with open(script_path, 'r') as f:
            exec(f.read())
    else:
        print("Error: gloom-ox.py not found")
        sys.exit(1)

if __name__ == "__main__":
    main()
