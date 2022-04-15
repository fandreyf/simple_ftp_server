from subprocess import PIPE, run

#run console cmd to show eth interfaces
def run_cmd(command='ip a'):
    return run(command,shell=True, stdout=PIPE).stdout.decode('utf-8')

#get start positions of eth interfaces and raw cmd stdout print
def get_ip_params():
    l = []
    cmd_stdout=run_cmd()
    for i in range(1, 10):
        if cmd_stdout.find(f'{i}: ') != -1:
            l.append(cmd_stdout.find(f'{i}: '))
    return l,cmd_stdout

#show number eth interfaces
def get_number_interfaces():
    return len(get_ip_params()[0])

#show ip adress one of eth interface
def get_ip(number_eth):
    l,out=get_ip_params()
    ip_raw=[]
    ip=[]
    for i in range(len(l)):
        try:
            ip_raw.append(out[l[i]:l[i+1]])
        except:
            ip_raw.append(out[l[i]:])
            break
    for i in range(len(ip_raw)):
        try:
            ip.append(ip_raw[i][ip_raw[i].find('inet ')+5:].split()[0].split('/')[0])
        except:
            ip.append(ip_raw[i][ip_raw[i].find('inet ') + 5:].split()[0])
    return ip[number_eth]