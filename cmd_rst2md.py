# -*- coding: utf-8 *-8
import os
import sys
import subprocess

inws = os.path.abspath('./source')
outws = os.path.abspath('./source_md')
print(inws)
print(outws)

for wroot, wdirs, wfiles in os.walk(inws):
    # for wdir in wdirs:
    #     print('-' * 20)
    #     adir = os.path.join(wroot, wdir)
    #     bdir = os.path.join(outws, adir[len(inws) + 1: ])
    #     print(adir)
    #     print(bdir)

    for wfile in wfiles:
        qian, hou = os.path.splitext(wfile)
        if hou == '.rst':
            pass
        else:
            continue
        afile = os.path.join(wroot, wfile)
        bfile = os.path.join(outws, afile[len(inws) + 1 : ])

        xdir, xfile = os.path.split(bfile)
        if os.path.exists(xdir):
            pass
        else:
            os.makedirs(xdir)
        cmd = 'pandoc --from rst --to markdown_strict {afile} -o {bfile}md'.format(afile = afile, bfile = bfile[:-3])
        subprocess.call(cmd, shell=True)
        print(cmd)


