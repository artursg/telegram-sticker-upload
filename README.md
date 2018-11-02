# Automatical Telegram Stickers Uploader

# Requirements
1. telegram-cli [link](https://github.com/vysheng/tg "link").
2. pytg [link](https://github.com/luckydonald/pytg "link").
3. configparser.

# Instruction: 

1. precondition images;
2. edit configuration file according your specifics;
3. launch ./telegram-sticker-upload.py;
4. check telegram output to fix occured issues. 

# Image preconditioning

> The image file should be in PNG format with a transparent layer and must fit into a 512x512 square (one of the sides must be 512px and the other 512px or less).

Fitting to 512x512 box can be easily be achieved using ImageMagick ([link](https://www.imagemagick.org "link")), using `convert "*.png" -resize 512x512 sticker.png`. 
