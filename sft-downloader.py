import ftplib
import os
import sys


ftp_host = 'ftp.datasus.gov.br';
ftp_port = 21
ftp_username = ''
ftp_password = ''

# Caminho padrão dos arquivos
SIHSUS_PATH='/dissemin/publicos/SIHSUS'
A2022 = '200801_/Dados'

# Tipos de Arquivo SIHSUS
TIPOS = ['ER','RD', 'RJ', 'SP']
ANOS = [1979,1980,1981,1982,1983,1984,1985,1986,
    1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,
    1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,
    2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,
    2017,2018,2019,2020,2021,2022]

ftp = ftplib.FTP(timeout=30)
ftp.connect(ftp_host, ftp_port)
ftp.login()


path = SIHSUS_PATH + '/' + A2022 + '/ERRO1812.dbc'
filename = 'ERRJ0808.dbc'

print(path)

with open(filename, 'wb') as file:
    ftp.retrbinary(f"RETR {path}",  file.write)

ftp.cwd(SIHSUS_PATH + '/' + A2022)
# files = ftp.dir()
# files = ftp.nlst()

# for f in files:
    # print(f)

print(ftp.pwd()[1:])

os.makedirs(ftp.pwd()[1:])

# def download_recursive(path, ftp):
#     ftp.cwd(path)
#     c_dir = ftp.pwd()[1:]
#     ftp_files = ftp.nlst()
#     if not os.path.exists(c_dir):
#         os.makedirs(c_dir)
    
#     for ftp_file in ftp_files:
#         c_file = os.path.join(c_dir, ftp_file)
#         with open(c_file, 'wb') as file:
#         ftp.retrbinary(f"RETR {ftp}",  open(file).write)

        


ftp.quit()

