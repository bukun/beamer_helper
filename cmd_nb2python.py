# -*- coding: utf-8 *-8
import os
import sys
import subprocess
import shutil

inws = os.path.abspath('./xx_src_nb')
outws = os.path.abspath('./xx_src_python')

if os.path.exists(outws):
    pass
else:
    os.mkdir(outws)

for wroot, wdirs, wfiles in os.walk(inws):
    # for wdir in wdirs:
    #     print('-' * 20)
    #     adir = os.path.join(wroot, wdir)
    #     bdir = os.path.join(outws, adir[len(inws) + 1: ])
    #     print(adir)
    #     print(bdir)
    if 'ipynb_checkpoints' in wroot:
        continue

    for wfile in wfiles:
        print(os.path.join(wroot, wfile))


        qian, hou = os.path.splitext(wfile)
        if hou == '.ipynb' and qian.startswith('sub'):
            fname_arr = qian.split('_')
            fname_arr[1] = 'x_' + fname_arr[1]
            afile = os.path.join(wroot, wfile)
            bfile = os.path.join(outws, afile[len(inws) + 1:])

            xdir, xfile = os.path.split(bfile)
            if os.path.exists(xdir):
                pass
            else:
                os.makedirs(xdir)
            cmd = 'jupyter-nbconvert {afile} --to python --output-dir {outdir} --output {' \
                  'outname}'.format(
                afile=afile,
                bfile=bfile[:-3],
                outdir=xdir,
                outname='_'.join(fname_arr) + '.py')

            subprocess.call(cmd, shell=True)

            the_file = os.path.join(xdir, '_'.join(fname_arr) + '.py' )
            cnts = open(the_file).readlines()

            with open(the_file, 'w') as file_o:
                for cnt in cnts:
                    uu = cnt.strip()
                    if uu.startswith('#') or uu == '':
                        pass
                    else:
                        # print(cnt)
                        file_o.write(cnt)

            new_cnts = open(the_file).readlines()
            if len(new_cnts)> 0:
                pass
            else:
                os.remove(the_file)


        elif hou == '.png':
            afile = os.path.join(wroot, wfile)
            bfile = os.path.join(outws, afile[len(inws) + 1:])
            xdir, xfile = os.path.split(bfile)
            if os.path.exists(xdir):
                pass
            else:
                os.makedirs(xdir)
            shutil.move(afile, bfile)
        else:
            continue

        # print(cmd)
