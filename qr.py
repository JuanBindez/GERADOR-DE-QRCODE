import pyqrcode
import png
from pyqrcode import QRCode

link = str(input("cole seu link aqui:\n"))
nome_de_saida = str(input("digite o nome de saida do arquivo com estensão .svg ou .png\n"))

url = pyqrcode.create(link)

url.svg(nome_de_saida, scale = 8)
url.png(nome_de_saida, scale = 6)