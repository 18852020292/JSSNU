#-*-coding:gb2312-*-
import requests
from ping3 import ping
import socket
import sys
import os
import win32api
import win32con

#�ж�����״̬
def is_connect():
    
    #�ж��Ƿ�ʹ��У԰��
    if ping("192.168.67.1",src_addr=None):
        print("�Ѿ�ʹ��У԰��")

        #�ж��Ƿ���֤У԰��
        if ping("www.baidu.com",src_addr=None) == None:
            print("������֤У԰��")
            return False
        else:
            print("�Ѿ�������У԰���ˣ���ע�������ԡ�")

            #�ж��û��Ƿ�ѡ��ע��
            if input("�����������ʼע��,ע�����������򣬰�0��ע��")!='0':
                open_url()
                return True
            else:
                return True
    else:
        print("��ʹ�õĲ���У԰��Ŷ��")
        return True

#��ע����ַ
def open_url():
    os.system('"C:/Program Files/Internet Explorer/iexplore.exe" http://192.168.67.1/')

#��ȡip��ַ
def get_host_ip():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip
    
#��ȡ�ļ�����·��
def path(config_name):
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(os.path.abspath(__file__))
    Path = os.path.join(application_path, config_name)
    return Path

#��ȡ�û���Ϣ
def message():
    #�ж��ļ��Ƿ����
    user = ""
    password = ""
    set = ""
    #��ȡ�ļ�,û���򴴽�
    if os.path.exists(path('user.txt')):
        with open(path('user.txt'),'r') as f:
            print('��ȡ�û���Ϣ')
            user = f.readline()
            password = f.readline()
            set = f.readline()
            
    if user == '' or password == '' or set == '':
        print('�û���Ϣ�����ڣ��������û���Ϣ')
        print("��������Ϣ")
        #�����û���Ϣ
        while user == '':
            user = input("�������û�����")
        while password == '':
            password = input("���������룺")
        while set == '':
            set = input("�ƶ�cmcc������njxy,���Ӧ���룺")
        
        #����Ϣ���浽�ļ�
        with open(path('user.txt'),'w') as f:
            f.write(user)
            f.write('\n')
            f.write(password)
            f.write('\n')
            f.write(set)
            f.write('\n')
    ip = get_host_ip()
    #strip()ȥ���ַ�����β�Ŀո�
    return user.strip(),password.strip(),set.strip(),ip


#���ÿ���������
def set_start():
    name = 'JSSUN'  # Ҫ��ӵ���ֵ����
    # ע�������
    KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
    # �쳣����
    try:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,  KeyName, 0,  win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path("JSSNU.exe"))
        win32api.RegCloseKey(key)
    except:
        print('���ʧ��')
    print('��ӳɹ���')

#��������
def post(user,password,set,ip):

    url = 'http://192.168.67.1:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account={}@{}&user_password={}&wlan_user_ip={}&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.2&v=3842'.format(user,set,password,ip)
    header = {"Accept": "*/*",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Connection": "keep-alive",
                "Referer": "http://192.168.67.1/",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30"
    }
    data = {}
    reponce = requests.post(url,data=data,headers=header).status_code

    #�ж��Ƿ��¼�ɹ�
    if reponce == 200:
        print('���ӳɹ�')
    else:
        print('����ʧ��')

#������
def main():
    #���������
    set_start()

    #�ж�����
    if is_connect():
       return

    #��ȡ��Ϣ
    user,password,set,ip= message()

    #��������
    post(user, password, set, ip)
   
    
if __name__ == '__main__':
    main()
