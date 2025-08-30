
import clr,os,sys

os.system("pip install")
sci = os.path.dirname(__file__) 
if getattr(sys,"frozen", False):
    sci = os.path.dirname(sys.executable)  
        

clr.AddReference(sci+"\\Libs\\Music_Light_Class.dll")
clr.AddReference(sci+"\\Libs\\NAudio.dll")

