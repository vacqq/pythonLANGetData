import os
from scapy.all import sniff, wrpcap, Raw, IP, TCP


def get_pcap(ifs, ip=None, size=100):
    ''' 获取指定 ifs(网卡), 指定数量size 的数据包;
        如果有指定ip，指定ip的包 '''
    filter = ""
    if ip:
        filter += "ip src %s" % ip
        dpkt = sniff(iface=ifs, filter=filter, count=size)
    else:
        dpkt = sniff(iface=ifs, count=size)
    # wrpcap("pc1.pcap", dpkt)  # 保存数据包到文件
    return dpkt


def get_ip_pcap(ifs, sender, size=100):
    ''' 获取指定 ifs(网卡), 指定发送方 sender(域名或ip) 的数据包
        size：(一次获取数据包的数量） '''
    print(sender)
    if 'www.' or 'http' in sender:
        v = os.popen('ping %s' % sender).read()
        if '请求找不到' in v:
            print("请求找不到此地址!")
            return 0
        ip = v.split()[8]
        print("准备接收IP为 %s 的数据包..." % ip)
    else:
        ip = sender
        print("准备接收IP为 %s 的数据包...!" % ip)
    # 输出报文数量
    count = 0
    while count < 30:
        d = get_pcap(ifs, ip=ip, size=size)
        for i in d:
            print(len(i))
            # try:
            #     if i[IP].src == ip:  # 发送方的IP为：ip  接收方的IP：i[IP].dst==ip
            #         print(i[Raw].load)
            # except:
            #     pass
        count += 1
        print("第" + count + "次")


def main():
    ifs = 'Realtek PCIe GBE Family Controller'  # 网卡
    ip = "www.baidu.com"  # ip地址，也可写域名，如：www.baidu.com
    get_ip_pcap(ifs, ip, size=1)  # 一次接收一个包


if __name__ == '__main__':
    main()
