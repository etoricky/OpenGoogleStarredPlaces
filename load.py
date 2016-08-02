import os, datetime, webbrowser, time, psutil
from bs4 import BeautifulSoup

class Runner:
    def __init__(self):
        pth = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(pth))
        self.chrome = webbrowser.get('chrome')
        
    def readHtm(self, htm):
        data = []
        with open(htm, 'r', encoding='utf8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            for A in soup.find_all('a'):
                try:
                    href = A.get('href') if A.has_attr('href') else ''
                    add_date = A.get('add_date') if A.has_attr('add_date') else ''
                    if href.startswith('http://maps.google.com'):
                        t = (add_date, href)
                        x = print(t)
                        data.append(t)
                except:
                    pass
        return sorted(data, key=lambda t:t[0])
        
    def open(self, url):
        print ('opening', url)
        self.chrome.open_new_tab(url)
            
    def IsChromeRunning(self, process_name):
        for p in psutil.process_iter():
            try:
                if p.name() == process_name:
                    return True
            except psutil.Error:
                pass
        return False

    def run(self):
        urls = self.readHtm('GoogleBookmarks-ricky0415.html')
        print ('urls', len(urls))
        n = 10
        groups = [urls[i:i+n] for i in range(0, len(urls), n)]
        print ('groups', len(groups))
        for group in groups:
            print (len(group))
            for t in group:
                print (t[0])
                if t[0]>'1444910851399001':
                    self.open(t[1])
                    time.sleep(3)
            while self.IsChromeRunning('chrome.exe'):
                time.sleep(1)
        
if __name__ == '__main__':
    s = Runner()
    s.run()
    #s.open('http://maps.google.com/?cid=9705591681612170132')
    #while True:
    #    print (s.IsChromeRunning('chrome.exe'))