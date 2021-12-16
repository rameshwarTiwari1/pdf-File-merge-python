import PyPDF2 
def merge_pdfs(_pdfs):

    mergeFile = PyPDF2.PdfFileMerger()

    for _pdf in _pdfs:

        mergeFile.append(PyPDF2.PdfFileReader(_pdf, 'rb'))

    mergeFile.write("New_Merged_File.pdf")

if __name__ == '__main__':

    _pdfs = [r'E:\\class content\\Sem 3\\Python\Notes\\15 Extended Slices.pdf',
             r'E:\\class content\Sem 3\\Python\\Notes\\Encapsulation in Python.pdf',
             r'E:\\class content\\Sem 3\\Python\Notes\\L2_3 Execution on Python_Riddhi Shah.pdf',
             r'E:\\class content\\Sem 3\\Python\\Notes\\L4 Python IDEs.pdf',
             r'E:\\class content\\Sem 3\\Python\\Notes\\L5 Python Variables, Constants & Literals.pdf',
             r'E:\\class content\\Sem 3\\Python\\Notes\\L6 Fundamental concepts about Control Structures.pdf',
             r'E:\\class content\\Sem 3\\Python\\Notes\\Operators in Python.pdf',
             r'E:\\class content\\Sem 3\\Python\\Notes\\Python Dictionary.pdf',
             r'E:\\class content\\Sem 3\\Python\\Notes\\Python Lists.pdf',
             r'E:\\class content\\Sem 3\\Python\\Notes\\Python String.pdf',
             r'E:\\class content\\Sem 3\\Python\\Notes\\Python Tuples.pdf']
    #here you can add multiple file like this in a same dir

    merge_pdfs(_pdfs)
