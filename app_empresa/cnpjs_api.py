#-*-coding:utf-8

import json
import requests

response = requests.get('https://www.receitaws.com.br/v1/cnpj/08513910000180')
json = response.json()
print json['fantasia'],'-',json['atividade_principal'][0]['text'], '-',json['municipio'],'-',json['cep'],'-', json['email'],'-', json['telefone'],'-', json['natureza_juridica']
print json['ultima_atualizacao'], '-', json['uf'], '-', json['status'], '-',json['capital_social']

"""

{
"atividade_principal": [
	{
	"text": "Reparação e manutenção de computadores e de equipamentos periféricos",
	"code": "95.11-8-00"
	}
],
"data_situacao": "02/04/2018",
"nome": "CARLOS ANDRE DANTAS DE LIMA 07140440409",
"uf": "AL",
"telefone": "(82) 9908-1114",
"email": "eucandre@gmail.com",
"qsa": [],
"situacao": "ATIVA",
"bairro": "Centro",
"logradouro": "AV Avenida dois de dezembro",
"numero": "776",
"cep": "57.442-000",
"municipio": "OLHO D'AGUA DAS FLORES",
"abertura": "02/04/2018",
"natureza_juridica": "213-5 - Empresário (Individual)",
"fantasia": "CARLOS LIMA DESENVOLVIMENTO LTDA",
"cnpj": "30.081.627/0001-85",
"ultima_atualizacao": "2018-04-28T12:03:14.941Z",
"status": "OK",
"tipo": "MATRIZ",
"complemento": "",
"efr": "",
"motivo_situacao": "",
"situacao_especial": "",
"data_situacao_especial": "",
"atividades_secundarias": [
{
"code": "00.00-0-00",
"text": "Não informada"
}
],
"capital_social": "1000.00",
"extra": {}
}

"""
