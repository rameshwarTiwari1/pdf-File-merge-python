import PyPDF2 

mergeFile = PyPDF2.PdfFileMerger()

#mergeFile.append(PyPDF2.PdfFileReader('E:\class content\Sem 3\Data struct\Notes\allfile.pdf', 'rb'))

mergeFile.append(PyPDF2.PdfFileReader(r'E:\class content\Sem 3\Data struct\Notes\DS_Asymptotic Notations_PDF.pdf', 'rb'))

mergeFile.append(PyPDF2.PdfFileReader(r'E:\class content\Sem 3\Data struct\Notes\DS_Array_Linear_BinarySearch_PDF.pdf', 'rb'))
mergeFile.append(PyPDF2.PdfFileReader(r'E:\class content\Sem 3\Data struct\Notes\DS_Intro&Algorithm.pdf', 'rb'))
mergeFile.append(PyPDF2.PdfFileReader(r'E:\class content\Sem 3\Data struct\Notes\DS_Singly Linked List.pdf', 'rb'))
mergeFile.append(PyPDF2.PdfFileReader(r'E:\class content\Sem 3\Data struct\Notes\DS_Sorting Algorithms_pdf.pdf', 'rb'))

                 

mergeFile.write("merged.pdf")
