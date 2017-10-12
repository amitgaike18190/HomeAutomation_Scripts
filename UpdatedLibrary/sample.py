import webbrowser
import os

current = os.getcwd()
html_path = os.path.join(r'file://',current,'index.html')
ie_path= r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s"
#os.startfile(html_path)
webbrowser.get(ie_path).open(html_path)
 
