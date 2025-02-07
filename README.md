# **PDFEdit - CLI Tool for Removing Pages from PDFs**  

PDFEdit is a simple command-line tool that allows users to **remove specific pages** from a PDF file. It works on **Windows, macOS, and Linux**.  

## **Features**  
✅ Remove one or multiple pages from a PDF  
✅ Works on Windows, Linux, and macOS  
✅ Lightweight and fast  
✅ No GUI—pure command-line tool  
✅ Supports custom output file names  

## **Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/YarKhan02/PDFEdit.git
cd PDFEdit
```

### **2. Install Dependencies**  
```bash
pip install -r requirements.txt
```

## **Usage**  

Basic command:  

```bash
python3 pdfedit.py input.pdf 2,4,5 --output newfile
```

### **Arguments:**  
- `input.pdf` → The PDF file to edit  
- `2,4,5` → Comma-separated page numbers to remove (1-based index)  
- `--output newfile` → Optional. Output file name **without extension** (default: `output.pdf`)  

### **Examples:**  

#### **Remove pages 2 and 4 from `document.pdf` and save as `edited.pdf`**  
```bash
python3 pdfedit.py document.pdf 2,4 --output edited
```

#### **Remove a single page (e.g., page 3)**  
```bash
python3 pdfedit.py document.pdf 3
```

#### **Remove pages 1, 5, and 10, save as `cleaned.pdf`**  
```bash
python3 pdfedit.py document.pdf 1,5,10 --output cleaned
```

---

## **Contributing**  
1. Fork the repository  
2. Create a new branch: `git checkout -b feature-branch`  
3. Commit your changes: `git commit -m "Added new feature"`  
4. Push to your branch: `git push origin feature-branch`  
5. Open a pull request  

---

## **Future Enhancements**  
🔹 Support for extracting pages  
🔹 Merge multiple PDFs  
🔹 Encrypt/Decrypt PDFs  
