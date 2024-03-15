import os
import PyPDF2


dir = os.path.dirname(os.path.abspath(__file__))
arqv = os.path.join(dir, 'rename.py')
p1 = "0001-04"
a = 'NOME 1'
p2 = "0004-57"
b = 'NOME 2'

c1 = c2 = 0

for nome_arquivo in os.listdir(dir):
    if nome_arquivo.endswith(".pdf"):
        caminho_completo = os.path.join(dir, nome_arquivo)
        with open(caminho_completo, "rb") as pdf_file:
            leitor_pdf = PyPDF2.PdfReader(pdf_file)
            texto_pdf = ""
            print('RENOMEANDO...')
            for pagina in range(len(leitor_pdf.pages)):
                texto_pdf += leitor_pdf.pages[pagina].extract_text()

            if p1 in texto_pdf:
                novo_nome = a + "_" + str(c1) + ".pdf"
                novo_caminho = os.path.join(dir, novo_nome)
                c1 += 1
            else: p2 in texto_pdf:
                novo_nome = b + "_" + str(c2) + ".pdf"
                novo_caminho = os.path.join(dir, novo_nome)
                c2 += 1

        os.rename(caminho_completo, novo_caminho)
      #  controle do ctrl z _
    print('FIM...')
