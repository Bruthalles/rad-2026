#ler txt, json, ou csv usa open
dicas_regex = open(r"rad.19-03.txt",'r',encoding = "utf-8").read()

#ler jsons de maneira melhor
#import json
#stringfy()   ////    converte json -> string
#json.loads() ////    converte string -> json

#ler csv de maneira melhor
#import pandas
#dicas_regex = pd.read_csv(r"arq.csv",delimiter="delimitador do arquivo")

#ler pdf
#import pdfminer ou py2pdf

#ler texto de imagens
#import OCR pytesseract
