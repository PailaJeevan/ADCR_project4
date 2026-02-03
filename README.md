
# 📄 Automated Document Processing, Categorization & Report Generation System

## 📌 Project Overview
This project is a **Python-based automation system** designed to process large volumes of documents with minimal human intervention.  
It reads multiple file formats, extracts text, categorizes documents using rule-based logic, generates summaries, and produces professional PDF reports.

The system closely resembles **enterprise-level document automation workflows** used in corporate offices, banks, legal firms, HR departments, and finance teams.

---

## 🎯 Project Objectives
- Automate document reading and text extraction
- Reduce manual effort in document classification
- Generate meaningful summaries and insights
- Maintain structured outputs for easy auditing
- Demonstrate real-world Python automation skills

---

## 🚀 Key Features
✔ Multi-format file processing (PDF, DOCX, TXT, XLSX)  
✔ Rule-based document categorization (No ML required)  
✔ Automatic summary generation (4–5 lines)  
✔ Keyword extraction  
✔ Date and amount detection (₹ and $ supported)  
✔ Word count & character count  
✔ Professional PDF report generation  
✔ Centralized logging with timestamps  

---

## 📂 Folder Structure
```
project/
│── input_documents/
│
│── output/
│   ├── summaries/
│   ├── categories/
│   ├── reports/
│
│── logs/
│   └── system.log
│
│── utils/
│   ├── file_reader.py
│   ├── classifier.py
│   ├── report_generator.py
│   └── logger.py
│
│── main.py
│── README.md
```

---

## 🗂 Document Categories & Rules
Documents are classified using **keyword-based rules**:

| Category | Sample Keywords |
|--------|----------------|
| HR | employee, salary, leave, attendance |
| Finance | invoice, bill, receipt, payment |
| Operations | order, delivery, shipment, inventory |
| Legal | contract, agreement, dispute, lawsuit |
| Unknown | No keyword matched |

> This approach avoids complexity while ensuring fast and explainable classification.

---

## 🧠 Information Extracted from Documents
For every processed document, the system extracts:
- **Summary** (first 4–5 meaningful sentences)
- **Top keywords** (most frequent terms)
- **Dates** (DD/MM/YYYY or DD-MM-YYYY)
- **Amounts** (supports ₹ and $ symbols)
- **Word count**
- **Character count**

---

## 📄 Generated Output Files
For each input document:
- 📄 `*_summary.txt` → Text summary  
- 🗂 `*_category.txt` → Assigned category  
- 📑 `*.pdf` → Detailed PDF report  

All outputs are stored in the `output/` folder.

---

## 📝 Logging System
A centralized log file is maintained:
```
logs/system.log
```
Each log entry contains:
- Timestamp
- Document name
- Assigned category
- Processing status
- Error details (if any)

---

## 🛠 Technologies & Libraries Used
- Python 3.x
- pdfplumber (PDF reading)
- python-docx (Word documents)
- openpyxl (Excel files)
- reportlab (PDF generation)
- re (pattern matching)
- logging
- datetime
- collections

---

## ▶ How to Run the Project
1. Place documents inside:
```
input_documents/
```

2. Run the program:
```bash
python main.py
```

3. View results inside:
```
output/
```

---

## 📊 Sample Console Output
```
✔ Processed: invoice_january.pdf
✔ Processed: employee_policy.docx
✖ Skipped notes.txt: Empty or unreadable
```

---

## 🔮 Future Enhancements
- Machine learning-based classification
- OCR support for scanned PDFs
- Web-based dashboard
- Database integration
- Email delivery of reports
- Multi-language document support

---

## 🎓 Academic Relevance
This project is ideal for:
- Mini projects
- Final year projects
- Python automation labs
- Resume & interview demonstrations

---

## 👨‍💻 Author
- 👨‍💻 **Developer:** Paila Jeevan
- 📧 **Email:** pailajeevan21@gmail.com
- 🌐 **GitHub:**
https://github.com/PailaJeevan  
Automated Document Processing & Python Automation System
