# image_resize
This script creates copies of images from `input` directory with new sizes.  

#####Before usage
		pip install Pillow

#####Usage

Step 1. Put your images in the `input` directory  
Step 3. Set your sizes in 'sizes' file  
(separated by commas as in the example)  
Step 3. Run in console   
		python resize.py 

The script will create new directory `out` with subdirectories.  
In this subdirectories will be new images with new sizes.  

---------------------------

#####How to install Pillow on mac
http://pillow.readthedocs.io/en/3.2.x/installation.html#os-x-installation

or 
Follow these steps  

    xcode-select --install  
    su  
    export CFLAGS=-Qunused-arguments  
    export CPPFLAGS=-Qunused-arguments  
    pip install pillow  

http://stackoverflow.com/questions/21867277/installing-pillow-with-mac-os-x-mavericks-10-9-1



