from var2yolo import VOC2Yolov5
import threading
# 使用多綫程技術來避免處理GUI卡死的問題  **未完成
import ast
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import ttk

def run(class_num, voc_img_path, voc_xml_path,
        yolo_txt_save_path, yolo_img_save_path=None):
    # str --> dict
    class_num_dict = ast.literal_eval(class_num)
    VOC2Yolov5(
        class_num=class_num_dict,
        voc_img_path=voc_img_path,
        voc_xml_path=voc_xml_path,
        yolo_txt_save_path=yolo_txt_save_path,
        # yolo_img_save_path="/home/zhouhe/datasets/huiliantiao/images/train2017"
    )

def selectPath(key=0):
    path_ = askdirectory()
    if key==0:
        path0.set(path_)
    elif key==1:
        path1.set(path_)
    elif key==2:
        path2.set(path_)

root = Tk()  # 实例化 Tk()
path0 = StringVar()
path1 = StringVar()
path2 = StringVar()
default = StringVar()
default.set("{'touch': 0, 'gear': 1, 'note': 2, 'hold': 3, 'double': 4}")
frm = ttk.Frame(root, padding=10)  # 使用 root 创建其他小部件
root.title('PascalVOC 2 YOLO TOOL')
frm.grid()
ttk.Label(frm, text="PascalVOC 2 YOLO TOOL").grid(column=0, row=0)

ttk.Label(frm, text="voc_images_path:").grid(column=0, row=1)
ttk.Label(frm, text="voc_labels_path:").grid(column=0, row=2)
ttk.Label(frm, text="yolo_labels_out_path:").grid(column=0, row=3)
ttk.Label(frm, text="class_name:").grid(column=0, row=4)

ttk.Button(frm, text="select_dir", command=lambda: selectPath(0)).grid(column=2, row=1)
ttk.Button(frm, text="select_dir", command=lambda: selectPath(1)).grid(column=2, row=2)
ttk.Button(frm, text="select_dir", command=lambda: selectPath(2)).grid(column=2, row=3)


vocImgPath = ttk.Entry(frm, textvariable = path0, width=30)
vocImgPath.grid(column=1, row=1)
vocLabPath = ttk.Entry(frm, textvariable = path1, width=30)
vocLabPath.grid(column=1, row=2)
yoloLabOutPath = ttk.Entry(frm, textvariable = path2, width=30)
yoloLabOutPath.grid(column=1, row=3)
Labels = ttk.Entry(frm, width=30, textvariable = default)
Labels.grid(column=1, row=4)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=5)
ttk.Button(frm, text="Run", command=lambda: run(Labels.get(), vocImgPath.get(), vocLabPath.get(), yoloLabOutPath.get())).grid(column=1, row=5)

# 进入消息循环
try:
    root.mainloop()
except Exception as e:
    print(e)
    import traceback
    traceback.print_exc()
