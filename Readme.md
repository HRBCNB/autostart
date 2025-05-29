# 使用方法

## 一、配置 `config.txt` 文件

`config.txt` 文件格式如下：

- **第一行**：`BetterGI.exe` 的完整安装路径  
- **后续每一行**：一次鼠标点击位置，格式为 `x,y`，分别为横纵坐标

### 步骤说明：

1. **找到 BetterGI 的安装目录**  
   右键快捷方式 → 打开文件所在位置  
   ![](https://gitee.com/hrbcnb/typora_pic/raw/master/img/20250529110111272.png)

2. **复制绝对路径**  
   ![](https://gitee.com/hrbcnb/typora_pic/raw/master/img/20250529110130326.png)

3. **打开 `config.txt` 文件**  
   将复制的路径粘贴在第一行，并添加 `\BetterGI.exe`，例如：

   ```
   D:\Program Files\BetterGI\BetterGI.exe
   ```

4. **以管理员身份运行 `mouse_position_recorder`**  
   右键 → 以管理员身份运行  
   > ⚠ 如果不是管理员身份运行，当焦点不在终端时将无法获取坐标

   ![](https://gitee.com/hrbcnb/typora_pic/raw/master/img/20250529110150733.png)

5. **启动 BetterGI**  
   若弹出“是否允许该程序更改你的设备”，直接点击“是”，**该点击不需要记录坐标**

6. **逐一记录点击坐标**  
   打开 BetterGI 后，依次记录每一个有效点击位置  
   
   > （获取的坐标点有可能会有没有用的，注意观察有效点击对应的坐标）
   
7. **最终配置示例**  
   ![](https://gitee.com/hrbcnb/typora_pic/raw/master/img/20250529110219701.png)

---

## 二、配置 Windows 任务计划程序

1. 打开 **任务计划程序**  
   在任务栏搜索 “任务计划程序” 并打开  
   ![](https://gitee.com/hrbcnb/typora_pic/raw/master/img/20250529110614926.png)

> 以下内容参考自：[Windows 设置定时执行脚本 - 博客园](https://www.cnblogs.com/sui776265233/p/13602893.html)

### 2. 创建基本任务

![step2](https://gitee.com/hrbcnb/typora_pic/raw/master/img/1364097-20200902170831028-680892963.png)

### 3. 命名任务并添加描述

![step3](https://gitee.com/hrbcnb/typora_pic/raw/master/img/1364097-20200902170920930-839321190.png)

### 4. 设置触发器（推荐选择“每天”）

### ![](https://gitee.com/hrbcnb/typora_pic/raw/master/img/20250529110704408.png)

### 5. 设置执行时间

![](https://gitee.com/hrbcnb/typora_pic/raw/master/img/20250529110725559.png)



### 6. 设置启动程序

![step6](https://gitee.com/hrbcnb/typora_pic/raw/master/img/1364097-20200902171201306-1070159278.png)

- 在弹出的窗口中，**程序选择 `auto_start.exe`**
- `config.txt` 要和 `auto_start.exe` 在 **同一目录下**

  ![](https://gitee.com/hrbcnb/typora_pic/raw/master/img/20250529110810803.png)

### 7. 查看并确认任务已创建成功

![step7](https://gitee.com/hrbcnb/typora_pic/raw/master/img/1364097-20200902171403343-216867839.png)

### 8. 设置最高权限启动

右键你刚刚设置好的任务，点击“**属性**”

![](https://gitee.com/hrbcnb/typora_pic/raw/master/img/20250529110843620.png)

在打开的属性窗口中，**勾选“使用最高权限运行”**，这样在执行 BetterGI 时就不会出现系统弹窗提示

![](https://gitee.com/hrbcnb/typora_pic/raw/master/img/20250529110854296.png)

## 三、总结

至此，配置完成，Windows 可以在每天特定的时间执行 BetterGI 的自动任务了。
