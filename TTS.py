import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import tkinter.messagebox as msgbox
import pyttsx3
import webbrowser

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rashida 文本→语音")
        self.geometry("450x270")
        self.resizable(0,0)
        self.engine = pyttsx3.init()
        self.file_path = tk.StringVar()
        self.mp3_path = tk.StringVar()
        self.mp3_path.set("output.mp3")
        self.init_ui()

    def init_ui(self):
        self.row1 = tk.LabelFrame(self, text="文本文件")
        self.txt_path = tk.Entry(self.row1, textvariable=self.file_path)
        self.txt_path.pack(side=tk.TOP, fill=tk.X, padx=(5,5),pady=0)

        self.row1_message = tk.Message(self.row1, text="上方输入TXT文件路径以 .txt 结尾或点击右边 选择文件 按钮", width=350)
        self.row1_message.pack(side=tk.LEFT, anchor='w', expand=True, fill=tk.X, padx=0, pady=0)

        self.btn_sel = tk.Button(self.row1, text="选择文件", command=self.select_file)
        self.btn_sel.pack(side=tk.RIGHT, padx=5, pady=5)
        self.row1.pack(fill=tk.X, padx=5, pady=5)
        
        self.btn_convert = tk.Button(self, text="TXT 转换为 MP3", command=self.convert_to_mp3)
        self.btn_convert.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.row2 = tk.LabelFrame(self, text="音频文件")
        self.mp3_path.set("OutPut.mp3")
        self.mp3_entry = tk.Entry(self.row2, textvariable=self.mp3_path)
        self.mp3_entry.pack(side=tk.TOP, fill=tk.X, expand=True, padx=(5,5),pady=0)

        self.row2_message = tk.Message(self.row2, text="上方输入MP3文件路径以 .mp3 结尾或点击右边 选择路径 按钮", width=350)
        self.row2_message.pack(side=tk.LEFT, anchor='w', expand=True, fill=tk.X, padx=0, pady=0)        

        self.mp3_sel_button = tk.Button(self.row2, text="选择路径", command=self.select_mp3_path)
        self.mp3_sel_button.pack(side=tk.RIGHT, pady=5, padx=5)
        self.row2.pack(fill=tk.X, padx=5, pady=5)

        self.btn_github = tk.Button(self, text="打开我的GitHub主页", command=self.open_github)
        self.btn_github.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

    def select_file(self):
        txt_file = filedialog.askopenfile(initialdir=".", title="选择文件", filetypes=(('文件文件', '*.txt'),('所有文件', '*.*')))
        if txt_file:
            self.file_path.set(txt_file.name)

    def select_mp3_path(self):
        mp3_path = filedialog.asksaveasfilename(initialdir=".", title="选择保存路径", filetypes=[("MP3 文件", "*.mp3"), ("所有文件", "*.*")])
        if mp3_path:
            self.mp3_path.set(mp3_path)

    def open_github(self):
        webbrowser.open("https://github.com/RashidaKAKU?tab=repositories") 
    
    def convert_to_mp3(self):
        filename = pathlib.Path(self.file_path.get())
        with open(filename, 'r', encoding='utf8') as f:
        	self.engine.save_to_file(f.read(), self.mp3_path.get())
        	self.engine.runAndWait()
        msgbox.showinfo("转换结果", "文件转换成功!")
        
if __name__ == "__main__":
    app = Application()
    app.mainloop()
