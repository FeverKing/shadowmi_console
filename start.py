from color import Color
import os, time, re, datetime


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
        input("press enter to continue...")
    Color.pl('''
选择功能:

    1. 开启网卡监听模式(在WiFi渗透前请选择此)
    2. WiFi 渗透
    3. GPS 信息
    4. GPS 轨迹
    5. 隐秘隧道配置
    6. 被动信息收集模块{O}(暂未完成交互){W}
    7. 启动 / 重启管理后台{O}(暂未完成交互){W}
    8. 关闭 GPS 监控
    9. 开启 GPS 监控
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
    if select == "3":
        get_current_gps()
    if select == "4":
        get_gps()
    if select == "5":
        conf_tunnel()
    if select == "6":
        input("press enter to continue...")
        show_main_menu()
    if select == "7":
        input("press enter to continue...")
        show_main_menu()
    if select == "8":
        os.system("adb shell am force-stop com.tool.location")
        os.system("adb shell am force-stop com.chartcross.gpstest")
        Color.pl("{+}成功, 返回上级...")
        time.sleep(1.5)
        show_main_menu()
    if select == "9":
        os.system("adb shell am start -n com.tool.location/.MainActivity")
        time.sleep(3)
        os.system("adb shell am start com.chartcross.gpstest/.MainActivity")
        Color.pl("{+}成功, 返回上级...")
        time.sleep(1.5)
        show_main_menu()

def get_current_gps():
    opt = os.popen('adb shell su root -c "tail -n 1 /data/data/com.tool.location/cache/location.txt"').read()
    Color.pl("{+}获取最后一次 GPS 信息:\n\n%s" % (convert_gps_log(opt)))
    input("press enter to continue...")
    show_main_menu()

def get_gps():
    opt = os.popen('adb shell su root -c "cat /data/data/com.tool.location/cache/location.txt"').read()
    opt_arr = opt.split("\n")
    Color.pl("{+}获取 GPS 轨迹信息:\n\n")
    for o in opt_arr:
        Color.pl("{+}%s" % (convert_gps_log(o)))
    input("press enter to continue...")
    show_main_menu()


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
{W}当前隧道服务器地址: {G}%s
{W}当前隧道服务器密钥: {G}%s{W}
1. 修改隧道服务器信息
0. 返回上级
''' % (sp.read(), kp.read()))
    select = input("请选择[?]: ")
    if select == "0":
        show_main_menu()
    elif select == "1":
        sp = input("请输入隧道服务器地址: ")
        kp = input("输入隧道服务器地址密钥: ")
        os.system("echo -n %s > /root/tunnelserver" % (sp))
        os.system("echo -n %s > /root/tunnelkey" % (kp))
        Color.pl("{+}成功, 返回上级...")
        time.sleep(1.5)
        show_main_menu()
    else:
        input("press enter to continue...")
        show_main_menu()


def convert_gps_log(data):
    # 使用正则表达式匹配数据中的经度、纬度、国家、辖区和街道信息
    pattern = r'latitude=([\d\.]+),\s+longitude=([\d\.]+),\s+country=([^,]+),\s+locality=([^,]+),\s+street=(.*)$'
    match = re.search(pattern, data)
    if not match:
        return None

    # 提取匹配到的信息
    latitude = match.group(1)
    longitude = match.group(2)
    country = match.group(3)
    locality = match.group(4)
    street = match.group(5)

    # 将日期时间格式化为指定格式
    datetime_str = data[:14]
    datetime_obj = datetime.datetime.strptime(datetime_str, '%Y%m%d%H%M%S')
    datetime_formatted = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

    # 拼接转换后的信息
    result = f"{datetime_formatted} 经度: {longitude}, 纬度: {latitude}, 国家: {country}, 辖区: {locality}, 街道: {street}"
    return result

if __name__ == "__main__":
    os.system("hostname shadow-dev")
    os.popen("adb shell connect 127.0.0.1:2333")
    show_main_menu(initstart=True)