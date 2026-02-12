#!/usr/bin/python3
"""Toma credenciales de GitHub (usuario y token) y muestra el ID del usuario."""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    try:
        print(response.json().get("id"))
    except:
        print(None)