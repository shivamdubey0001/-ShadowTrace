#!/usr/bin/env python3
"""
ShadowTrace - Digital Footprint & Suspicious Pattern Finder
Pattern Library - Regex Patterns for Suspicious Data Detection
Author: Your Name
Version: 1.0
"""

import re
from typing import Dict, List, Tuple, Optional


class PatternLibrary:
    """Library containing all regex patterns for detecting suspicious data"""

    def __init__(self):
        # Email pattern - matches most valid email formats
        self.EMAIL_PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        # Phone number patterns - various formats
        self.PHONE_PATTERN = r'(?:\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})'

        # Credit card pattern - 4 groups of 4 digits
        self.CREDIT_CARD_PATTERN = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'

        # Social Security Number pattern
        self.SSN_PATTERN = r'\b\d{3}-?\d{2}-?\d{4}\b'

        # URL pattern - matches http/https URLs
        self.URL_PATTERN = r'https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*)?(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?'

        # IP Address pattern - IPv4
        self.IP_PATTERN = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

        # Bitcoin address pattern
        self.BITCOIN_PATTERN = r'\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b'

        # File path pattern - Windows and Unix paths
        self.FILE_PATH_PATTERN = r'(?:[A-Za-z]:\\|/)[^\s<>"]*'

        # MAC Address pattern
        self.MAC_PATTERN = r'\b([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})\b'

        # API Key pattern (basic)
        self.API_KEY_PATTERN = r'\b(?:api_key|apikey|api-key)[:=]\s*["\']?([A-Za-z0-9_-]{20,})["\']?\b'

        # AWS Access Key pattern
        self.AWS_KEY_PATTERN = r'\bAKIA[0-9A-Z]{16}\b'

        # Password pattern (basic)
        self.PASSWORD_PATTERN = r'\b(?:password|pwd|pass)[:=]\s*["\']?([^\s"\']{6,})["\']?\b'

    def validate_email(self, email: str) -> bool:
        """Validate if email format is correct"""
        return bool(re.match(self.EMAIL_PATTERN, email))

    def validate_ip(self, ip: str) -> bool:
        """Validate if IP address is in correct format"""
        if not re.match(self.IP_PATTERN, ip):
            return False

        parts = ip.split('.')
        return all(0 <= int(part) <= 255 for part in parts)

    def validate_credit_card(self, cc: str) -> bool:
        """Basic credit card validation using Luhn algorithm"""
        # Remove spaces and hyphens
        cc_clean = re.sub(r'[-\s]', '', cc)

        if not cc_clean.isdigit() or len(cc_clean) < 13 or len(cc_clean) > 19:
            return False

        # Luhn algorithm
        total = 0
        reverse_digits = cc_clean[::-1]

        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:  # Every second digit from right
                n *= 2
                if n > 9:
                    n = n // 10 + n % 10
            total += n

        return total % 10 == 0

    def find_all_patterns(self, text: str) -> Dict[str, List[str]]:
        """Find all patterns in the given text"""
        results = {
            'emails': [],
            'phone_numbers': [],
            'credit_cards': [],
            'ssn_numbers': [],
            'urls': [],
            'ip_addresses': [],
            'bitcoin_addresses': [],
            'file_paths': [],
            'mac_addresses': [],
            'api_keys': [],
            'aws_keys': [],
            'passwords': []
        }

        try:
            # Find all pattern types
            results['emails'] = list(set(re.findall(self.EMAIL_PATTERN, text, re.IGNORECASE)))
            results['phone_numbers'] = list(set(['-'.join(match) for match in re.findall(self.PHONE_PATTERN, text)]))
            results['credit_cards'] = list(set(re.findall(self.CREDIT_CARD_PATTERN, text)))
            results['ssn_numbers'] = list(set(re.findall(self.SSN_PATTERN, text)))
            results['urls'] = list(set(re.findall(self.URL_PATTERN, text, re.IGNORECASE)))
            results['ip_addresses'] = list(set(re.findall(self.IP_PATTERN, text)))
            results['bitcoin_addresses'] = list(set(re.findall(self.BITCOIN_PATTERN, text)))
            results['file_paths'] = list(set(re.findall(self.FILE_PATH_PATTERN, text)))
            results['mac_addresses'] = list(set(re.findall(self.MAC_PATTERN, text)))
            results['api_keys'] = list(set(re.findall(self.API_KEY_PATTERN, text, re.IGNORECASE)))
            results['aws_keys'] = list(set(re.findall(self.AWS_KEY_PATTERN, text)))
            results['passwords'] = list(set(re.findall(self.PASSWORD_PATTERN, text, re.IGNORECASE)))

        except Exception as e:
            print(f"Error finding patterns: {str(e)}")

        return results

    def generate_pattern_report(self, text: str) -> str:
        """Generate a comprehensive report of all patterns found"""
        patterns = self.find_all_patterns(text)

        report = "SHADOWTRACE PATTERN ANALYSIS REPORT\n"
        report += "=" * 50 + "\n\n"

        total_patterns = sum(len(matches) for matches in patterns.values())
        report += f"Total Suspicious Patterns Found: {total_patterns}\n\n"

        for pattern_type, matches in patterns.items():
            if matches:
                report += f"{pattern_type.replace('_', ' ').title()}: {len(matches)} found\n"
                for match in matches[:5]:  # Show first 5 matches
                    report += f"  - {match}\n"
                if len(matches) > 5:
                    report += f"  ... and {len(matches) - 5} more\n"
                report += "\n"

        if total_patterns == 0:
            report += "No suspicious patterns detected.\n"

        return report


def test_patterns():
    """Test function to demonstrate pattern detection capabilities"""
    patterns = PatternLibrary()

    # Sample text with various suspicious patterns
    test_text = """
    Contact Information:
    - Email: john.doe@example.com, admin@suspicious-site.org
    - Phone: (555) 123-4567, 555.987.6543
    - Website: https://example.com, http://malicious-site.com

    Financial Data:
    - Credit Card: 4532-1234-5678-9012
    - Bitcoin: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa

    System Information:
    - IP Address: 192.168.1.1, 10.0.0.1
    - File Path: C:\\Windows\\System32\\config.txt
    - MAC Address: 00:1B:44:11:3A:B7

    Credentials (DO NOT USE IN REAL SCENARIOS):
    - API Key: api_key_1234567890abcdef1234567890
    - AWS Key: AKIAIOSFODNN7EXAMPLE
    - Password: password=mysecretpass123
    """

    print("Testing ShadowTrace Pattern Detection...")
    print("=" * 50)

    # Test all patterns
    results = patterns.find_all_patterns(test_text)

    found_any = False
    for pattern_name, matches in results.items():
        if matches:
            found_any = True
            print(f"\n{pattern_name.replace('_', ' ').title()}: {len(matches)} found")
            for match in matches:
                print(f"  - {match}")

    if not found_any:
        print("No patterns detected.")

    # Generate full report
    print("\n" + "=" * 50)
    print("FULL REPORT:")
    print("=" * 50)
    report = patterns.generate_pattern_report(test_text)
    print(report)


# Test the patterns if this file is run directly
if __name__ == "__main__":
    test_patterns()