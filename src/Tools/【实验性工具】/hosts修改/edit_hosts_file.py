import argparse

def add_host_entry(ip: str, hostname: str):
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "a") as file:
        file.write(f"{ip} {hostname}\n")

def remove_host_entry(target: str):
    try:
        with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "r") as file:
            lines = file.readlines()

        with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "w") as file:
            found = False
            for line in lines:
                if not line.startswith("#") and target not in line.split():
                    file.write(line)
                else:
                    found = True
            if not found:
                print("未找到指定的域名或 IP 地址")
    except PermissionError:
        print("权限不足，请尝试以管理员身份运行")

def list_host_entries():
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "r") as file:
        for line in file:
            if not line.startswith("#") and len(line.strip()) > 0:
                print(line.strip())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="编辑 hosts 文件")
    parser.add_argument("--add", nargs=2, metavar=("ip", "hostname"), help="添加新的域名映射")
    parser.add_argument("--remove", metavar="target", help="删除已有的映射")
    parser.add_argument("--list", action="store_true", help="列出已配置的域名映射")
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.error("请提供有效的参数")

    if args.add:
        ip, hostname = args.add
        add_host_entry(ip, hostname)
        print(f"已添加新的域名映射: {ip} {hostname}")

    if args.remove:
        target = args.remove
        remove_host_entry(target)

    if args.list:
        print("已配置的域名映射:")
        list_host_entries()
