#!/usr/bin/env python3
"""
ShadowTrace - Digital Footprint & Suspicious Pattern Finder
Analysis Engine - Core Logic for Pattern Detection and Risk Assessment
Author: Your Name
Version: 1.0
"""

import re
import string
from collections import Counter
from typing import Dict, List, Tuple, Any

# Import our pattern definitions
try:
    from patterns import PatternLibrary
except ImportError:
    print("Error: patterns.py not found. Make sure all files are in the same directory.")
    import sys
    sys.exit(1)


class SentimentAnalyzer:
    """Simple sentiment analysis using word-based approach"""

    def __init__(self):
        # Positive words for sentiment analysis
        self.positive_words = {
            'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'perfect',
            'love', 'like', 'enjoy', 'happy', 'pleased', 'satisfied', 'awesome',
            'brilliant', 'outstanding', 'superb', 'marvelous', 'terrific', 'fabulous',
            'nice', 'beautiful', 'pretty', 'cool', 'sweet', 'fun', 'exciting',
            'positive', 'successful', 'win', 'victory', 'triumph', 'achieve', 'accomplish'
        }

        # Negative words for sentiment analysis
        self.negative_words = {
            'bad', 'terrible', 'awful', 'horrible', 'disgusting', 'hate', 'dislike',
            'angry', 'mad', 'furious', 'upset', 'sad', 'depressed', 'disappointed',
            'frustrated', 'annoyed', 'irritated', 'worried', 'scared', 'afraid',
            'dangerous', 'risky', 'threat', 'attack', 'hack', 'steal', 'fraud',
            'scam', 'virus', 'malware', 'suspicious', 'illegal', 'criminal', 'kill',
            'destroy', 'damage', 'harm', 'hurt', 'problem', 'issue', 'fail', 'failure'
        }

        # Suspicious/risky words that increase risk score
        self.risky_words = {
            'password', 'login', 'admin', 'root', 'hack', 'crack', 'exploit',
            'vulnerability', 'backdoor', 'trojan', 'virus', 'malware', 'ransomware',
            'phishing', 'scam', 'fraud', 'steal', 'money', 'bank', 'account',
            'credit', 'debit', 'ssn', 'social', 'security', 'personal', 'private',
            'confidential', 'secret', 'hidden', 'anonymous', 'darkweb', 'bitcoin',
            'cryptocurrency', 'illegal', 'drugs', 'weapon', 'bomb', 'attack'
        }

    def analyze_sentiment(self, text: str) -> str:
        """Analyze sentiment of text and return Positive/Negative/Neutral"""
        # Convert to lowercase and remove punctuation
        text_clean = text.lower().translate(str.maketrans('', '', string.punctuation))
        words = text_clean.split()

        positive_count = sum(1 for word in words if word in self.positive_words)
        negative_count = sum(1 for word in words if word in self.negative_words)

        # Determine sentiment based on word counts
        if positive_count > negative_count:
            return "Positive"
        elif negative_count > positive_count:
            return "Negative"
        else:
            return "Neutral"

    def calculate_risk_from_words(self, text: str) -> int:
        """Calculate risk score based on risky words found"""
        text_clean = text.lower().translate(str.maketrans('', '', string.punctuation))
        words = text_clean.split()

        risky_word_count = sum(1 for word in words if word in self.risky_words)
        total_words = len(words)

        if total_words == 0:
            return 0

        # Calculate percentage of risky words
        risk_percentage = (risky_word_count / total_words) * 100

        # Cap at 50% since we'll add pattern-based risk too
        return min(int(risk_percentage * 2), 50)


