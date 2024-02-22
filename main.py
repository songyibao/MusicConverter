import tkinter as tk
from tkinter import filedialog
import subprocess

def select_input_dir():
    input_dir = filedialog.askdirectory()
    input_dir_entry.delete(0, tk.END)
    input_dir_entry.insert(0, input_dir)

def select_output_dir():
    output_dir = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, output_dir)

def convert_music():
    input_dir = input_dir_entry.get()
    output_dir = output_dir_entry.get()

    # 构建命令行参数列表
    command = ['/Users/songyibao/PycharmProjects/pythonProject/um']
    if output_dir:
        command.extend(['-o', output_dir])
    command.append(input_dir)

    # 调用二进制文件
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        # 输出执行结果
        print("Command executed:", ' '.join(command))
        print("Output:", result.stdout)
        print("Error:", result.stderr)
    except FileNotFoundError:
        print("Error: Executable not found.")
    except Exception as e:
        print("An error occurred:", e)

# 创建主窗口
root = tk.Tk()
root.title("Music Converter")

# 创建输入目录选择部件
input_dir_label = tk.Label(root, text="输入文件夹:")
input_dir_label.grid(row=0, column=0, padx=5, pady=5)

input_dir_entry = tk.Entry(root, width=50)
input_dir_entry.grid(row=0, column=1, padx=5, pady=5)

input_dir_button = tk.Button(root, text="浏览", command=select_input_dir)
input_dir_button.grid(row=0, column=2, padx=5, pady=5)

# 创建输出目录选择部件
output_dir_label = tk.Label(root, text="输出文件夹:")
output_dir_label.grid(row=1, column=0, padx=5, pady=5)

output_dir_entry = tk.Entry(root, width=50)
output_dir_entry.grid(row=1, column=1, padx=5, pady=5)

output_dir_button = tk.Button(root, text="浏览", command=select_output_dir)
output_dir_button.grid(row=1, column=2, padx=5, pady=5)

# 创建转换按钮
convert_button = tk.Button(root, text="开始转换", command=convert_music)
convert_button.grid(row=2, column=1, padx=5, pady=5)


# 运行主事件循环
root.mainloop()
