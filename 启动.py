import http.server
import socketserver
import webbrowser
import os
import sys
import threading

# 获取exe所在目录
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PORT = 18080
os.chdir(BASE_DIR)

handler = http.server.SimpleHTTPRequestHandler

class QuietHandler(handler):
    def log_message(self, format, *args):
        pass  # 静默日志

with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
    url = f"http://localhost:{PORT}/luoyang-ligong-assistant.html"
    
    def open_browser():
        webbrowser.open(url)
    
    threading.Timer(1.5, open_browser).start()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()
