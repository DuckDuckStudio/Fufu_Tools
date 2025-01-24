import os
import sys
import winreg as reg
import configparser

def get_version():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))), "config.ini"))
    return config.get('information', 'status_or_revision_number')

def register_protocol(protocol_name, application_path):
    key = f'Software\\Classes\\{protocol_name}'
    with reg.CreateKey(reg.HKEY_CURRENT_USER, key) as protocol_key:
        reg.SetValueEx(protocol_key, '', 0, reg.REG_SZ, f'URL:{protocol_name}')
        reg.SetValueEx(protocol_key, 'URL Protocol', 0, reg.REG_SZ, '')

        command_key = os.path.join(key, 'shell', 'open', 'command')
        with reg.CreateKey(reg.HKEY_CURRENT_USER, command_key) as cmd_key:
            reg.SetValue(cmd_key, '', reg.REG_SZ, f'"{application_path}" "%1"')
    
    print(f'[INFO] 协议 "{protocol_name}" 已注册。')

def remove_protocol(protocol_name):
    key = f'Software\\Classes\\{protocol_name}'
    try:
        reg.DeleteKey(reg.HKEY_CURRENT_USER, key)
        print(f'[INFO] 协议 "{protocol_name}" 已移除。')
    except FileNotFoundError:
        print(f'[WARN] 找不到协议 "{protocol_name}"。')
    except PermissionError:
        print(f'[WARN] 权限不足，请尝试手动移除注册表:\nHKEY_CURRENT_USER\\{key}')

def main():
    sorn = get_version()
    if sorn in ["code", "lite"]:
        app = "芙芙工具箱.pyw"
    elif sorn in ["exe", "pack"]:
        app = "芙芙工具箱.exe"
    else:
        print("[ERROR] 版本信息文件错误")
        return 1

    protocols = {
        'fft': os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))), app),
    }

    while True:
        action = input('? 您想注册还是移除协议 [register(r)/remove(d)]: ').strip().lower()
        if action in ['register', 'r', '注册', 'remove', 'd', '移除']:
            break
        print('[ERROR] 无效操作。请键入 "注册" 或 "移除"。')

    for protocol_name, application_path in protocols.items():
        if action in ['register', 'r', '注册']:
            register_protocol(protocol_name, application_path)
        elif action in ['remove', 'd', '移除']:
            # 这里的 d 指 del , 用于与前面的 r 区分
            remove_protocol(protocol_name)
    return 0

if __name__ == '__main__':
    sys.exit(main())
