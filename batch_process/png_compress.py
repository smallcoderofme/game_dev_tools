import os
import subprocess

exec_path = "pngquant --quality=70-80 {}" 
# .format(file)
png_seq = []

def read(file_dir):
	for root, dirs, files in os.walk(file_dir):
		# print("root",root)
		# print("dirs",dirs)
		# print("files",files)
		for re in files:
			ft = os.path.splitext(re)[1]
			lines = ''
			re_pa = root[2:]
			if ft == '.png':
				if len(re_pa) == 0:
					lines = r''+re
				else: 
					lines = r''+re_pa+'/'+re
			if len(lines) > 0:
				png_seq.append((lines.replace('\\', '/'), re))
		pass
	print("png_seq:", png_seq)
	if len(png_seq)>0:
		compress(png_seq.pop())
		pass
	pass

def compress(png_file):
	command = exec_path.format(png_file[0])
	print('command:', command)
	bat_file = "encode.bat"
	with open(bat_file,"wt") as cmd_file:
		cmd_file.write(command)
		cmd_file.close()
	completeProcess = subprocess.run([bat_file], stdout=subprocess.PIPE, shell=True)
	if completeProcess.returncode == 0:
		print('compress complete of {}.'.format(png_file[0]))
		if len(png_seq)>0:
			compress(png_seq.pop())
		else:
			os.remove(bat_file)
	pass


# replace_source = True
read('.')

# os.rename('chongzhuchongzhu.png', 'chong.png')