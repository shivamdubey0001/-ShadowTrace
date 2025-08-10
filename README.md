# 🔍 ShadowTrace - Digital Footprint & Suspicious Pattern Finder

**A powerful Python CLI tool for detecting suspicious patterns and analyzing digital footprints in text data.**

---

## 🤔 What is ShadowTrace?

Hey there! I'm Shivam Dubey, and I built this tool because I wanted to create something that could help people understand what kind of sensitive information might be hiding in their text data. 

ShadowTrace is like a digital detective - it scans through any text you give it and finds potentially risky information like:
- Email addresses and phone numbers
- Credit card numbers (super dangerous if exposed!)
- Social security numbers
- Web links and IP addresses
- Bitcoin wallet addresses
- API keys and passwords
- And much more!

Think of it as your personal security scanner that helps you check if your data contains anything that shouldn't be shared publicly.

---

## 🎯 Why Did I Build This?

I was working on a cybersecurity project for college and realized there wasn't a simple, beginner-friendly tool that could:
- Detect multiple types of suspicious patterns at once
- Give you a clear risk assessment 
- Work right from the command line
- Look professional but still be easy to understand

So I decided to build one myself! This tool is perfect for:
- **Students** learning about cybersecurity and data analysis
- **Developers** who want to scan their code/logs for exposed secrets
- **Anyone** curious about what sensitive info might be in their text files

---

## ✨ What Can ShadowTrace Do?

### 🔍 **Pattern Detection**
- **Financial Data**: Credit cards, Bitcoin addresses, banking info
- **Personal Info**: Email addresses, phone numbers, social security numbers
- **Security Credentials**: API keys, passwords, AWS keys, JWT tokens
- **Network Data**: IP addresses, URLs, MAC addresses, file paths

### 📊 **Smart Analysis**
- **Word Frequency**: Shows you the most common words in your text
- **Sentiment Analysis**: Tells you if the text feels positive, negative, or neutral
- **Risk Scoring**: Gives you a percentage score (0% = safe, 100% = very risky)
- **Detailed Reports**: Saves everything to a file you can review later

### 🎨 **Beautiful Interface**
- Colorful terminal output (works on Windows, Mac, Linux)
- Loading animations and progress bars
- Professional-looking reports
- Easy-to-understand results

---

## 🚀 How to Get Started

### Prerequisites
You just need Python 3.7 or newer. That's it! No complicated installations.

### Installation
1. **Download the files**: Get all 4 Python files and put them in the same folder
   - `main.py`
   - `analyzer.py` 
   - `utils.py`
   - `patterns.py`

2. **Run the program**:
   ```bash
   python main.py
   ```

That's literally it! The tool will guide you through everything else.

---

## 🎮 How to Use ShadowTrace

### Step 1: Start the Program
```bash
python main.py
```
You'll see a cool welcome screen with the ShadowTrace logo.

### Step 2: Choose Input Method
The tool will ask you how you want to input your data:
- **Option 1**: Type or paste text directly
- **Option 2**: Load text from a file (like .txt, .log, etc.)

### Step 3: View Results
ShadowTrace will show you:
- 📌 **Suspicious Patterns Found**: What risky data was detected
- 📊 **Word Frequency**: Most common words in your text
- 😊 **Sentiment**: Overall tone of the text
- ⚠️ **Risk Score**: How dangerous the data might be if exposed

### Step 4: Save Report (Optional)
You can save all results to a timestamped file for later review.

---

## 📱 Example Usage

Let's say you have this text:
```
Hi! My email is john@company.com and my phone is (555) 123-4567.
My credit card is 4532-1234-5678-9012. Please send money to Bitcoin 
address: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
Visit https://example.com for more info.
```

ShadowTrace will detect:
- ✉️ **Email**: john@company.com
- 📞 **Phone**: (555) 123-4567  
- 💳 **Credit Card**: 4532-1234-5678-9012 (HIGH RISK!)
- ₿ **Bitcoin**: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
- 🌐 **URL**: https://example.com
- ⚠️ **Risk Score**: 87% (Very High Risk!)

---

## 🗂️ Project Structure

