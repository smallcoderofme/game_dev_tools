# Version: ImageMagick 7.0.9-14 Q16 x64 2020-01-05 http://www.imagemagick.org *<br />

* image compress and resize <br />
magick convert -resize "4096x2048" -strip -quality 75% input.png output.png<br />
* format convert*<br />
magick convert rose.jpg rose.png<br />

* foramt convert and resize*<br />
 magick convert rose.jpg -resize 50% rose.png<br />

* generate gif animate*<br />
magick *.jpg images.gif <br />

* generate gif animate *<br />
 magick 'images.gif[0]' image.png <br />
 magick 'images.gif[0-3]' images.mng <br />

* selecting image region *<br />
 magick convert input.jpg[w x h + offsetX + offsetY] output.jpg <br />


myimages.txt  <br />
	frame001.jpg<br />
	frame002.jpg<br />
	frame003.jpg<br />

magick @myimages.txt mymovie.gif<br />
magick image-%d.jpg[1-5]  <br />
image-1.jpg
image-2.jpg
image-3.jpg
image-4.jpg
image-5.jpg