# Version: ImageMagick 7.0.9-14 Q16 x64 2020-01-05 http://www.imagemagick.org *

* image compress and resize *
** magick convert -resize "4096x2048" -strip -quality 75% input.png output.png **
* format convert*
** magick convert rose.jpg rose.png**

* foramt convert and resize*
** magick convert rose.jpg -resize 50% rose.png**

* generate gif animate*
** magick *.jpg images.gif **

* generate gif animate *
** magick 'images.gif[0]' image.png **
** magick 'images.gif[0-3]' images.mng **

* selecting image region *
** magick convert input.jpg[wxh+offsetX+offsetY] output.jpg **