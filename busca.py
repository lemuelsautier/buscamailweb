import requests
from bs4 import BeautifulSoup
import re

def find_emails(url):
  """
  Função para encontrar e-mails em uma página da web.

  Args:
    url: URL da página a ser analisada.

  Returns:
    Uma lista de e-mails encontrados.
  """

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for error HTTP status codes

    soup = BeautifulSoup(response.text, 'html.parser')

    # Use uma expressão regular para encontrar padrões de e-mail
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_regex, soup.text)

    return emails
  except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar a URL {url}: {e}")
    return []

# Lista de URLs para analisar
urls = [
"https://www.peeringdb.com/net/7232",
"https://www.peeringdb.com/net/29793",
"https://www.peeringdb.com/net/33332",
"https://www.peeringdb.com/net/11427"
  # Adicione mais URLs aqui
]

# Loop para analisar cada URL
for url in urls:
  emails = find_emails(url)
  if emails:
    print(f"E-mails encontrados em {url}:")
    for email in emails:
      print(email)
