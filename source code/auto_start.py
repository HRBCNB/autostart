"""
自动启动工具 - AutoStart Tool
=========================

这个工具能做什么？(你能干什么？)
- 🖥️ 桌面管理：自动最小化窗口，显示桌面
- 🔊 音频控制：智能静音扬声器
- ⚙️ 进程管理：安全关闭相关程序避免冲突
- 🎮 游戏自动化：自动启动BetterGI并执行预设任务
- ⏰ 定时执行：支持Windows任务计划程序

支持的任务类型：
- 📅 每日任务自动化
- 🌾 自动锄地(资源收集)
- 🎯 其他可配置的BetterGI任务

使用方法：
1. 配置 config.txt 文件(设置BetterGI路径和点击坐标)
2. 设置Windows任务计划程序定时执行
3. 享受全自动的游戏任务执行

作者：HRBCNB
用途：原神BetterGI自动化工具
"""

import subprocess
from time import sleep
import pyautogui
import psutil
import os
import sys
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import win32com.client
import time

def show_desktop():
    """
    最小化所有窗口，显示桌面
    """
    shell = win32com.client.Dispatch("Shell.Application")
    shell.MinimizeAll()

def mute_default_speaker(mute=True):
    """
    静音或取消静音默认扬声器
    :param mute: True 静音，False 取消静音
    """
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(1 if mute else 0, None)


def find_and_kill_process(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # 模糊匹配进程名（不区分大小写）
            if process_name.lower() in proc.info['name'].lower():
                print(f"正在终止进程: {proc.info['name']} (PID: {proc.info['pid']})")
                p = psutil.Process(proc.info['pid'])
                p.terminate()  # 尝试优雅终止
                p.wait(timeout=3)  # 等待3秒确认结束
        except psutil.NoSuchProcess:
            continue
        except psutil.AccessDenied:
            print(
                f"权限不足，无法终止进程: {proc.info['name']} (PID: {proc.info['pid']})")
        except Exception as e:
            print(f"终止进程时发生错误: {e}")


def read_config(file_path):
    coordinates = []
    exe_path = ''
    with open(file_path, 'r', encoding='utf-8') as file:
        # 读取第一行作为exe路径
        exe_path = file.readline().strip()
        # 读取剩余部分作为坐标
        for line in file:
            if line.strip():  # 跳过空行
                if line.strip().startswith('#'):  # 跳过注释
                    continue
                x, y = map(int, line.strip().split(','))
                coordinates.append((x, y))
    return exe_path, coordinates


def click_coordinates(coordinates):
    """
    执行自动化鼠标点击序列
    这个函数是自动化的核心 - 它能根据预设坐标自动操作BetterGI界面
    """
    print(f"📍 开始执行 {len(coordinates)} 个点击操作:")
    for i, coord in enumerate(coordinates, 1):
        x, y = coord
        print(f"🖱️ [{i}/{len(coordinates)}] 点击坐标: ({x}, {y})")
        pyautogui.moveTo(x, y, duration=0.5)  # 移动到指定位置，duration为移动时间
        pyautogui.click()
        sleep(1)  # 等待界面响应
    print("✅ 所有点击操作执行完成！")


if __name__ == "__main__":
    print("=" * 50)
    print("🎮 自动启动工具启动中...")
    print("🎯 功能：原神BetterGI自动化执行")
    print("=" * 50)
    
    # 第一步：桌面管理 - 显示桌面
    print("📋 [1/6] 正在最小化所有窗口...")
    time.sleep(1)  # 可以延迟1秒，看效果
    show_desktop()
    print("✅ 已显示桌面！")

    # 第二步：音频控制 - 静音
    print("🔇 [2/6] 正在静音扬声器...")
    mute_default_speaker(True)
    print("✅ 扬声器已静音！")

    # 第三步：进程管理 - 关闭相关程序避免冲突
    print("⚙️ [3/6] 正在清理相关进程...")
    print('🔸 尝试关闭微星小飞机进程')
    find_and_kill_process('MSIAfterburner')

    print('🔸 尝试关闭原神与BetterGI进程')
    find_and_kill_process('yuanshen')
    find_and_kill_process('bettergi')

    print('🔸 尝试关闭Snipaste截图程序')
    find_and_kill_process('Snipaste')
    print("✅ 进程清理完成！")

    # 第四步：配置读取
    print("📁 [4/6] 正在读取配置文件...")
    # 获取当前脚本或exe文件所在目录，保证能正确读取config.txt
    base_dir = os.path.dirname(sys.executable if getattr(
        sys, 'frozen', False) else __file__)
    config_path = os.path.join(base_dir, "config.txt")

    # 读取配置文件，获取要打开的exe路径和坐标列表
    exe_path, coords = read_config(config_path)
    print(f"✅ 配置加载完成！任务坐标数量: {len(coords)}")

    # 第五步：启动BetterGI
    print("🚀 [5/6] 正在启动BetterGI...")
    print(f"📂 启动路径: {exe_path}")
    process = subprocess.Popen(exe_path)

    # 等待几秒以确保应用程序已完全启动，这里设置为5秒，可以根据实际情况调整
    print("⏳ 等待BetterGI完全启动中...")
    sleep(5)
    print("✅ BetterGI启动完成！")

    # 第六步：执行自动化点击
    print("🖱️ [6/6] 开始执行自动化点击序列...")
    click_coordinates(coords)
    
    print("=" * 50)
    print("🎉 自动化任务执行完成！")
    print("🎮 BetterGI将继续执行预设任务")
    print("=" * 50)

    #pyinstaller --onefile auto_start.py

