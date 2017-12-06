import socket
import requests
import json
'''
Autorizar e autenicar no DJANGO ! ! !

request_text = """\r\n\
GET /api/v2/minhas-informacoes/meus-dados/ HTTP/1.1\r\n\
Host: suap.ifrn.edu.br\r\n\
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n\
Accept: application/json\r\n\
Accept-Language: en-US,en;q=0.5\r\n\
Accept-Encoding: gzip, deflate, br\r\n\
X-CSRFToken: V2VTgqqCiOGtb8M9NEIXJwvGAdHyFhbf7aIBTrdOEQsLZb71SwA26CpCfh2qgMTO\r\n\
Referer: https://suap.ifrn.edu.br/api/docs/\r\n\
Cookie: csrftoken=lScUKtnFkhlxItrrh7TrS5EavNYAoXfN5jBfAk7NYtBhu50uv4nhVxBnfCOplrAP; sessionid=rwehm7up54sunv6xhgi846a66wlj8ifr\r\n\
Connection: keep-alive\r\n\
\r\n\
"""
'''

header = {'Accept': 'application/json', 'X-CSRFToken':'lScUKtnFkhlxItrrh7TrS5EavNYAoXfN5jBfAk7NYtBhu50uv4nhVxBnfCOplrAP',
'Authorization': 'Basic MjAxNzIwMTQwNTAwMzk6QzBuY2xhdjMh'}
r = requests.get('https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/', headers=header)
aluno = r.json()

print(json.dumps(aluno, indent=4,))
