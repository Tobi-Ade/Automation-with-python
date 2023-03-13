from PyPDF2 import PdfReader, PdfWriter
import time


def merge_pdfs(pdf_paths, output):
    
    # create a pdf writer object to
    pdf_writer = PdfWriter()
    
    # iterate through the pdf_paths
    
    for pdf in pdf_paths:
        # create a pdf reader object for each pdf
        pdf_reader = PdfReader(pdf)
        # get the pages in each pdf and add to the writer object
        for page in range(len(pdf_reader.pages)):
            print(page)
            pdf_writer.add_page(pdf_reader.pages[page])
            
    # write the merged pdf to a file
    
    with open(output, 'wb') as outfile:
        pdf_writer.write(outfile)
        


if __name__ == "__main__":
    pdf_paths = ['Readable_Code.pdf','Spreadsheet_errors.pdf']
    output = 'merged.pdf'
    merge_pdfs(pdf_paths, output)
        
       