#!/usr/bin/python3
import os
import argparse
from sys import exit

GREEN = "\033[0;32m"

msg = """
   \n* Copyright of Patan Musthakheem, 2021                         *
   Supports Checksum For SHA256, SHA1, MD5"""

parser = argparse.ArgumentParser(description=msg)
parser.add_argument("--hash", help="Hash To Compare With")
parser.add_argument("-a", help="Algorithm Of Hashing")
parser.add_argument("path", help="Path of The File")
args = parser.parse_args()
md5_len = 39
sha256_len = 71
sha1_len = 47
hash = args.hash
algo = args.a
path = args.path
if os.path.exists(path) != True:
    print(f"[-] Given File Not Found In Directory {path}")
    exit(12)
if hash is None and algo is None:
    md5 = os.popen(f"md5sum {path}" + "| awk \'{print $1}\'").read().replace("\n", "")
    sha256 = os.popen(f"sha256sum {path}" + "| awk \'{print $1}\'").read().replace("\n", "")
    sha1 = os.popen(f"sha1sum {path}" + "| awk \'{print $1}\'").read().replace("\n", "")
    print(f"MD5:{md5}")
    print(f"SHA256:{sha256}")
    print(f"SHA1:{sha1}")
    exit()

hashes_supported = ["md5", "sha1", "sha256"]
if algo in hashes_supported:
    pass
else:
    print("[-] Please Enter Correct Hashing Algorithm")
    exit()
command = algo + "sum " + path + "| awk \'{print $1}\'"
p = os.popen(command).read().replace("\n", "")
hash_returned = p
if hash_returned != hash:
    print(f"[-] Hashes Not Matched Please Re-Download The File")
    print(f"[-] Hash Given: {hash}")
    print(f"[-] File Hash: {hash_returned}")
    if len(hash) != len(hash_returned):
        print("[-] Wrong Hashing Algorithm Given")

else:
    print(GREEN, "OK")
