import os
import sys
import json
import subprocess

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

if not sys.argv[1]:
    print("[ERROR] 使用示例: python xxx.py <新版本号>")
    sys.exit(1)

# 获取参数
新版本号 = sys.argv[1]

# 新版本号不应以 v 开头
if 新版本号.startswith('v'):
    print("[ERROR] 新版本号不应以 v 开头")
    sys.exit(1)

print(f"[INFO] 新版本号: {新版本号}")

# 列出所有打开的且带有“待发布”标签的 Issue
issues = subprocess.check_output(["gh", "issue", "list", "--json", "url", "--label", "待发布", "--state", "open"]).decode("utf-8")
issues = json.loads(issues)
for issue in issues:
    print(f"[INFO] 正在处理 Issue: {issue['url']}")
    subprocess.run(["gh", "issue", "edit", issue["url"], "--remove-label", "待发布", "--add-label", "DEV-已完成"], check=True)
    print("    成功替换标签: 待发布 -> DEV-已完成")
    subprocess.run(["gh", "issue", "close", issue["url"], "--reason", "completed", "--comment", f"此议题的相关修改已在 [{新版本号}](https://github.com/DuckDuckStudio/Fufu_Tools/releases/tag/v{新版本号}) 中发布。"], check=True)
    print(f"    成功关闭 Issue: {issue['url']}")
    print(f"[INFO] Issue {issue['url']} 处理完成🎉")

issues = subprocess.check_output(["gh", "issue", "list", "--json", "url", "--label", "待发布", "--state", "closed"]).decode("utf-8")
issues = json.loads(issues)
for issue in issues:
    print(f"[INFO] 正在处理 Issue: {issue['url']}")
    subprocess.run(["gh", "issue", "edit", issue["url"], "--remove-label", "待发布", "--add-label", "DEV-已完成"], check=True)
    print("    成功替换标签: 待发布 -> DEV-已完成")
    subprocess.run(["gh", "issue", "comment", issue["url"], "--body", f"此议题的相关修改已在 [{新版本号}](https://github.com/DuckDuckStudio/Fufu_Tools/releases/tag/v{新版本号}) 中发布。"], check=True)
    print(f"    成功评论 Issue: {issue['url']}")
    print(f"[INFO] Issue {issue['url']} 处理完成🎉")


# 列出所有带有“待发布”标签的 Pull Request
pullrequests = subprocess.check_output(["gh", "pr", "list", "--json", "url", "--label", "待发布", "--state", "merged"]).decode("utf-8")
pullrequests = json.loads(pullrequests)
for pullrequest in pullrequests:
    print(f"[INFO] 正在处理 Pull Request: {pullrequest['url']}")
    subprocess.run(["gh", "pr", "edit", pullrequest["url"], "--remove-label", "待发布", "--add-label", "DEV-已完成"], check=True)
    print("    成功替换标签: 待发布 -> DEV-已完成")
    subprocess.run(["gh", "pr", "comment", pullrequest["url"], "--body", f"此拉取请求的相关修改已在 [{新版本号}](https://github.com/DuckDuckStudio/Fufu_Tools/releases/tag/v{新版本号}) 中发布。"], check=True)
    print(f"    成功关闭 Pull Request: {pullrequest['url']}")
    print(f"[INFO] Pull Request {pullrequest['url']} 处理完成🎉")

print("[INFO] 所有 Issue 和 Pull Request 处理完成🎉")
