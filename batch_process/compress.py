# https://github.com/kornelski/pngquant
# https://github.com/meowtec/Imagine

import subprocess
import os
# from PIL import Image                   
file_list = []

file_path = "./"
image_format = ".png"
quality = "50%"

def init(file_dir):
	fileList = []
	vaild_file_list = []
	for root, dirs, files in os.walk(file_dir):  
		# print("root:",root) #当前目录路径  
		# print("dirs:",dirs) #当前路径下所有子目录  
		# fileList += files
		for name in files:
			if os.path.splitext(name)[1] == image_format:
				fileList.append(os.path.join(root, name))
	# print('all file:', fileList)
	return fileList

def buildEncode(file):
	# img = Image.open(file); 
	# command = "magick convert -resize {}x{} -depth 8 -strip -quality {} {} {}".format(img.size[0], img.size[1], quality, file, file)
	command = "pngquant --quality=50-60 {}".format(file)
	print("command:", command)
	fileName = "encode.bat"
	with open(fileName,"wt") as outFile:
		outFile.write(command)
		outFile.close()
	completeProcess = subprocess.run([fileName], stdout=subprocess.PIPE, shell=True)
	if completeProcess.returncode is 0:
		# print("----------------- over!")
		if len(file_list)>0:
			buildEncode(file_list.pop())
		else:
			os.remove(fileName)
		# else:
		# 	print("tasks complete！")
	pass

if __name__ == '__main__':
	# completeProcess = subprocess.run(["encode.bat"], stdout=subprocess.PIPE)
	# print(completeProcess.returncode)
	file_list = init(file_path)
	print(file_list)
	# generator(file_list.pop())
	if len(file_list) > 0:
		# generator(file_list.pop())
		buildEncode(file_list.pop())