class SuspiciousPatternAnalyzer:
    """Main analyzer class that detects patterns and calculates risk"""

    def __init__(self):
        self.patterns = PatternLibrary()
        self.sentiment_analyzer = SentimentAnalyzer()

    def find_patterns(self, text: str) -> Dict[str, List[str]]:
        """Find all suspicious patterns in the text"""
        found_patterns = {
            'emails': [],
            'phone_numbers': [],
            'credit_cards': [],
            'ssn_numbers': [],
            'urls': [],
            'ip_addresses': [],
            'bitcoin_addresses': [],
            'file_paths': []
        }

        try:
            # Find email addresses
            email_matches = re.findall(self.patterns.EMAIL_PATTERN, text, re.IGNORECASE)
            found_patterns['emails'] = list(set(email_matches))  # Remove duplicates

            # Find phone numbers
            phone_matches = re.findall(self.patterns.PHONE_PATTERN, text)
            found_patterns['phone_numbers'] = list(set(phone_matches))

            # Find credit card numbers
            cc_matches = re.findall(self.patterns.CREDIT_CARD_PATTERN, text)
            found_patterns['credit_cards'] = list(set(cc_matches))

            # Find SSN numbers
            ssn_matches = re.findall(self.patterns.SSN_PATTERN, text)
            found_patterns['ssn_numbers'] = list(set(ssn_matches))

            # Find URLs
            url_matches = re.findall(self.patterns.URL_PATTERN, text, re.IGNORECASE)
            found_patterns['urls'] = list(set(url_matches))

            # Find IP addresses
            ip_matches = re.findall(self.patterns.IP_PATTERN, text)
            found_patterns['ip_addresses'] = list(set(ip_matches))

            # Find Bitcoin addresses
            bitcoin_matches = re.findall(self.patterns.BITCOIN_PATTERN, text)
            found_patterns['bitcoin_addresses'] = list(set(bitcoin_matches))

            # Find file paths
            path_matches = re.findall(self.patterns.FILE_PATH_PATTERN, text)
            found_patterns['file_paths'] = list(set(path_matches))

        except Exception as e:
            print(f"Error during pattern matching: {str(e)}")

        return found_patterns

    def analyze_word_frequency(self, text: str, top_n: int = 20) -> List[Tuple[str, int]]:
        """Analyze word frequency in the text"""
        try:
            # Clean the text - remove punctuation and convert to lowercase
            text_clean = text.lower()

            # Remove punctuation but keep spaces
            translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
            text_clean = text_clean.translate(translator)

            # Split into words and filter out empty strings and short words
            words = [word for word in text_clean.split() if len(word) > 2]

            # Common stop words to ignore
            stop_words = {
                'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with',
                'by', 'from', 'up', 'about', 'into', 'through', 'during', 'before',
                'after', 'above', 'below', 'between', 'among', 'through', 'during',
                'before', 'after', 'above', 'below', 'between', 'this', 'that', 'these',
                'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her',
                'us', 'them', 'my', 'your', 'his', 'its', 'our', 'their', 'am', 'is',
                'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
                'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might',
                'must', 'can', 'shall', 'a', 'an'
            }

            # Filter out stop words
            filtered_words = [word for word in words if word not in stop_words]

            # Count word frequency
            word_counts = Counter(filtered_words)

            # Return top N most common words
            return word_counts.most_common(top_n)

        except Exception as e:
            print(f"Error during word frequency analysis: {str(e)}")
            return []

    def calculate_pattern_risk(self, patterns: Dict[str, List[str]]) -> int:
        """Calculate risk score based on patterns found"""
        risk_score = 0

        # Risk weights for different pattern types
        risk_weights = {
            'emails': 5,           # Low risk - emails are common
            'phone_numbers': 8,    # Medium risk
            'urls': 6,             # Low-medium risk
            'ip_addresses': 12,    # Higher risk
            'credit_cards': 25,    # High risk - financial data
            'ssn_numbers': 30,     # Very high risk - personal ID
            'bitcoin_addresses': 15, # High risk - crypto related
            'file_paths': 10       # Medium-high risk - system paths
        }

        try:
            for pattern_type, matches in patterns.items():
                if matches:  # If any matches found
                    count = len(matches)
                    weight = risk_weights.get(pattern_type, 5)

                    # Calculate risk for this pattern type
                    pattern_risk = min(count * weight, 40)  # Cap individual pattern risk at 40
                    risk_score += pattern_risk

            # Cap total pattern risk at 70%
            return min(risk_score, 70)

        except Exception as e:
            print(f"Error calculating pattern risk: {str(e)}")
            return 0

    def calculate_total_risk(self, patterns: Dict[str, List[str]], text: str) -> int:
        """Calculate total risk score combining patterns and content analysis"""
        try:
            # Get pattern-based risk
            pattern_risk = self.calculate_pattern_risk(patterns)

            # Get word-based risk
            word_risk = self.sentiment_analyzer.calculate_risk_from_words(text)

            # Combine risks (pattern risk has more weight)
            total_risk = int(pattern_risk * 0.7 + word_risk * 0.3)

            # Add bonus risk for multiple pattern types
            pattern_types_found = sum(1 for matches in patterns.values() if matches)
            if pattern_types_found >= 3:
                total_risk += 15  # Bonus risk for multiple suspicious patterns
            elif pattern_types_found >= 2:
                total_risk += 8

            # Ensure risk is between 0 and 100
            return max(0, min(total_risk, 100))

        except Exception as e:
            print(f"Error calculating total risk: {str(e)}")
            return 0

    def analyze(self, text: str) -> Dict[str, Any]:
        """Main analysis function that returns all results"""
        try:
            # Validate input
            if not text or not text.strip():
                return {
                    'patterns': {},
                    'frequency': [],
                    'sentiment': 'Neutral',
                    'risk_score': 0
                }

            # Find suspicious patterns
            patterns = self.find_patterns(text)

            # Analyze word frequency
            frequency = self.analyze_word_frequency(text)

            # Analyze sentiment
            sentiment = self.sentiment_analyzer.analyze_sentiment(text)

            # Calculate risk score
            risk_score = self.calculate_total_risk(patterns, text)

            # Return comprehensive analysis results
            return {
                'patterns': patterns,
                'frequency': frequency,
                'sentiment': sentiment,
                'risk_score': risk_score
            }

        except Exception as e:
            print(f"Error during analysis: {str(e)}")
            # Return safe default values in case of error
            return {
                'patterns': {},
                'frequency': [],
                'sentiment': 'Neutral',
                'risk_score': 0
            }

    def get_analysis_summary(self, analysis_result: Dict[str, Any]) -> str:
        """Generate a human-readable summary of the analysis"""
        try:
            patterns = analysis_result['patterns']
            risk_score = analysis_result['risk_score']
            sentiment = analysis_result['sentiment']

            # Count total patterns found
            total_patterns = sum(len(matches) for matches in patterns.values())

            # Generate summary text
            summary = f"Analysis Summary:\n"
            summary += f"- Found {total_patterns} suspicious patterns\n"
            summary += f"- Sentiment: {sentiment}\n"
            summary += f"- Risk Score: {risk_score}%\n"

            if risk_score >= 80:
                summary += "- Risk Level: VERY HIGH - Immediate attention required\n"
            elif risk_score >= 60:
                summary += "- Risk Level: HIGH - Review recommended\n"
            elif risk_score >= 40:
                summary += "- Risk Level: MEDIUM - Monitor closely\n"
            else:
                summary += "- Risk Level: LOW - Appears safe\n"

            return summary

        except Exception as e:
            return f"Error generating summary: {str(e)}"


# Test function for development
def test_analyzer():
    """Test function to check if analyzer works correctly"""
    analyzer = SuspiciousPatternAnalyzer()

    test_text = """
    Hey there! My email is john.doe@example.com and my phone is (555) 123-4567.
    My credit card number is 4532-1234-5678-9012. Please transfer money to my 
    Bitcoin address: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
    You can visit https://example.com for more info.
    This is a test of the suspicious pattern detection system.
    """

    result = analyzer.analyze(test_text)

    print("Test Results:")
    print("=============")
    print(f"Patterns found: {result['patterns']}")
    print(f"Top words: {result['frequency'][:5]}")
    print(f"Sentiment: {result['sentiment']}")
    print(f"Risk Score: {result['risk_score']}%")

    summary = analyzer.get_analysis_summary(result)
    print(f"\nSummary:\n{summary}")


# Run test if this file is executed directly
if __name__ == "__main__":
    test_analyzer()