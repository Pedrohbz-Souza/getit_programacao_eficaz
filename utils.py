import json

def load_data(file_name):
    with open(f'static/data/{file_name}','r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def load_template(template_name):
    with open(f'static/templates/{template_name}', 'r', encoding='utf-8') as arquivo:
        return arquivo.read()
