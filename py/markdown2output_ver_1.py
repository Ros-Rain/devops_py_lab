import subprocess

def convert_to_pptx(md_file, pptx_file):
    subprocess.check_call(["pandoc","-o",pptx_file,md_file]) 
    pass
