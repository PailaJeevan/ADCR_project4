# Author: Paila Jeevan
# Purpose: Main script to process documents,classify them,extract details,and generate reports.
# Tools Used: Python, ReportLab,Custom Utilities
# TODO: Enhance classification model,improve detail extraction accuracy.
# Project: Automated Document Processing,Categorization and Report Generation System

import os
from utils.file_reader import FileReading
from utils.classifier import DocumentClassify
from utils.report_generator import  generating_pdf
from utils.logger import  seting_logger
import re # Regular expressions for detail extraction
from collections import Counter #imported libraries


print("🚀 Starting Document Processing System")
print("🔍 Reading documents from 'input_documents' folder")
print("🗂️  Classifying and extracting details")
print("📄 Generating PDF reports")
print("✅ Process completed. Check 'output' folder for results.")
print("--------------------------------------------------") 
print("Add your documents to the 'input_documents' folder and rerun the script to process more files.\n\n")

# ------------------ Fixed Folders ------------------ #
INPUT_DIR = "input_documents" # Input folder for documents
SUMMARY_DIR = "output/summaries" # Output folder for summaries
CATEGORY_DIR = "output/categories" # Output folder for categories
REPORT_DIR = "output/reports" # Output folder for PDF reports

# Ensure output folders exist
os.makedirs(SUMMARY_DIR, exist_ok=True) # Create summaries directory if not exists
os.makedirs(CATEGORY_DIR, exist_ok=True) # Create categories directory if not exists
os.makedirs(REPORT_DIR, exist_ok=True)# Create reports directory if not exists

# Initialize modules
reader = FileReading()
classifier = DocumentClassify()
logger = seting_logger()

#
def extracting_details(text):
    words = re.findall(r'\b\w+\b', text.lower())
    summary = ". ".join(re.split(r'[.!?]', text)[:5]).strip()
    keywords = [word for word, _ in Counter(words).most_common(5)]
    dates = re.findall(r'\b\d{2}[/-]\d{2}[/-]\d{4}\b', text) # Date pattern DD/MM/YYYY or DD-MM-YYYY
    amounts = re.findall(r'(₹|\$)?\s?\d+(?:,\d+)*(?:\.\d+)?', text) # Amount pattern with optional currency symbols (₹, $)
# Special requirement: Handle mixed currency symbols (₹, $)

    return {
        "Summary": summary,
        "Keywords": keywords,
        "Dates Found": dates,
        "Amounts Found": amounts,
        "Word Count": len(words),
        "Character Count": len(text)
    }

#main processing function
def main():
    if not os.path.exists(INPUT_DIR):
        print(f"Input folder '{INPUT_DIR}' does not exist.")
        return

    files = [os.path.join(INPUT_DIR, f) for f in os.listdir(INPUT_DIR)] # List all files in input directory

    for file_path in files:
        filename = os.path.basename(file_path)

        try:
            content = reader.reading_file(file_path)
            if not content.strip():
                logger.error(f"{filename} | ERROR | Empty or unreadable file")
                print(f"✖ Skipped {filename}: Empty or unreadable")
                continue

            category = classifier.classifer(content)
            details = extracting_details(content)

            base_name = os.path.splitext(filename)[0]

            # Save summary
            with open(f"{SUMMARY_DIR}/{base_name}_summary.txt", "w", encoding="utf-8") as f:
                f.write(details["Summary"])

            # Save category
            with open(f"{CATEGORY_DIR}/{base_name}_category.txt", "w", encoding="utf-8") as f:
                f.write(category)

            # Generate PDF report
            pdf_data = {
                "Document Name": filename,
                "Category": category,
                **details
            }
            generating_pdf(f"{REPORT_DIR}/{base_name}.pdf", pdf_data)

            # Log success
            logger.info(f"{filename} | {category} | Processed Successfully")
            print(f"✔ Processed: {filename}")

        except Exception as e:
            logger.error(f"{filename} | ERROR | {str(e)}")
            print(f"✖ Error processing {filename}")

if __name__ == "__main__":
    main()
