from bs4 import BeautifulSoup
import requests

url = 'https://nvd.nist.gov/vuln/detail/CVE-2021-3520'

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

descriptions = doc.find('p', {'data-testid': 'vuln-description'})
vector = doc.find('span', {'data-testid': 'vuln-cvss3-nist-vector'})
baseScore = doc.find('a', {'data-testid': 'vuln-cvss3-panel-score'})
hyperlinks = doc.find('table', {'data-testid': 'vuln-hyperlinks-table'})
links = hyperlinks.find_all('a')
for link in links:
    print(link.text.strip())

quickInfo = doc.find('div', {'class': 'bs-callout bs-callout-info'})
print(quickInfo.text.strip())
