import subprocess

raw_files_dir = './'
raw_filename = 'DOSC2019.dbc'

def dbc2csv(raw_filename):
    dbc2csv_path = "./dbc2csv.R " + raw_files_dir + " " + "./csv" + " " + raw_filename

    try:
        r_script_path = subprocess.getstatusoutput('dbc2csv.R')[1]
        subprocess.call("./" + " --vanilla " + dbc2csv_path, shell=True)
        return True
    except:
        print("(Rscript) Error converting file: " + raw_filename)

    return False