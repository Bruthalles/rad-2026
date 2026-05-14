import re,os

base = os.path.dirname(__file__)
caminho = os.path.join(base, 'arquivo_leitura.txt')

pattern = r'(?<=total:)\D+\d+[,.]\d+'

with open(caminho, 'r', encoding='utf-8') as f:
    arquivo = f.readlines()

for linha in arquivo:
    matches = re.findall(pattern, linha)
    print(matches)