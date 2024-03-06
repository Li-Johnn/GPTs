import subprocess
import re

# 执行 conda list 命令，并捕获输出
result = subprocess.run(['conda', 'list'], capture_output=True, text=True)

# 解析输出，获取包名和版本号
packages = []
lines = result.stdout.split('\n')
for line in lines[2:]:
    if line.strip():  # 跳过空行
        package_info = line.split()
        package_name = package_info[0]
        package_version = package_info[1]
        packages.append(f"{package_name}=={package_version}")

# 将输出写入 requirements.txt 文件
with open('requirements.txt', 'w') as file:
    file.write('\n'.join(packages))
