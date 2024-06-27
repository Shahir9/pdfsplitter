from pypdf import PdfReader, PdfWriter

def split_pdf(input_pdf, output_prefix, pages_per_split):
    # Open the input PDF file
    with open(input_pdf, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)
        
        # Calculate the number of split PDFs needed
        num_splits = (total_pages + pages_per_split - 1) // pages_per_split
        
        for i in range(num_splits):
            pdf_writer = PdfWriter()
            start_page = i * pages_per_split
            end_page = min(start_page + pages_per_split, total_pages)
            
            # Add pages to the new PDF
            for page in range(start_page, end_page):
                pdf_writer.add_page(pdf_reader.pages[page])
            
            # Save the split PDF
            output_pdf = f"{output_prefix}_part{i + 1}.pdf"
            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)
            
            print(f"Created {output_pdf}")

# Usage
input_pdf = r'sample.pdf'  # Replace with your input PDF file
output_prefix = r'output\output'  # Prefix for the output files
pages_per_split = 500  # Number of pages per split

split_pdf(input_pdf, output_prefix, pages_per_split)
