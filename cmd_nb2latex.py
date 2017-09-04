# -*- coding: utf-8 *-8
import os
import sys
import subprocess
import shutil

# outws = os.path.abspath('./xx_src_latex_raw')
outws = os.path.abspath('./part010')



if os.path.exists(outws):
    pass
else:
    os.mkdir(outws)


def convert(inws, sig = ''):
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
            thefile = os.path.join(wroot, wfile)
            if sig:
                if sig in thefile:
                    pass
                else:
                    continue


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
                cmd = 'jupyter-nbconvert {afile} --to latex --template base ' \
                      '--output-dir {outdir} --output {outname}'.format(
                    afile=afile,
                    bfile=bfile[:-3],
                    outdir=xdir,
                    outname='_'.join(fname_arr) + '.tex')
                print('=' * 20)
                print(cmd)
                subprocess.call(cmd, shell=True)

                outfile = os.path.join(xdir, '_'.join(fname_arr) + '.tex')
                print(outfile)
                cnts = open(outfile).readlines()
                with open(outfile, 'w') as file_out:
                    sig = False
                    for cnt in cnts:
                        if '\end{document}' in cnt:
                            sig = False

                        if sig:
                            cnt = cnt.replace('\subsection', '\subsubsection')
                            cnt = cnt.replace('\section', '\subsection')
                            file_out.write(cnt)

                        if '\maketitle' in cnt:
                            sig = True


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
    inws = os.path.abspath('./xx_src_nb')
    sig = ''
    if len(sys.argv) > 1:
        sig = os.path.split(sys.argv[1])[-1]
        print(sig)
    convert(inws, sig = sig)
