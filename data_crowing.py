headers = {'User-Agent' : 'Mozilla/5.0'}
url = 'https://www.tripadvisor.co.kr/Attractions-g789433-Activities-Wonju_Gangwon_do.html'
res = requests.get(url, header = headers)
print(res.status_code)
