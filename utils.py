
#!/usr/bin/env python3
"""
ShadowTrace - Digital Footprint & Suspicious Pattern Finder
Utility Functions - Helper functions for UI, formatting, and user input
Author: Your Name
Version: 1.0
"""

import os
import sys
import time
from typing import Optional, List


class Colors:
    """ANSI color codes for terminal output"""
    
    # Basic colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Text formatting
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    STRIKETHROUGH = '\033[9m'
    
    # Reset
    RESET = '\033[0m'
    
    def disable_colors(self):
        """Disable all colors (useful for file output)"""
        for attr in dir(self):
            if not attr.startswith('_') and attr != 'disable_colors':
                setattr(self, attr, '')

    def warning_box(self, message: str) -> str:
        """Create a warning box around message"""
        lines = message.split('\n')
        max_length = max(len(line) for line in lines) if lines else 0

        box = f"{self.YELLOW}┌{'─' * (max_length + 2)}┐{self.RESET}\n"

        for line in lines:
            padding = max_length - len(line)
            box += f"{self.YELLOW}│ {self.RED}{line}{' ' * padding} {self.YELLOW}│{self.RESET}\n"

        box += f"{self.YELLOW}└{'─' * (max_length + 2)}┘{self.RESET}"
        return box

    def success_box(self, message: str) -> str:
        """Create a success box around message"""
        lines = message.split('\n')
        max_length = max(len(line) for line in lines) if lines else 0

        box = f"{self.GREEN}┌{'─' * (max_length + 2)}┐{self.RESET}\n"

        for line in lines:
            padding = max_length - len(line)
            box += f"{self.GREEN}│ {self.WHITE}{line}{' ' * padding} {self.GREEN}│{self.RESET}\n"

        box += f"{self.GREEN}└{'─' * (max_length + 2)}┘{self.RESET}"
        return box

    def info_box(self, message: str) -> str:
        """Create an info box around message"""
        lines = message.split('\n')
        max_length = max(len(line) for line in lines) if lines else 0

        box = f"{self.BLUE}┌{'─' * (max_length + 2)}┐{self.RESET}\n"

        for line in lines:
            padding = max_length - len(line)
            box += f"{self.BLUE}│ {self.WHITE}{line}{' ' * padding} {self.BLUE}│{self.RESET}\n"

        box += f"{self.BLUE}└{'─' * (max_length + 2)}┘{self.RESET}"
        return box


def clear_screen():
    """Clear the terminal screen - works on Windows, Mac, and Linux"""
    try:
        # Windows
        if os.name == 'nt':
            os.system('cls')
        # Mac and Linux
        else:
            os.system('clear')
    except:
        # If clearing fails, print empty lines
        print('\n' * 50)


def print_banner():
    """Print the cool ShadowTrace banner with ASCII art"""
    colors = Colors()
    
    banner = f"""
{colors.CYAN}
    ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗████████╗██████╗  █████╗  ██████╗███████╗
    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
    ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║   ██║   ██████╔╝███████║██║     █████╗  
    ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║   ██║   ██╔══██╗██╔══██║██║     ██╔══╝  
    ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝   ██║   ██║  ██║██║  ██║╚██████╗███████╗
    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝
{colors.RESET}
{colors.YELLOW}                        🔍 Digital Footprint & Suspicious Pattern Finder 🔍{colors.RESET}
{colors.GREEN}                                    Version 1.0 - Stay Safe Online{colors.RESET}
"""
    print(banner)


def print_loading_animation(message: str = "Loading", duration: float = 2.0):
    """Print a loading animation"""
    colors = Colors()
    chars = "⣾⣽⣻⢿⡿⣟⣯⣷"
    
    print(f"{colors.CYAN}{message} ", end="", flush=True)
    
    start_time = time.time()
    i = 0
    
    while time.time() - start_time < duration:
        print(f"\b{chars[i % len(chars)]}", end="", flush=True)
        time.sleep(0.1)
        i += 1
    
    print(f"\b✅ {colors.GREEN}Done!{colors.RESET}")


def get_user_input(prompt: str, required: bool = False) -> str:
    """Get user input with validation"""
    while True:
        try:
            user_input = input(prompt).strip()
            if user_input or not required:
                return user_input
            print("⚠️ This field is required. Please enter a valid value.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            sys.exit(0)
        except EOFError:
            print("\n\nEnd of input detected.")
            return ""


def get_choice(prompt: str, choices: List[str], case_sensitive: bool = False) -> str:
    """Get a valid choice from user"""
    colors = Colors()
    
    while True:
        print(f"\n{colors.CYAN}{prompt}{colors.RESET}")
        for i, choice in enumerate(choices, 1):
            print(f"{colors.YELLOW}{i}.{colors.RESET} {choice}")
        
        user_input = get_user_input(f"\nEnter your choice (1-{len(choices)}): ")
        
        try:
            choice_num = int(user_input)
            if 1 <= choice_num <= len(choices):
                return choices[choice_num - 1]
            else:
                print(f"{colors.RED}Invalid choice! Please enter a number between 1 and {len(choices)}.{colors.RESET}")
        except ValueError:
            # Try to match the choice by name
            for choice in choices:
                if (case_sensitive and user_input == choice) or \
                   (not case_sensitive and user_input.lower() == choice.lower()):
                    return choice
            
            print(f"{colors.RED}Invalid choice! Please enter a valid option.{colors.RESET}")


def confirm_action(message: str, default: bool = False) -> bool:
    """Ask user for confirmation"""
    colors = Colors()
    default_text = " [Y/n]" if default else " [y/N]"
    
    response = get_user_input(f"{colors.YELLOW}{message}{default_text}: {colors.RESET}")
    
    if not response:
        return default
    
    return response.lower() in ['y', 'yes', '1', 'true']


def format_file_size(size_bytes: int) -> str:
    """Format file size in human readable format"""
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f} {size_names[i]}"


