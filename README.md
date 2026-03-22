# 🔐 File Integrity Checker

## 📌 Project Overview
The **File Integrity Checker** is a Python-based tool designed to monitor changes in files by calculating and comparing cryptographic hash values. It helps in detecting unauthorized modifications, additions, or deletions of files within a specified directory. This project is developed as part of a Cyber Security Internship Task.

## 🎯 Objective
To build a system that ensures file integrity by generating hash values of files, storing hash records securely, and detecting any changes by comparing hashes over time.

## 🛠️ Technologies Used
- Python 3  
- hashlib – for generating secure hash values (SHA-256)  
- os – for directory traversal  
- json – for storing and retrieving hash records  

## ⚙️ Features
- Calculates SHA-256 hash for each file  
- Detects modified files, new files, and deleted files  
- Stores hash values in a structured JSON file  
- Easy to use command-line interface  
- Well-structured and modular code  

## 📂 Project Structure
file-integrity-checker/  
├── file_integrity_checker.py   # Main Python script  
├── hash_store.json             # Stored hash values (auto-generated)  
└── README.md                   # Project documentation  

## ▶️ How to Run the Project
Step 1: Clone the Repository  
git clone https://github.com/your-username/file-integrity-checker.git  

Step 2: Navigate to the Project Directory  
cd file-integrity-checker  

Step 3: Run the Script  
python file_integrity_checker.py  

Step 4: Provide Directory Path  
Enter the directory you want to monitor when prompted.

## 🧪 Sample Output
Enter the directory path to monitor: C:\TestFolder  
Scanning files...  
--- File Integrity Report ---  
[MODIFIED] C:\TestFolder\example.txt  
[NEW] C:\TestFolder\new_file.txt  
[DELETED] C:\TestFolder\old_file.txt  
--- Scan Complete ---  
Hash values stored successfully.  

## 🔍 How It Works
The script scans all files in the specified directory, generates a SHA-256 hash for each file, and stores these hash values in a JSON file. On subsequent runs, hashes are recalculated and compared with previously stored values to detect any modifications, additions, or deletions.

## 📌 Use Cases
- Detect unauthorized file modifications  
- Monitor sensitive directories  
- Basic intrusion detection support  
- Data integrity verification  

## 🚀 Future Enhancements
- Real-time monitoring using file system watchers  
- Graphical User Interface (GUI)  
- Email or notification alerts on changes  
- Support for multiple hash algorithms  

## 👨‍💻 Author
Neeraj Bhujbal

## 📎 Submission Note
This project is submitted as part of the Cyber Security Internship Task (Task 1), as per the given instructions.
