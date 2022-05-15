# требуется установить pandoc (например, с помощью Chocolatey: choco pandoc install)

import subprocess

def convert_to_pptx(md_template, pptx_output):
    subprocess.check_call(["pandoc","-o",pptx_output,md_template])