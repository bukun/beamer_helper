\NeedsTeXFormat{LaTeX2e}[1999/12/01]
\ProvidesClass{ogl_booktp}[2005/07/06 0.1 Tsinghua University Thesis Template for Doctor and Master]

\LoadClass[11pt, oneside]{book}[2009/05/05]  % book, oneside，避免双面排版

% \DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}

% 双面排版使用， 不然用下面
% \RequirePackage[showframe=false,twoside,headheight=5mm,headsep=7mm,footskip=1em, bindingoffset=10mm]{geometry}

% 不然用下面
\usepackage{geometry}

% \geometry{top=.8in,bottom=.5in,left=.5in,right=.5in,paperheight=7.4in, paperwidth=12.20in }
% \geometry{top=1in,bottom=1.2in,left=1.45in,right=1.25in, lines=.5in}
% \geometry{papersize={170mm,240mm},top=20mm,textwidth=130mm,lines=36,inner=15mm}

\geometry{left=3.2cm,right=2.5cm,top=2.5cm,bottom=2.5cm, headsep=1cm, foot=1cm, bindingoffset=0mm}

% 可以修改页面的大小。双栏的话在类型中添加：twocolumn
% \geometry{top=1in,bottom=1in,left=1.65in,right=1.05in,paperheight=7.4in, paperwidth=12.20in }

\columnsep=.8cm % 双栏article中, 左右栏间空白的距离
\columnseprule=0.4pt  % 双栏article中, 左右栏间分隔线的宽度, 缺省 为零, 即没 有线

% \predisplaypenalty    = \z@
% \postdisplaypenalty   = \z@
% \clubpenalty              = \z@
% \widowpenalty=\z@
% \displaywidowpenalty = \z@
% \interlinepenalty         = \z@
