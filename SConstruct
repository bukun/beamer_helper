import os
env = Environment(ENV=os.environ, PDFLATEX = 'xelatex')

env.AppendUnique(PDFLATEXFLAGS='-shell-escape')
# env.AppendUnique(PDFLATEXFLAGS='-output-directory=build')


# flags = env.ParseFlags(['-output-directory=build'])
# env.MergeFlags(class_flags)

#  # environment['PDFLATEX'] = 'xelatex'
#  # target and source:
#  pdf_output = env.PDF(target='py3gis.pdf', source='py3gis.tex')
#  # Add synctex
#  env.AppendUnique(PDFLATEXFLAGS='-synctex=1')
#  # make sure that the pdf is reloaded properly (e.g., in Skim)
#  env.Precious(pdf_output)

dst = env.PDF("slide_casmooc_python_a.tex")
inst = env.Install("documents",dst)
Default(inst)

