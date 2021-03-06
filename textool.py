#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys
import shutil

# 注意，文件夹中要包含字符串
fz_dict = {'part': 'ch',
           'ch': 'sec',
           'slide': 'sec',
           'cha': 'test',  # For simple book.
           'sec': 'test',
           }
# magic_str = '%----%'
magic_str = '%%%% ==== %%%% ==== %%%% ==== %%%%'


def get_tmp_file(fileobj, fig_index=1, file_ext='png'):
    return os.path.join(
        os.path.split(os.path.realpath(fileobj))[0],
        'xx' + os.path.split(os.path.realpath(fileobj))[1][4:-3] + '{0}.{1}'.format(fig_index, file_ext)
    )


def get_file_path(inroot, wname):
    '''
    根据给定的路径，得到文件的路径
    找不到的話，就返回空字符串
    '''
    # print('x' * 20)
    # print(inroot)
    # print(wname)
    if wname.startswith('pa') or wname.startswith('ch') or wname.startswith('sec'):
        # 对章节不处理
        return ''
    for wroot, wdirs, wfiles in os.walk(inroot):
        for wfile in wfiles:
            # 分别对两使用情况进行处理
            # 使用include的时候，可能不会包含.tex后缀
            #
            if wfile == wname:
                # print('y' * 10)
                outpath = os.path.join(wroot, wfile)
                # print(outpath)
                return outpath
            tt = os.path.splitext(wfile)[0]
            if tt == wname:
                # print('y' * 10)
                outpath = os.path.join(wroot, tt)
                # print(outpath)
                return outpath
    # print('not find')
    return ''


def check_condition(instr):
    '''
    对条件进行判断
    '''
    if r'\includegraphics' in instr:
        return True
    if r'\lstinput' in instr:
        return True
    if r'\input' in instr:
        return True
    if r'\adjustimage' in instr:
        return True
    return False


def bianli_chili_include(inws, pre_len=0):
    '''
    对tex文件中的图片，程序等引用外部文件的进行处理
    '''
    for wroot, wdirs, wfiles in os.walk(inws):
        for wfile in wfiles:
            if wfile.endswith('tex'):
                # print(wfile)
                cur_file = os.path.join(wroot, wfile)

                # 使用临时文件写入，防止出现问题
                tep_name = os.path.join(wroot, 'tmp_' + wfile)
                cnts = open(cur_file).readlines()
                fo = open(tep_name, 'w')
                for cnt in cnts:
                    if check_condition(cnt) == True:
                        '''
                        注意，只許出现在一行中，并且有且只能有一组{}
                        '''
                        # print(cnt)

                        # print('=' * 80)

                        ind_start = cnt.rindex('{')
                        ind_end = cnt.rindex('}')

                        filepath = cnt[ind_start + 1:ind_end]

                        filename = os.path.split(filepath)[-1]

                        houzhui = os.path.splitext(filename)[-1]
                        outpath = get_file_path(wroot, filename)

                        if outpath == '':
                            # print("Not Found")
                            pass
                        else:
                            # 根据当前路径处理
                            outpath = '.' + outpath[pre_len:]
                            tmp = cnt.replace(filepath, outpath)

                            cnt = tmp

                    fo.write(cnt)
                fo.close()

                os.remove(cur_file)
                shutil.move(tep_name, cur_file)


def zuzhi_dir(inws, sig_main, w_len):
    # 根据两个标识来分另寻找主tex与组成tex
    sig_zucheng = fz_dict[sig_main]
    # print(inws)
    # 只以文件夹前面进行判断

    # 当前文件夹下对应的主tex文件
    main_tex_file = ''
    # 主tex文件的组成文件
    zucheng_files = []

    '''
    对文件进行遍历
    找到唯一的文件
    并找到组成的文件
    '''
    for wroot, wdirs, wfiles in os.walk(inws):
        for wfile in wfiles:
            if wfile.endswith('tex') == False:
                continue
            if wfile.startswith(sig_main):
                # 找到唯一的main_tex_file
                # print(wfile)
                main_tex_file = os.path.join(wroot, wfile)
                # 在此文件下面进行操作

    if len(main_tex_file) > 0:
        pass
    else:
        return

    for w2root, w2dirs, w2files in os.walk(inws):
        for w2file in w2files:
            if w2file.startswith(sig_zucheng) and w2file.endswith('.tex'):
                w2filein = os.path.join(w2root, w2file)
                # print(w2filein)
                zucheng_files.append(w2filein)
    if len(zucheng_files) > 0:
        pass
    else:
        return

    zucheng_files.sort()

    cnts = open(main_tex_file).readlines()

    fo = open(main_tex_file, 'w')
    for cnt in cnts:
        if cnt.startswith('%----%') or cnt.startswith(magic_str):
            break
        fo.write(cnt)
    fo.write('%s\n' % magic_str)

    for zucheng_file in zucheng_files:
        # print('-' * 80)
        # print(zucheng_file)
        # 取第一行，写入
        tep = open(zucheng_file).readlines()[0]
        fo.write('%% %s' % (tep))
        # 写入组成文件
        zucheng_file = zucheng_file[w_len:-4]
        fo.write('\input{.%s}\n\n' % (zucheng_file))

    fo.close()


def do_for_dir(inws, pre_len=0):
    w_len = len(inws)

    for wroot, wdirs, wfiles in os.walk(inws):
        switch = False

        if 'part0' in wroot:
            switch = True
        else:
            for wdir in wdirs:
                if 'part0' in wdir:
                    switch = True

        for wdir in wdirs:
            indir = os.path.join(wroot, wdir)
            '''
            此处对keys进行遍历，然后逐个判断
            我想这样代码更好理解
            因为也不会太多，不考虑效率的事了
            '''
            for fzkey in fz_dict.keys():
                if wdir.startswith(fzkey):
                    sig_main = fzkey
                    # 分别得到目录的名称，下一级的标识，以及路径的长度
                    zuzhi_dir(indir, sig_main, pre_len)


if __name__ == '__main__':
    # if len(sys.argv) > 1:


    fuws = os.path.join(os.getcwd(), sys.argv[1])
    # print(fuws)
    # else:
    #     fuws = os.getcwd()
    # fuws = os.path.join(os.getcwd(), 'part010/ch06_shapely/sec2_geometry_opt')
    # generate_init()
    root_len = len(os.getcwd())
    do_for_dir(fuws, pre_len=root_len)
    bianli_chili_include(fuws, pre_len=root_len)