```
ShadowTrace/
│
├── main.py          # Main program - handles user interface
├── analyzer.py      # Core analysis logic and risk scoring
├── utils.py         # Colors, formatting, and helper functions  
├── patterns.py      # Regex patterns for detecting suspicious data
└── README.md        # This file you're reading!
```

### What Each File Does:

**🎮 main.py** - The "controller"
- Handles all user interaction
- Shows the welcome screen and menus
- Gets input from user (typing or file upload)
- Displays results in a nice format
- Saves reports to files

**🧠 analyzer.py** - The "brain" 
- Does all the smart analysis work
- Finds suspicious patterns in text
- Calculates risk scores and sentiment
- Counts word frequency
- Combines everything into final results

**🎨 utils.py** - The "stylist"
- Makes everything look colorful and professional
- Handles screen clearing and formatting
- Creates progress bars and loading animations
- Provides helper functions for input/output

**🔍 patterns.py** - The "detective"
- Contains all the regex patterns for finding suspicious data
- Knows how to detect 19 different types of risky information
- Validates found patterns (like checking if credit cards are real)
- Assigns risk levels to different pattern types

---

## 🛡️ What Makes This Tool Special?

### 🎯 **Real-World Focused**
- Patterns are tested on actual data to minimize false positives
- Risk scoring is based on real cybersecurity threat levels
- Works with messy, real-world text (not just perfect examples)

### 🚀 **Performance Optimized**
- Pre-compiled regex patterns for fast scanning
- Efficient algorithms that work on large text files
- Smart duplicate removal and data processing

### 💪 **Robust & Safe**
- Comprehensive error handling prevents crashes
- Works across different operating systems
- Validates all input and handles edge cases gracefully

### 🎓 **Educational Value**
- Clean, well-commented code that's easy to learn from
- Demonstrates real cybersecurity concepts
- Shows advanced Python techniques and best practices

---

## ⚠️ Important Notes

### 🔒 **Privacy & Security**
- This tool runs completely offline - your data never leaves your computer
- It's designed for legitimate security analysis and education
- Always respect privacy laws when analyzing data that isn't yours

### 🎯 **Use Cases**
- ✅ Checking your own documents for sensitive info before sharing
- ✅ Educational projects and cybersecurity learning
- ✅ Code review to find accidentally committed secrets
- ✅ Log analysis for security incidents

### 🚫 **Not Intended For**
- Analyzing other people's private data without permission
- Any malicious or illegal activities
- Production security monitoring (this is a learning tool)

---

## 🐛 Troubleshooting

### Common Issues:

**Problem**: Colors don't show up properly on Windows
- **Solution**: Use Windows 10+ or try Windows Terminal app

**Problem**: "ModuleNotFoundError" when running
- **Solution**: Make sure all 4 .py files are in the same folder

**Problem**: Can't read certain file formats
- **Solution**: Convert to plain text (.txt) format first

**Problem**: Tool seems to miss some patterns
- **Solution**: The patterns are tuned to avoid false positives, so very unusual formats might not be detected

---

## 🚀 Future Ideas

I'm thinking about adding these features in the future:
- Support for more file formats (PDF, Word docs, etc.)
- Additional pattern types (passport numbers, license plates)
- Export results to different formats (JSON, CSV)
- Batch processing of multiple files
- Simple GUI version for non-technical users

If you have suggestions or find bugs, feel free to reach out!

---

## 📚 Learning Resources

If you want to learn more about the concepts used in this tool:

**Regex (Pattern Matching)**:
- Practice with online regex testers
- Learn pattern matching for text analysis

**Python Skills**:
- File handling and text processing
- Object-oriented programming
- Error handling and exceptions
- Command-line interface design

**Cybersecurity Concepts**:
- Data loss prevention (DLP)
- Sensitive data identification
- Risk assessment and scoring
- Digital forensics basics

---

## 🎉 Final Thoughts

Building ShadowTrace was a fun project that taught me a lot about cybersecurity, Python programming, and creating user-friendly tools. I hope it helps you learn something new too!

Remember: the goal of this tool is to make people more aware of digital security and help them protect their sensitive information. Use it responsibly and keep learning!

---

**Made with ❤️ by Shivam Dubey**

*If this tool helped you learn something new or solved a problem, that makes me happy! Keep exploring and building cool stuff.* 🚀

---

## 📄 License

This project is open source and available under the MIT License.
