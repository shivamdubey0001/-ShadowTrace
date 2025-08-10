#!/usr/bin/env python3
"""
ShadowTrace - Digital Footprint & Suspicious Pattern Finder
Main CLI Controller File
Author: Your Name
Version: 1.0
"""

import os
import sys
from datetime import datetime

# Import our custom modules
try:
    from analyzer import SuspiciousPatternAnalyzer
    from utils import Colors, clear_screen, print_banner, get_user_input
except ImportError as e:
    print(f"Error: Missing required modules. Make sure all files are in the same directory.")
    print(f"Details: {e}")
    sys.exit(1)


class ShadowTrace:
    """Main class that controls the entire ShadowTrace application"""

    def __init__(self):
        # Initialize the pattern analyzer
        self.analyzer = SuspiciousPatternAnalyzer()
        self.colors = Colors()

    def display_welcome(self):
        """Show the welcome message and application info"""
        clear_screen()
        print_banner()
        print(f"{self.colors.CYAN}🔍 Welcome to ShadowTrace – Digital Footprint & Suspicious Pattern Finder{self.colors.RESET}")
        print(f"{self.colors.YELLOW}{'='*70}{self.colors.RESET}")
        print(f"{self.colors.GREEN}This tool helps you find suspicious patterns in text data:{self.colors.RESET}")
        print(f"  • Email addresses, phone numbers, credit cards")
        print(f"  • URLs and IP addresses")
        print(f"  • Word frequency analysis")
        print(f"  • Sentiment analysis")
        print(f"  • Risk assessment")
        print(f"{self.colors.YELLOW}{'='*70}{self.colors.RESET}\n")

    def get_input_data(self):
        """Get text input from user - either manual input or file upload"""
        while True:
            print(f"{self.colors.CYAN}Choose input method:{self.colors.RESET}")
            print("1. Type/Paste text manually")
            print("2. Load from text file")
            print("3. Exit")

            choice = get_user_input(f"{self.colors.YELLOW}Enter your choice (1-3): {self.colors.RESET}")

            if choice == "1":
                return self.get_manual_input()
            elif choice == "2":
                return self.get_file_input()
            elif choice == "3":
                print(f"{self.colors.GREEN}Thanks for using ShadowTrace! Stay safe! 👋{self.colors.RESET}")
                sys.exit(0)
            else:
                print(f"{self.colors.RED}Invalid choice! Please enter 1, 2, or 3.{self.colors.RESET}\n")

    def get_manual_input(self):
        """Get text input manually from user"""
        print(f"\n{self.colors.CYAN}Enter your text data (Press Enter twice when done):{self.colors.RESET}")
        print(f"{self.colors.YELLOW}> {self.colors.RESET}", end="")

        lines = []
        empty_line_count = 0

        try:
            while True:
                line = input()
                if line.strip() == "":
                    empty_line_count += 1
                    if empty_line_count >= 2:  # Two empty lines means user is done
                        break
                else:
                    empty_line_count = 0
                lines.append(line)
                print(f"{self.colors.YELLOW}> {self.colors.RESET}", end="")

        except KeyboardInterrupt:
            print(f"\n{self.colors.RED}Input cancelled by user.{self.colors.RESET}")
            return None

        text_data = "\n".join(lines).strip()

        if not text_data:
            print(f"{self.colors.RED}No text entered! Please try again.{self.colors.RESET}")
            return None

        return text_data

    def get_file_input(self):
        """Load text data from a file"""
        filename = get_user_input(f"{self.colors.CYAN}Enter filename (with path if needed): {self.colors.RESET}")

        try:
            # Check if file exists
            if not os.path.exists(filename):
                print(f"{self.colors.RED}Error: File '{filename}' not found!{self.colors.RESET}")
                return None

            # Try to read the file
            with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read().strip()

            if not content:
                print(f"{self.colors.RED}Error: File is empty!{self.colors.RESET}")
                return None

            print(f"{self.colors.GREEN}✅ File loaded successfully! ({len(content)} characters){self.colors.RESET}")
            return content

        except PermissionError:
            print(f"{self.colors.RED}Error: Permission denied! Cannot read file '{filename}'.{self.colors.RESET}")
            return None
        except Exception as e:
            print(f"{self.colors.RED}Error reading file: {str(e)}{self.colors.RESET}")
            return None

    def display_results(self, analysis_result):
        """Display the analysis results in a formatted way"""
        print(f"\n{self.colors.YELLOW}[Analyzing data... 🔎]{self.colors.RESET}")
        print(f"{self.colors.BLUE}{'='*50}{self.colors.RESET}")

        # Display found patterns
        patterns = analysis_result['patterns']
        if any(patterns.values()):  # If any patterns found
            print(f"{self.colors.CYAN}📌 Suspicious Patterns Found:{self.colors.RESET}")

            for pattern_type, items in patterns.items():
                if items:  # If this pattern type has results
                    print(f"  {self.colors.RED}• {pattern_type.title()}:{self.colors.RESET}")
                    for item in items[:5]:  # Show max 5 items per type
                        print(f"    - {item}")
                    if len(items) > 5:
                        print(f"    ... and {len(items) - 5} more")
        else:
            print(f"{self.colors.GREEN}📌 No suspicious patterns detected! ✅{self.colors.RESET}")

        # Display word frequency
        frequency = analysis_result['frequency']
        if frequency:
            print(f"\n{self.colors.CYAN}📊 Top Word Frequency:{self.colors.RESET}")
            for word, count in frequency[:8]:  # Show top 8 words
                print(f"  - {word}: {count}")

        # Display sentiment
        sentiment = analysis_result['sentiment']
        sentiment_color = self.colors.GREEN if sentiment == 'Positive' else self.colors.RED if sentiment == 'Negative' else self.colors.YELLOW
        print(f"\n{sentiment_color}😊 Sentiment: {sentiment}{self.colors.RESET}")

        # Display risk score
        risk_score = analysis_result['risk_score']
        if risk_score >= 80:
            risk_color = self.colors.RED
            risk_level = "Very High Risk"
            risk_emoji = "🚨"
        elif risk_score >= 60:
            risk_color = self.colors.YELLOW
            risk_level = "High Risk"
            risk_emoji = "⚠️"
        elif risk_score >= 40:
            risk_color = self.colors.BLUE
            risk_level = "Medium Risk"
            risk_emoji = "⚡"
        else:
            risk_color = self.colors.GREEN
            risk_level = "Low Risk"
            risk_emoji = "✅"

        print(f"\n{risk_color}{risk_emoji} Risk Score: {risk_score}% ({risk_level}){self.colors.RESET}")
        print(f"{self.colors.BLUE}{'='*50}{self.colors.RESET}")

    def save_report(self, text_data, analysis_result):
        """Save the analysis report to a file"""
        choice = get_user_input(f"\n{self.colors.CYAN}Save this report as a file? (y/n): {self.colors.RESET}").lower()

        if choice not in ['y', 'yes']:
            return

        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"shadow_report_{timestamp}.txt"

        try:
            with open(filename, 'w', encoding='utf-8') as file:
                # Write header
                file.write("=" * 60 + "\n")
                file.write("ShadowTrace - Digital Footprint Analysis Report\n")
                file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("=" * 60 + "\n\n")

                # Write original text (first 500 chars)
                file.write("ANALYZED TEXT:\n")
                file.write("-" * 20 + "\n")
                if len(text_data) > 500:
                    file.write(text_data[:500] + "...(truncated)\n\n")
                else:
                    file.write(text_data + "\n\n")

                # Write patterns
                file.write("SUSPICIOUS PATTERNS FOUND:\n")
                file.write("-" * 30 + "\n")
                patterns = analysis_result['patterns']
                found_any = False
                for pattern_type, items in patterns.items():
                    if items:
                        file.write(f"{pattern_type.title()}:\n")
                        for item in items:
                            file.write(f"  - {item}\n")
                        file.write("\n")
                        found_any = True

                if not found_any:
                    file.write("No suspicious patterns detected.\n\n")

                # Write frequency analysis
                file.write("WORD FREQUENCY ANALYSIS:\n")
                file.write("-" * 25 + "\n")
                for word, count in analysis_result['frequency'][:15]:
                    file.write(f"{word}: {count}\n")

                # Write sentiment and risk
                file.write(f"\nSENTIMENT: {analysis_result['sentiment']}\n")
                file.write(f"RISK SCORE: {analysis_result['risk_score']}%\n")

                file.write("\n" + "=" * 60 + "\n")
                file.write("Report generated by ShadowTrace v1.0\n")

            print(f"{self.colors.GREEN}✅ Report saved as '{filename}'{self.colors.RESET}")

        except Exception as e:
            print(f"{self.colors.RED}Error saving report: {str(e)}{self.colors.RESET}")

    def run(self):
        """Main application loop"""
        self.display_welcome()

        while True:
            try:
                # Get input data
                text_data = self.get_input_data()

                if text_data is None:
                    continue  # Go back to input selection

                # Analyze the data
                print(f"{self.colors.YELLOW}Processing your data...{self.colors.RESET}")
                analysis_result = self.analyzer.analyze(text_data)

                # Display results
                self.display_results(analysis_result)

                # Save report option
                self.save_report(text_data, analysis_result)

                # Ask if user wants to analyze more data
                print(f"\n{self.colors.CYAN}Would you like to analyze more data?{self.colors.RESET}")
                continue_choice = get_user_input("Enter 'y' to continue or any other key to exit: ").lower()

                if continue_choice not in ['y', 'yes']:
                    print(f"{self.colors.GREEN}Thanks for using ShadowTrace! Stay safe! 🛡️{self.colors.RESET}")
                    break

                # Clear screen for next analysis
                clear_screen()
                print_banner()

            except KeyboardInterrupt:
                print(f"\n{self.colors.YELLOW}Program interrupted by user. Exiting...{self.colors.RESET}")
                sys.exit(0)
            except Exception as e:
                print(f"{self.colors.RED}An unexpected error occurred: {str(e)}{self.colors.RESET}")
                print(f"{self.colors.YELLOW}Please try again or contact support.{self.colors.RESET}")


def main():
    """Entry point of the application"""
    try:
        # Create and run the ShadowTrace application
        app = ShadowTrace()
        app.run()
    except Exception as e:
        print(f"Critical error: {str(e)}")
        sys.exit(1)


# This ensures the script runs only when executed directly
if __name__ == "__main__":
    main()