import requests

try:
    resposta = requests.get('https://www.google.com', timeout=5)
    if resposta.status_code == 200:
        print('✅ Conexão bem-sucedida! Internet funcionando.')
    else:
        print(f'⚠️ Conseguiu acessar, mas o site respondeu com código: {resposta.status_code}')
except requests.ConnectionError:
    print('❌ Sem conexão com a internet.')
except requests.Timeout:
    print('❌ A conexão demorou muito e expirou.')
