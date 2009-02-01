import os
def pre_configure(options, buildout):
    """Custom pre-make hook for building libjpeg."""
    os.system("sh autogen.sh")

