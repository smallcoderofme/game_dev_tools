//https://sharp.pixelplumbing.com/api-output#tofile
const sharp = require('sharp');
const path = require("path");
const fs = require('fs');
var data = sharp("2809.png")
	.webp({ lossless: true })
	// .limitInputPixels(0)
	// .tile({size: 256})
	.toFile("out.webp", (err, info) => {
		if (err === null) {
			console.log('toFile complete!');
		} else {
			console.log('toFile err:', err);
		}
	});