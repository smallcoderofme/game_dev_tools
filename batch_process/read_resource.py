import os
import sys

def file(file_dir):
	f = open('resource.txt', 'w')
	for root, dirs, files in os.walk(file_dir):
		# print("root",root)
		# print("dirs",dirs)
		# print("files",files)
		for re in files:
			ft = os.path.splitext(re)[1]
			lines = ''
			re_pa = root[2:]
			if ft == '.png' or ft == '.jpg':
				if len(re_pa) == 0:
					lines = r'{ type:Loader.IMAGE, url:"'+re+'"},'+"\n"
				else: 
					lines = r'{ type:Loader.IMAGE, url:"'+re_pa+'/'+re+'"},'+"\n"
			elif ft == '.sk':
				if len(re_pa) == 0:
					lines = r'{ type:Loader.BUFFER,url:"'+re+'"},'+"\n"
				else: 
					lines = r'{ type:Loader.BUFFER,url:"'+re_pa+'/'+re+'"},'+"\n"
			elif ft == '.atlas':
				if len(re_pa) == 0:
					lines = r'{ type:Loader.ATLAS, url:"'+re+'"},'+"\n"
				else: 
					lines = r'{ type:Loader.ATLAS, url:"'+re_pa+'/'+re+'"},'+"\n"
			f.writelines(lines.replace('\\', '/'))
		pass
	f.close()
	pass


file('.')
# print(sys.path[0], sys.path[0].find('res'))
