import os
heder_tmpl = '''\ProvidesPackage{{{name}}}[2005/07/06 0.1 Tsinghua University Thesis Template for Doctor and Master]'''

in_tmpl = open('tmpl_header.tex').readlines()
qian = ''
hou = ''

qian_switch = True
hou_swith = False
for the_line in in_tmpl:

    if '%<<<<' in the_line:
        qian_switch = False

    if qian_switch:
        qian +=  the_line
    if hou_swith:
        hou +=  the_line

    if '%>>>>' in the_line:
        hou_swith = True

dic = {
    'darkgreen': {
    'primary': '16272e',
    'secondary':  '58765a',
    'tertiary': 'afee9d',
    },

    # Color from: https://gist.github.com/zmwangx/21cda8eb0ab4b1b0e5aa
   'Stanford': {


    'primary': '8C1515',
    'secondary':  'D2C295',
    'tertiary': 'DAD7CB',

    },



    'blueone': {


    'primary': '2D6D79',
    'secondary':  '9CB5B1',
    'tertiary': 'DCD8D5',

    },

    'bluetwo': {

    'primary': '005f58',
    'secondary':  '52b5f3',
    'tertiary': 'f5c904',

    }

}

def_color_tmpl = '''\definecolor{{color_{ckey}}}{{HTML}}{{{cval}}}'''


for tkey in dic.keys():
    out_file = 'ogl_{sig}.sty'.format(sig = tkey.lower())
    with open(out_file, 'w') as fo:
        fo.write(heder_tmpl.format(name= os.path.splitext(out_file)[0]) + '\r')
        print(qian)
        print(out_file)
        fo.writelines(qian)
        for ckey in dic[tkey].keys():
            fo.write(def_color_tmpl.format(ckey = ckey, cval = dic[tkey][ckey]) + '\r')

        fo.writelines(hou)
