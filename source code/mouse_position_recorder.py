"""
鼠标位置记录器 - Mouse Position Recorder
========================================

这个工具能做什么？
- 🖱️ 实时记录鼠标点击的坐标位置
- 🎯 帮助配置auto_start.py所需的点击序列
- 🧹 支持F5快速清屏功能
- ⌨️ 使用Ctrl+C安全退出

使用方法：
1. 以管理员身份运行此脚本
2. 在需要记录的位置点击鼠标
3. 复制输出的坐标到config.txt文件
4. 按F5清空屏幕，按Ctrl+C退出

注意：必须以管理员身份运行，否则当焦点不在终端时无法获取坐标
"""

import os
from pynput import mouse, keyboard


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def on_click(x, y, button, pressed):
    if pressed:
        print(f"{x}, {y}")


def on_press(key):
    # 按 F5 清屏
    if key == keyboard.Key.f5:
        clear_console()
        # print("控制台已清空")


if __name__ == "__main__":
    print("=" * 60)
    print("🖱️ 鼠标位置记录器 - 为自动化配置收集坐标")
    print("=" * 60)
    print("📋 使用说明:")
    print("  • 点击鼠标记录坐标位置")
    print("  • 按 F5 清空屏幕") 
    print("  • 按 Ctrl+C 退出程序")
    print("=" * 60)
    print("⚠️ 重要：请确保以管理员身份运行此程序！")
    print("📍 开始记录坐标位置...")
    print()

    keyboard_listener = keyboard.Listener(on_press=on_press)
    keyboard_listener.start()

    with mouse.Listener(on_click=on_click) as mouse_listener:
        mouse_listener.join()

    keyboard_listener.join()
