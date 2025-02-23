import argparse
import os
import fitz  # PyMuPDF
import sys

def remove_page(file_name, pages_to_remove, output_file):
    # Validate input file
    if not os.path.isfile(file_name):
        print("Error: Input file not found!")
        sys.exit(1)

    # Open file
    doc = fitz.open(file_name)

    # Remove pages 
    for i in pages_to_remove:
        try:
            doc.delete_page(i - 1)
        except Exception as e:
            print(f'Error removing page {i}: {e}')
            sys.exit(1)

    doc.save(output_file)
    print(f"Success! Saved as: {output_file}")

def main():
    """Handles command-line arguments and runs the remove_page function."""
    
    parser = argparse.ArgumentParser(description="Remove specific pages from a PDF file.")
    parser.add_argument("input", help="Path to the input PDF file")
    parser.add_argument("pages", help="Comma-separated page numbers to remove (e.g., 1,2,3)")
    parser.add_argument("output", nargs="?", default="output.pdf", help="Name of the output PDF file (optional)")

    args = parser.parse_args()

    # Convert page numbers to a list of integers
    try:
        pages_to_remove = sorted(list(map(int, args.pages.split(","))), reverse=True)
        if any(p <= 0 for p in pages_to_remove):
            print("Error: Page numbers must be positive integers!")
            sys.exit(1)
    except ValueError:
        print("Error: Page numbers must be integers separated by commas! e.g -> (1,2,3)")
        sys.exit(1)

    if "." in args.output and not args.output.endswith(".pdf"):
        print("Error: Output file should have a '.pdf' extension.")
        sys.exit(1)

    output_file = args.output if args.output.endswith(".pdf") else args.output + ".pdf"

    remove_page(args.input, pages_to_remove, output_file)


if __name__ == '__main__':
    main()