def format_time_elapsed(start_time: float) -> str:
    """Format elapsed time in human readable format"""
    elapsed = time.time() - start_time
    
    if elapsed < 60:
        return f"{elapsed:.1f} seconds"
    elif elapsed < 3600:
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        return f"{minutes}m {seconds}s"
    else:
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        return f"{hours}h {minutes}m"


def create_progress_bar(current: int, total: int, width: int = 50) -> str:
    """Create a text-based progress bar"""
    colors = Colors()
    
    if total == 0:
        percentage = 100
    else:
        percentage = (current / total) * 100
    
    filled_width = int(width * current // total) if total > 0 else width
    bar = '█' * filled_width + '░' * (width - filled_width)
    
    return f"{colors.GREEN}[{bar}] {percentage:.1f}% ({current}/{total}){colors.RESET}"


def sanitize_filename(filename: str) -> str:
    """Sanitize filename to be safe for filesystem"""
    # Remove or replace unsafe characters
    unsafe_chars = '<>:"/\\|?*'
    for char in unsafe_chars:
        filename = filename.replace(char, '_')
    
    # Remove leading/trailing dots and spaces
    filename = filename.strip('. ')
    
    # Ensure filename is not empty
    if not filename:
        filename = "untitled"
    
    return filename


def print_table(headers: List[str], rows: List[List[str]], title: Optional[str] = None):
    """Print a formatted table"""
    colors = Colors()
    
    if not rows:
        print(f"{colors.YELLOW}No data to display.{colors.RESET}")
        return
    
    # Calculate column widths
    col_widths = [len(header) for header in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Print title if provided
    if title:
        total_width = sum(col_widths) + len(headers) * 3 - 1
        print(f"\n{colors.BOLD}{colors.CYAN}{title.center(total_width)}{colors.RESET}")
    
    # Print separator
    separator = "+" + "+".join("-" * (width + 2) for width in col_widths) + "+"
    print(f"\n{colors.BLUE}{separator}{colors.RESET}")
    
    # Print headers
    header_row = "|"
    for i, header in enumerate(headers):
        header_row += f" {colors.BOLD}{header.ljust(col_widths[i])}{colors.RESET} |"
    print(header_row)
    
    print(f"{colors.BLUE}{separator}{colors.RESET}")
    
    # Print rows
    for row in rows:
        data_row = "|"
        for i, cell in enumerate(row):
            if i < len(col_widths):
                data_row += f" {str(cell).ljust(col_widths[i])} |"
        print(data_row)
    
    print(f"{colors.BLUE}{separator}{colors.RESET}")


def show_help():
    """Show help information"""
    colors = Colors()
    
    help_text = f"""
{colors.BOLD}{colors.CYAN}ShadowTrace - Help & Usage Guide{colors.RESET}

{colors.YELLOW}What is ShadowTrace?{colors.RESET}
ShadowTrace is a digital footprint analyzer that scans text data for suspicious patterns
including personal information, financial data, system information, and potential security threats.

{colors.YELLOW}Supported Pattern Types:{colors.RESET}
• Email addresses
• Phone numbers  
• Credit card numbers
• Social Security Numbers (SSN)
• URLs and websites
• IP addresses
• Bitcoin addresses
• File paths
• MAC addresses
• API keys
• AWS access keys
• Password patterns

{colors.YELLOW}Risk Assessment:{colors.RESET}
The tool provides a risk score from 0-100% based on:
• Number and types of suspicious patterns found
• Content sentiment analysis
• Presence of security-related keywords

{colors.YELLOW}Input Methods:{colors.RESET}
1. Manual text input (type or paste text)
2. File upload (supports .txt files)

{colors.YELLOW}Output Options:{colors.RESET}
• Real-time analysis display
• Detailed pattern breakdown
• Risk assessment with recommendations
• Save analysis reports to file

{colors.YELLOW}Safety Notice:{colors.RESET}
This tool is for educational and security analysis purposes only.
Never input real sensitive data like actual passwords or financial information.

{colors.GREEN}Stay safe online! 🛡️{colors.RESET}
"""
    
    print(help_text)


# Test utility functions
def test_utils():
    """Test utility functions"""
    colors = Colors()
    
    print("Testing ShadowTrace Utilities...")
    print("=" * 40)
    
    # Test banner
    print_banner()
    
    # Test color boxes
    print(colors.success_box("This is a success message!"))
    print(colors.warning_box("This is a warning message!"))
    print(colors.info_box("This is an info message!"))
    
    # Test progress bar
    print("\nProgress bar test:")
    for i in range(0, 101, 10):
        print(f"\r{create_progress_bar(i, 100)}", end="", flush=True)
        time.sleep(0.1)
    print()
    
    # Test table
    headers = ["Pattern Type", "Count", "Risk Level"]
    rows = [
        ["Emails", "3", "Low"],
        ["Phone Numbers", "2", "Medium"],
        ["Credit Cards", "1", "High"]
    ]
    print_table(headers, rows, "Pattern Analysis Results")
    
    print(f"\n{colors.GREEN}All utility tests completed!{colors.RESET}")


# Run tests if this file is executed directly
if __name__ == "__main__":
    test_utils()
