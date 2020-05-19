# -*- coding:utf-8 -*-
#python version 3.6.5
import subprocess
import os

file_index = 0

def generator(file, size="1920x1080", hz="11025", bitrate="64k"):
	fileName = "encode.bat"
	with open(fileName,"wt") as outFile:
		clearName = os.path.basename(file)
		#-y -i %1 -vcodec libvpx -quality good -cpu-used 5 -b:v 700k -maxrate 700k -bufsize 1000k -qmin 10 -qmax 42 -vf scale=trunc(oh*a/2)*2:480 -threads 4 -acodec libvorbis -f webm %1.webm
		# outFile.write("ffmpeg -i "+ file + " -b 1500k -vcodec libtheora -acodec libvorbis -ab 160000 -g 30 -s 640x360 "+ clearName+".ogv")
		outFile.write("ffmpeg -i "+ file + " -c:v libx264 -s "+size+" -ar " +hz+ " -b:a "+bitrate+" -crf 28 " + clearName +".flv")
		#outFile.write("ffmpeg -i "+ file + " -vcodec libvpx -quality good -cpu-used 5 -b:v 700k -maxrate 700k -bufsize 1000k -qmin 10 -qmax 42 -vf -threads 4 -acodec libvorbis -f webm "+ clearName+".mov")
		outFile.close()
	pass

def init(file_dir):
	fileList = []
	vaild_file_list = []
	for root, dirs, files in os.walk(file_dir):  
		# print("root:",root) #当前目录路径  
		# print("dirs:",dirs) #当前路径下所有子目录  
		fileList = files
	for file in fileList:
		if os.path.splitext(file)[1] == ".mp4":
			vaild_file_list.append(file)
			pass
	return vaild_file_list

def buildEncode():
	completeProcess = subprocess.run(["encode.bat"], stdout=subprocess.PIPE)
	if completeProcess.returncode is 0:
		os.remove("encode.bat")
		if len(file_list)>0:
			generator(file_list.pop())
			buildEncode()
		else:
			print("所有视频转码完成！")
	pass

if __name__ == '__main__':
	# completeProcess = subprocess.run(["encode.bat"], stdout=subprocess.PIPE)
	# print(completeProcess.returncode)
	file_list = init(os.getcwd())
	print(file_list)
	if len(file_list) > 0:
		generator(file_list.pop())
		buildEncode()
	

