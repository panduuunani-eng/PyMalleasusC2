import argparse
import platform
import sys

def analyze_device():
    info = platform.uname()
    print(f"Node Name: {info.node}")
    print(f"System: {info.system}")
    print(f"Release: {info.release}")
    print(f"Version: {info.version}")
    print(f"Machine: {info.machine}")
    print(f"Processor: {info.processor}")

def main():
    parser = argparse.ArgumentParser(description='Enhanced Script with Device Analysis')
    parser.add_argument('--device-analysis', action='store_true', help='Show device analysis information.')
    args = parser.parse_args()
    
    if args.device_analysis:
        analyze_device()
    else:
        print('No device analysis requested.')

if __name__ == '__main__':
    main()