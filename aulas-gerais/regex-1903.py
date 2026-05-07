
nota_fiscal = '''
Nome: pedro dos santos             Data nascimento: 01/01/2000
cpf: 123.456.789-00       Endereço: nova america, del castilho                                    
                                                                 loja 3
Valor dos serviços: R$ 1.200,00
Tipo de contrato: Mei
--------------------------------------------------------------
Nome: ana             Data nascimento: 01-01-2010
cpf: 123.456.789-00       Endereço: norte shop
Valor dos serviços: R$ 1200
Tipo de contrato: clt
'''

#############################################

import re

def venda_principal():
    exp_valor = r".+ {0,1}R\$ {0,1}[\d,.]+"
    produto = re.findall(exp_valor, nota_fiscal)
    print(produto)
    return 0

def data_nascimento():
    exp_data = r"(?<=[dD]ata[.+ ][nN]ascimento: )\d{2}\W\d{2}\W\d{4}"
    data = re.findall(exp_data, nota_fiscal)
    print(data)
    return 0

def endereco():
    exp_endereco = r"(?<=[eE]ndere[cç]o. )[\s\S]+?(?=Valor dos serviços: )"
    local = re.findall(exp_endereco, nota_fiscal)
    for end in local:
        end.split()
        lista = local
    
    print(lista)
    return 0

if __name__ == "__main__":
    venda_principal()
    data_nascimento()
    endereco()