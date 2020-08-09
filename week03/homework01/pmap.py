import argparse
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import ipaddress
import json
import os


class ArgsParser:
    def __init__(self):
        try:
            self.parser = argparse.ArgumentParser(description='IP 網段掃描工具.')
            self.parser.add_argument('-n', type=int, default='20', help='worker number (defualt=5) ')
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
            self.args.isValid = True


        except Exception as e:
            print(e)
            self.args.isValid = False
            self.parser.print_help()

    def _validate_args(self):
        if self._validate_ipv4_net(self.args.start_ip) is False:
            raise Exception('IP 地址不合法')

        if self._validate_ipv4_net(self.args.end_ip) is False:
            raise Exception('IP 地址不合法')

    def _validate_ipv4_net(self, network: str) -> bool:
        try:
            ipaddress.IPv4Network(network)
            return True
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError, ValueError) as e:
            return False


def scan_ping(target_ip):
    response = os.system('ping -c 1 -w 1' + ' ' + target_ip + " > nul 2>&1")
    if response == 0:
        return (target_ip, "alive")


def scan_tcp(target_ip, target_port):
    s = socket.socket()
    s.settimeout(0.1)

    if s.connect_ex((target_ip, target_port)) == 0:
        record = [target_ip, target_port, 'open']
    else:
        record = [target_ip, target_port, 'close']
    s.close()
    return record


def exec_task(args):
    # 检查IP段
    start_ip = args.start_ip
    end_ip = args.end_ip

    # 并发数量
    if args.n <= 0:
        raise RuntimeError("args.n", "并发数必须大于0! ")
    concurrent = args.n

    # 扫描类型
    task_type = args.f

    # 是否保存结果
    save_file = args.w

    # 是否打印耗时信息
    verbose = args.v

    # 初始化变量
    tasks = []
    results = []
    start_time = time.time()

    # 初始化线程池
    with ThreadPoolExecutor(max_workers=concurrent) as executor:
        start_ip = ipaddress.IPv4Address(start_ip)
        end_ip = ipaddress.IPv4Address(end_ip)
        if start_ip > end_ip:
            raise RuntimeError("起始IP必须小于结束IP! ")

        if task_type == 'tcp':
            for int_ip in range(int(start_ip), int(end_ip) + 1):
                str_ip = str(ipaddress.IPv4Address(int_ip))
                for port in range(1, 1024):
                    tasks.append(executor.submit(scan_tcp, str_ip, port))
        elif task_type == 'ping':
            for int_ip in range(int(start_ip), int(end_ip) + 1):
                str_ip = str(ipaddress.IPv4Address(int_ip))
                tasks.append(executor.submit(scan_ping, str_ip))

        for future in as_completed(tasks):
            if not future.result() is None:
                if task_type == 'tcp':
                    if future.result()[2] == 'open':
                        print(future.result())
                        results.append(future.result())
                elif task_type == 'ping':
                    print(future.result())
                    results.append(future.result())

        # 打印运行耗时
        if verbose:
            end_time = time.time()
            print("任务耗时(秒)：", end_time - start_time)

        # 保存结果
        if not save_file is None:
            with open(save_file, 'w') as f:
                json.dump(results, f)


if __name__ == '__main__':
    args = ArgsParser().args
    if args.isValid:
        exec_task(args)
