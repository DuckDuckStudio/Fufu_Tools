import hashlib
import os

def calculate_hash(file_path, algorithms):
    if not os.path.exists(file_path):
        print("[ERROR]文件不存在。")
        return

    try:
        with open(file_path, "rb") as file:
            data = file.read()
            hash_values = {}
            for algorithm in algorithms:
                if algorithm == "md5":
                    hash_values["MD5"] = hashlib.md5(data).hexdigest()
                elif algorithm == "sha1":
                    hash_values["SHA-1"] = hashlib.sha1(data).hexdigest()
                elif algorithm == "sha256":
                    hash_values["SHA-256"] = hashlib.sha256(data).hexdigest()
                elif algorithm == "sha512":
                    hash_values["SHA-512"] = hashlib.sha512(data).hexdigest()
                elif algorithm == "blake2b":
                    hash_values["Blake2b"] = hashlib.blake2b(data).hexdigest()
                elif algorithm == "blake2s":
                    hash_values["Blake2s"] = hashlib.blake2s(data).hexdigest()
                else:
                    print(f"[ERROR]不支持的算法 '{algorithm}'")
            return hash_values
    except Exception as e:
        print(f"[ERROR] {e}")

def main():
    file_path = input("请输入文件路径：").strip('"')
    algorithms = ["md5", "sha1", "sha256", "sha512", "blake2b", "blake2s"]
    hash_values = calculate_hash(file_path, algorithms)
    if hash_values:
        print("哈希值:")
        for algorithm, value in hash_values.items():
            print(f"{algorithm}: {value}")

if __name__ == "__main__":
    main()

input("按Enter键继续...")