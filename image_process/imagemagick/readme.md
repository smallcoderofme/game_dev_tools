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