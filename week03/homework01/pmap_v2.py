import argparse
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import ipaddress
import json
import os
from typing import Tuple


class ArgsParser:
    def __init__(self):
        try:
            self.parser = argparse.ArgumentParser(description='IP 網段掃描工具.')
            self.parser.add_argument('-n', type=int, default='5', help='worker number (defualt=5) ')
            self.parser.add_argument('-ip', required=True, help='ip address ')
            self.parser.add_argument('-f', choices=['ping', 'tcp'], default='ping',
                                     help='ping(defualt)|tcp (connection type)')
            self.parser.add_argument('-m', choices=['proc', 'thread'], default='thread', help='proc(defualt)|thread')
            self.parser.add_argument('-v', action='store_true', help='打印运行耗时')
            self.parser.add_argument('-w', help='扫描结果檔案名')
            self.args = self.parser.parse_args()

            # parse start,end ip
            ips = self.args.ip.split('-')
            self.args.start_ip, self.args.end_ip = ips[0], ips[0]
            if len(ips) == 2:
                self.args.end_ip = ips[1]

            self._validate_args()

        except Exception as e:
            print(e)
            self.parser.print_help()

    def _validate_args(self):
        if self._validate_ipv4_net(self.args.start_ip) is not True:
            raise Exception('xxxx')

        if self._validate_ipv4_net(self.args.end_ip) is not True:
            raise Exception('xxxx')


    def _validate_ipv4_net(network: str) -> bool:
        try:
            ipaddress.IPv4Network(network)
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError, ValueError) as e:
            return False
        else:
            return True


class IPScaner:
    def __init__(self, start_ip, end_ip, worker_number, scan_type, save_file, print_time):
        self.start_ip = start_ip
        self.end_ip = end_ip
        self.worker_number = worker_number
        self.scan_type = scan_type
        self.save_file = save_file
        self.print_time = print_time
        print(self.__dict__)

    def start(self):
        ip_list = self._create_ip_list()
        print(ip_list)

        # 初始化变量
        tasks = []
        results = []
        start_time = time.time()

        # 初始化线程池
        with ThreadPoolExecutor(max_workers=self.worker_number) as executor:
            if self.scan_type == 'tcp':
                for ip in self._create_ip_list():
                    for port in range(1, 1024):
                        tasks.append(executor.submit(self._scan_tcp, ip, port))
            elif self.scan_type == 'ping':
                for ip in self._create_ip_list():
                    tasks.append(executor.submit(self._scan_ping, ip))


            for future in as_completed(tasks):
                if not future.result() is None:
                    if self.scan_type == 'tcp':
                        if future.result()[2] == 'open':
                            print(future.result())
                            results.append(future.result())
                    elif self.scan_type == 'ping':
                        print(future.result())
                        results.append(future.result())

            # 打印运行耗时
            if self.print_time:
                end_time = time.time()
                print("任务耗时(秒)：", end_time - start_time)


            # # 保存结果
            # if not save_file is None:
            #     with open(save_file, 'w') as f:
            #         json.dump(results, f)


    def _create_ip_list(self):
        scan_ip_list = []

        ip_start = ipaddress.IPv4Address(self.start_ip)
        ip_end = ipaddress.IPv4Address(self.end_ip)
        for int_ip in range(int(ip_start), int(ip_end) + 1):
            scan_ip_list.append(str(ipaddress.IPv4Address(int_ip)))

        return scan_ip_list
        #
        # # 線程數量
        # work_number = args.n
        #
        # # 掃描類型
        # scan_type = args.f
        #

        #
        # print(scan_ip_list)

    def _scan_ping(self,target_ip):
        response = os.system('ping -c 1 -w 1' + ' ' + target_ip + " > nul 2>&1")
        if response == 0:
            return (target_ip, "alive")

    def _scan_tcp(self,target_ip, target_port):
        s = socket.socket()
        s.settimeout(0.1)

        if s.connect_ex((target_ip, target_port)) == 0:
            record = [target_ip, target_port, 'open']
        else:
            record = [target_ip, target_port, 'close']
        s.close()
        return record

if __name__ == '__main__':
    args = ArgsParser().args
    scaner = IPScaner(start_ip=args.start_ip,
                      end_ip=args.end_ip,
                      worker_number=args.n,
                      scan_type=args.f,
                      save_file=args.w,
                      print_time=args.v
                      )
    scaner.start()

    #
    # excuate_task(parser.args)

    # ips = parser.args.ip_range.split('-')
    # for ip in ips:
    #     print(validate_ipv4_net(ip)[0])
    #     # validate ip
    #
    # scan_ip_list = []
    # if (len(ips) == 1):
    #     scan_ip_list.append(ips[0])
    # else:
    #     xx = ipRange(ips[0],ips[1])
    #     print(xx)
    #     # ip_start = ipaddress.IPv4Address(ips[0])
    #     # ip_end = ipaddress.IPv4Address(ips[1])
    #     #
    #     # xx = ip_end - ip_start

#
#
# def validate_ipv4_net(network: str) -> Tuple[bool, str]:
#     """
#     Checks if string is a valid IPv4 network
#     :param network: string representation of IPv4 network
#     :return: tuple of (bool, str). (True, msg) if valid; (False, msg) if invalid
#     """
#     try:
#         ipaddress.IPv4Network(network)
#     except (ipaddress.AddressValueError, ipaddress.NetmaskValueError, ValueError) as e:
#         valid = False
#         msg = "Provided string is not a valid network: {}.".format(e)
#     else:
#         valid = True
#         msg = "String is a network."
#
#     return valid, msg
#
#
# def ipRange(start_ip, end_ip):
#     start = list(map(int, start_ip.split(".")))
#     end = list(map(int, end_ip.split(".")))
#     temp = start
#     ip_range = []
#
#     ip_range.append(start_ip)
#     while temp != end:
#         start[3] += 1
#         for i in (3, 2, 1):
#             if temp[i] == 256:
#                 temp[i] = 0
#                 temp[i - 1] += 1
#         ip_range.append(".".join(map(str, temp)))
#
#     return ip_range
