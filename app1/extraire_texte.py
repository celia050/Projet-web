import pdfplumber
"""import textract """
import pathlib

def extraction(fichier):
    f=pathlib.Path(fichier)
    """if f.suffix == "txt":
        return textract.process(fichier)"""
    if f.suffix == "pdf":
        f=pdfplumber.open(fichier)
        return f.extract_text()