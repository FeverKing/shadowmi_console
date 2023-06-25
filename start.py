from color import Color
import os, time


def show_main_menu(initstart=False):
    os.system("clear")

    Color.pl('''

{+}you are now using:
''')
    Color.pl('''
        __                   __                                      
        /\ \                 /\ \                                     
    ____\ \ \___      __     \_\ \    ___   __  __  __     __   _ __  
    /',__\\\ \  _ `\  /'__`\   /'_` \  / __`\/\ \/\ \/\ \  /'__`\/\`'__\\
    /\__, `\\\ \ \ \ \/\ \L\.\_/\ \L\ \/\ \L\ \ \ \_/ \_/ \/\  __/\ \ \/ 
    \/\____/ \ \_\ \_\ \__/.\_\ \___,_\ \____/\ \___x___/'\ \____\\\ \_\ 
    \/___/   \/_/\/_/\/__/\/_/\/__,_ /\/___/  \/__//__/   \/____/ \/_/    

    {R}desc: {W}口袋型WiFi攻击模块
    {B}vers: {W}v0.9.2+20230625-incompatible
    {C}feat: {W}WiFi pentesting, network scanning, encrypted tunnel, GPS tracking
    {O}note:{W} 你可以在调试模式随时使用命令 {G}startw {W}进入此菜单
    {G}===================================================================={W}
''')
    if initstart:
        input("press any key to continue...")
    Color.pl('''
选择功能:

    1. 开启网卡监听模式(在WiFi渗透前请选择此)
    2. WiFi 渗透
    3. GPS 信息
    4. GPS 轨迹
    5. 隐秘隧道配置
    6. 被动信息收集模块
    7. 启动 / 重启管理后台
    0. 进入调试模式
''')
    select = input("请选择[?]: ")
    if select == "0":
        Color.pl("\n{!}进入调试模式...\n")
        time.sleep(1.5)
        exit(0)
    if select == "1":
        start_wlan0mon()
    if select == "2":
        start_wificrack()
    if select == "5":
        conf_tunnel()

def start_wificrack():
    os.system("wificrack")
    Color.pl("{+}结束, 返回上级...")
    time.sleep(1.5)
    show_main_menu()

def start_wlan0mon():
    os.system("startmon")
    Color.pl("{+}成功, 返回上级...")
    time.sleep(1.5)
    show_main_menu()

def conf_tunnel():
    sp = open("/root/tunnelserver")
    kp = open("/root/tunnelkey")
    
    Color.pl('''
{W}当前隧道服务器地址: {G}%s{W}当前隧道服务器密钥: {G}%s{W}
1. 修改隧道服务器信息
0. 返回上级
''' % (sp.read(), kp.read()))
    select = input("请选择[?]: ")
    if select == "0":
        show_main_menu()
    if select == "1":
        sp = input("请输入隧道服务器地址: ")
        kp = input("输入隧道服务器地址密钥: ")
        os.system("echo -n %s > /root/tunnelserver" % (sp))
        os.system("echo -n %s > /root/tunnelkey" % (kp))
        Color.pl("{+}成功, 返回上级...")
        time.sleep(1.5)
        show_main_menu()

if __name__ == "__main__":
    show_main_menu(initstart=True)