chmod 755 ./*
mkdir /usr/share/fonts/xpfonts
cp * /usr/share/fonts/xpfonts
cd /usr/share/fonts/xpfonts
mkfontscale
mkfontdir
fc-cache -fv
fc-list
