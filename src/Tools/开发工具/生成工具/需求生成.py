import os
import ast
import argparse
import sys
import subprocess
import warnings
from colorama import init, Fore

init(autoreset=True)

def extract_libraries(file_path):
    libraries = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("ignore")
                tree = ast.parse(file.read(), filename=file_path)
                for warning in w:
                    if not str(warning.filename).startswith(os.path.abspath(__file__)):
                        warnings.warn_explicit(warning.message, warning.category, warning.filename, warning.lineno)
    except SyntaxError as e:
        print(f"{Fore.RED}✕{Fore.RESET} 解析文件 {Fore.BLUE}{file_path}{Fore.RESET} 时出现错误: {Fore.RED}{e}{Fore.RESET}")
        return libraries
    except UnicodeDecodeError:
        print(f"{Fore.RED}✕{Fore.RESET} 文件 {Fore.BLUE}{file_path}{Fore.RESET} 包含非 UTF-8 编码字符")
        return libraries

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                libraries.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module is not None:
                libraries.add(node.module)
    return libraries

def get_installed_libraries(python_exec):
    try:
        result = subprocess.run([python_exec, "-m", "pip", "freeze"], capture_output=True, text=True)
        installed_libraries = set(result.stdout.strip().split('\n'))
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}✕{Fore.RESET} 无法获取到已安装的库。")
        sys.exit(1)
    return installed_libraries

def generate_requirements(directory_path, output_path, python_exec=None):
    existing_libraries = set()
    if os.path.exists(output_path):
        with open(output_path, "r") as req_file:
            existing_libraries = set(req_file.read().splitlines())

    new_libraries = set()
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(('.py', '.pyw')):
                file_path = os.path.join(root, file)
                libraries = extract_libraries(file_path)
                new_libraries.update(libraries)

    if python_exec:
        installed_libraries = get_installed_libraries(python_exec)
        new_libraries -= installed_libraries

    new_libraries -= existing_libraries

    with open(output_path, "a") as req_file:
        for library in new_libraries:
            req_file.write(library + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="根据目录中的Python文件生成requirements.txt文件。")
    parser.add_argument("--dir", type=str, required=True, help="包含Python文件的目录路径。")
    parser.add_argument("--output", type=str, required=False, default="requirements.txt", help="requirements.txt文件的输出路径（完整路径）。")
    parser.add_argument("--env", type=str, required=False, help="指定已有环境中的Python解释器，仅列出环境中还未安装的库。")
    args = parser.parse_args()

    directory_path = args.dir
    output_path = args.output

    if not output_path.endswith('.txt'):
        if output_path.endswith('\\'):
            output_path += 'requirements.txt'
        else:
            output_path += '\\requirements.txt'

    python_exec = args.env

    generate_requirements(directory_path, output_path, python_exec)
    print(f"{Fore.GREEN}✓{Fore.RESET} 已将 requirements.txt 保存至 {Fore.BLUE}{output_path}{Fore.BLUE}")
