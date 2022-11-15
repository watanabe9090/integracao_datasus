import subprocess
import os
import ftplib
from pathlib import Path
import time

L_PATH=Path(__file__).parent.absolute()

R_SCRIPT_NAME='conv.R'
R_SCRIPT_PATH=(os.path.join(L_PATH, R_SCRIPT_NAME))

DBC_DIR_NAME='DBC'
DBC_DIR_PATH=(os.path.join(L_PATH, DBC_DIR_NAME))

CSV_DIR_NAME='CSV'
CSV_DIR_PATH=(os.path.join(L_PATH, CSV_DIR_NAME))



# Conexão com o FTP do DATASUS
FTP_HOST = 'ftp.datasus.gov.br'
FTP_PORT = 21
FTP_USERNAME = ''
FTP_PASSWORD = ''


def dbc2csv(input, output):
    try:
        commands = ["/usr/bin/Rscript","--vanilla", R_SCRIPT_PATH, input, output]
        subprocess.call(commands, shell=False)
        return True
    except:
        print(f"Erro no Rscript - ao converter arquivo: {input}")
        return False



def download_folder(ftp_location): 
    ftp = ftplib.FTP(timeout=30)
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login()


    ftp.cwd(ftp_location)
    ftp_dir = ftp.pwd()[1:]
    dbc_dir = os.path.join(DBC_DIR_PATH, ftp_dir)
    csv_dir = os.path.join(CSV_DIR_PATH, ftp_dir)

    if not os.path.exists(dbc_dir):
        os.makedirs(dbc_dir)
    if not os.path.exists(csv_dir):
        os.makedirs(csv_dir)

    files = ftp.nlst()
    size = len(files)
    for index, ftp_filename in enumerate(files):
        local_path = os.path.join(dbc_dir, ftp_filename)
        print(f"Download Nº:{index}/{size} - {ftp_filename}, Em: {local_path}")


        if not os.path.exists(local_path):
            with open(local_path, 'wb') as file:
                ftp.retrbinary(f"RETR {ftp_filename}", file.write)
        else:
            print(f"{local_path} já existe, pulando download...")


        csv_filename = Path(ftp_filename).stem+'.csv'
        csv_path = os.path.join(csv_dir, csv_filename)
        if not os.path.exists(csv_path):
            dbc2csv(local_path, csv_path)
            print(f"Conversão completa de: {local_path} para: {csv_path}")
        else: 
            print(f"CSV: {csv_path} já existe")


        time.sleep(3)

    ftp.quit()


FTP_PATH='/dissemin/publicos/SIHSUS/200801_/Dados'

download_folder(FTP_PATH)
