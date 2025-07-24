import os
import math
import argparse
import sys
import shutil
try:
    from pyfiglet import Figlet
except ImportError:
    Figlet = None


def print_banner():
    """Print a dynamic banner that fits the terminal width."""
    terminal_width = shutil.get_terminal_size((100, 20)).columns
    banner_text = "DK3Y Combo Splitter"
    
    # ANSI color codes
    GREEN = "\033[92m"  # Bright green (hacker green)
    RESET = "\033[0m"   # Reset to default color
    
    if Figlet:
        f = Figlet(font='big', width=terminal_width)
        banner = f.renderText(banner_text)
        print(f"{GREEN}{banner}{RESET}")
    else:
        # Fallback if pyfiglet is not available
        separator = "=" * min(len(banner_text) + 4, terminal_width)
        centered_text = f"  {banner_text}  ".center(terminal_width)
        print(f"{GREEN}{separator}")
        print(f"{centered_text}")
        print(f"{separator}{RESET}")


def split_file(input_file, num_parts=None, lines_per_file=None, output_dir=None):
    """
    Efficiently splits a text file into multiple parts by number of files or lines per file, suitable for very large files.
    """
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        return

    if os.path.getsize(input_file) == 0:
        print(f"Error: File '{input_file}' is empty.")
        return

    if (num_parts is None and lines_per_file is None) or (num_parts and lines_per_file):
        print("Error: Provide either number of files or lines per file, not both.")
        return

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    else:
        output_dir = os.path.dirname(input_file) or '.'

    base_name, ext = os.path.splitext(os.path.basename(input_file))

    # Overwrite protection
    def output_exists(idx):
        return os.path.exists(os.path.join(output_dir, f"{base_name}_part{idx}{ext}"))

    # First pass: count lines if needed
    total_lines = None
    if num_parts and not lines_per_file:
        with open(input_file, 'r', encoding='utf-8') as f:
            total_lines = sum(1 for _ in f)
        if total_lines < num_parts:
            print(f"Error: File has only {total_lines} lines, which is less than the number of parts ({num_parts}).")
            return
        lines_per_file = math.ceil(total_lines / num_parts)
    elif lines_per_file:
        with open(input_file, 'r', encoding='utf-8') as f:
            total_lines = sum(1 for _ in f)
        if lines_per_file > total_lines:
            print(f"Warning: Number of lines per file is greater than total lines. Only one file will be created.")

    # Overwrite warning
    part_count = num_parts if num_parts else math.ceil(total_lines / lines_per_file) if total_lines and lines_per_file else 1
    overwrite = False
    for idx in range(1, part_count + 1):
        if output_exists(idx):
            resp = input(f"Output file {base_name}_part{idx}{ext} already exists. Overwrite all? (y/n): ").strip().lower()
            if resp == 'y':
                overwrite = True
                break
            else:
                print("Aborting to avoid overwriting files.")
                return

    # Second pass: split in a single read
    part_idx = 1
    line_count = 0
    output_file = os.path.join(output_dir, f"{base_name}_part{part_idx}{ext}")
    f_out = None
    written = 0
    processed = 0
    try:
        f_out = open(output_file, 'w', encoding='utf-8', buffering=1024*1024)
        with open(input_file, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                f_out.write(line)
                written += 1
                line_count += 1
                processed += 1
                if lines_per_file and written >= lines_per_file:
                    f_out.close()
                    print(f"Created: {output_file} ({written} lines)")
                    part_idx += 1
                    output_file = os.path.join(output_dir, f"{base_name}_part{part_idx}{ext}")
                    f_out = open(output_file, 'w', encoding='utf-8', buffering=1024*1024)
                    written = 0
                if i % 1_000_000 == 0:
                    print(f"Processed {i} lines...", file=sys.stderr)
            if written > 0:
                f_out.close()
                print(f"Created: {output_file} ({written} lines)")
            else:
                f_out.close()
                os.remove(output_file)  # Remove empty file if last part is empty
        print(f"\nSummary: {processed} lines processed, {part_idx} file(s) created.")
    except Exception as e:
        print(f"An error occurred: {e}")
        if f_out and not f_out.closed:
            f_out.close()


def main():
    print_banner()
    # Prompt for file name first
    input_file = input('Enter the path to the text file to split: ').strip()
    while not os.path.isfile(input_file):
        print(f"File '{input_file}' not found. Please try again.")
        input_file = input('Enter the path to the text file to split: ').strip()

    # Ask how to split after file is provided
    print('How would you like to split the file?')
    print('1. By number of parts')
    print('2. By lines per file')
    choice = input('Enter 1 or 2: ').strip()
    num_parts = None
    lines_per_file = None
    if choice == '1':
        while True:
            try:
                num_parts = int(input('Enter the number of parts: ').strip())
                if num_parts > 0:
                    break
                else:
                    print('Please enter a positive integer.')
            except ValueError:
                print('Please enter a valid integer.')
    elif choice == '2':
        while True:
            try:
                lines_per_file = int(input('Enter the number of lines per file: ').strip())
                if lines_per_file > 0:
                    break
                else:
                    print('Please enter a positive integer.')
            except ValueError:
                print('Please enter a valid integer.')
    else:
        print('Invalid choice. Exiting.')
        return

    output_dir = input('Enter output directory (leave blank for same as input file): ').strip() or None
    split_file(input_file, num_parts, lines_per_file, output_dir)


if __name__ == "__main__":
    main()
