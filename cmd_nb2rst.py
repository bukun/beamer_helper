# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import shutil

inws = os.path.abspath('./xx_src_nb')
# outws = os.path.abspath('./xx_src_rst')
outws = os.path.abspath('./source')

if os.path.exists(outws):
    pass
else:
    os.mkdir(outws)


def clean_tmp_files():
    for wroot, _, wfiles in os.walk(outws):
        for wfile in wfiles:
            if '_x_' in wfile:
                # print(wfile)
                os.remove(os.path.join(wroot, wfile))


def convert_to_rst():
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
            # print(os.path.join(wroot, wfile))

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
                cmd = 'jupyter-nbconvert {afile} --to rst --output-dir {outdir} --output {outname}'.format(
                    afile=afile,
                    bfile=bfile[:-3],
                    outdir=xdir,
                    outname='_'.join(fname_arr) + '.rst')
                subprocess.call(cmd, shell=True)
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


if __name__ == '__main__':
    clean_tmp_files()
    convert_to_rst()
