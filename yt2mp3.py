from bs4 import BeautifulSoup
from requests import get

def get_link(suffix):#get link for downloading file

        url = 'https://www.yt-download.org/api/button/mp3/'+suffix
        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        headers = {"user-agent" : USER_AGENT}
        resp = get(url, headers=headers)
        soup = BeautifulSoup(resp.content, "html.parser")
        link = soup.find_all('a')[0]['href']
        return link

def download(link,name):#download file from link

        print()
        print('[-] BE CALM, SMILE :) AND RELAX. YOUR SONG IS DOWNLOADING')
        r = get(link,allow_redirects=True)
        if open(name+'.mp3','wb').write(r.content):
            return 1
        return 0

def main():

    c = 0
    links=[]
    while 1:
        print('[-] ENTER LINK TO YOUTUBE VIDEO AND PRESS ENTER TO ADD TO QUEUE. ENTER "DONE" AND PRESS ENTER TO START DOWNLOADING')
        l=input()
        if l.upper() == "DONE":break
        links.append(l)
    print()
    for a in links:
        print('[-] DOWNLOADING ',c,' OUT OF ',len(links)-c)
        download(get_link(suffix=a.split('?v=')[-1]),str(c))

if __name__ == "__main__":main()