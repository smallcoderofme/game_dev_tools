"use strict";

const path = require("path");
const fs = require('fs');


var file_list = [];
var config = [];
function get_name(file) {
	let lastDot = file.lastIndexOf('.');
	let pre = file.lastIndexOf('\\');
	return file.slice(pre+1, lastDot);
}
function run(file) {
	let file_name = get_name(file);
	let data = sharp(file)
		.jpeg()
		.limitInputPixels(0)
		.tile({size: 256})
		.toFile('big_comp_output/'+file_name, (err, info) => {
			if (err == null) {
				if (file_list.length) {
					console.log(file, 'slice complete.');
					setTimeout(()=> {
						run(file_list.shift());
					}, 1000);
				}
			} else {
				console.log('toFile err:', err);
			}
		});
}

function get_files(file_path){
	/**
    function files(path1){
        fs.readdir(path1,
        	function(err, files){
        		if (err) { throw err; }
		        files.forEach(function (item, index) {
		        	// console.log(item, index);
		            let f_path = path.join(path1,item);
		            fs.stat(f_path, function(err, stat) {
		            	if (err) { throw err; }
	            	    if(stat.isDirectory() === true) {
		                	files(f_path);
			            }
			            if (stat.isFile() === true) { 
			              	file_list.push(f_path);
	              			console.log('push file', f_path);
			            }
		            });
		        
		        });
    	});
    }
*/
    function files(path1){
     	let files = fs.readdirSync(path1);
        files.forEach(function (item, index) {
        	// console.log(item, index);
            let f_path = path.join(path1,item);
            let stat = fs.statSync(f_path);
            if(stat.isDirectory() === true) {
                files(f_path);
            }
            if (stat.isFile() === true) { 
              file_list.push(f_path);
            }
        });
    }

    files(file_path);
 
 //    file_list.forEach((file) => {
 //    	config.push(file.replace('inputs\\', '../outputs/').replace('.jpg','.dzi'));
 //    });
 
    console.log('总共获取文件数为:', file_list.length);
    fs.writeFile('output.txt', JSON.stringify(file_list), (err) => {
		if (err) throw err;
		console.log('output.txt was saved');
	});
}

get_files("input");