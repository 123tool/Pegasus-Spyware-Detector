import subprocess
import os
import re

def deteksi_spyware():
    # Daftar signature virus spyware yang dikenal
    spyware_signatures = ['pegasus', 'rat', 'spyware']

    # Perintah untuk mendapatkan daftar proses
    cmd = 'tasklist'
    try:
        result = subprocess.check_output(cmd, shell=True)
        de = result.decode()
        # Ambil daftar proses
        lines = de.splitlines()
        for line in lines[3:]:  # Awal dari daftar proses
            parts = line.split()
            if len(parts) > 1:
                proc_name = parts[0]
                proc_id = parts[1]
                # Periksa apakah proses mencurigakan
                for signature in spyware_signatures:
                    if re.search(signature, proc_name, re.IGNORECASE):
                        print(f"Proses mencurigakan ditemukan: {proc_name} ({proc_id})")
                        # Lakukan tindakan yang diperlukan
                        handle_spyware(proc_id)
    except subprocess.CalledProcessError as e:
        print(f"Error menjalankan perintah: {e}")

def handle_spyware(proc_id):
    # Perintah untuk mematikan proses
    kill = f'taskkill /F /PID {proc_id}'
    try:
        kill_task = subprocess.check_output(kill, shell=True)
        print(f"..........Terminating proses {proc_id} ......")
        print(kill_task.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error mematikan proses: {e}")

if __name__ == "__main__":
    print("Deteksi spyware...")
    deteksi_spyware()
