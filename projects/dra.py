import pandas as pd
import docxtpl
from docxtpl import DocxTemplate
import sys
from views import exam_path

from django.http.response import HttpResponse


import os

GDRAT_abs_path =  os.path.join(os.path.dirname(os.path.dirname(__file__)),'projects/media/examGPT/exam_template.docx')
G = GDRAT_abs_path.replace('\\', '/')
exam = DocxTemplate(G)
print(G)
print(exam_path)
