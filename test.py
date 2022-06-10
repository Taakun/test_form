# テストフォーム
import requests
 
url = "https://docs.google.com/forms/d/e/1FAIpQLSc4q18agBt8jp7gM5NbttEEsuU50cPCiUuiIPuiMdhjdAi7Ig/formResponse"
 
params = {
  'entry.946001934' : 'ruka',
  'entry.1703206049' : 'いいえ',
}
 
r = requests.get(url, params=params)
print(r.url)
print(r.status_code)