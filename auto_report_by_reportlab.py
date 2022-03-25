
def colr(x, y, z):
    return (x/255, y/255, z/255)

import reportlab
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
from reportlab.platypus import SimpleDocTemplate, TableStyle, Paragraph, Image, Spacer, Frame, Paragraph
from reportlab.platypus.tables import Table
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from subprocess import Popen


pdfmetrics.registerFont(TTFont('THSarabun', 'THSarabun.ttf'))
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
styleN.alignment = TA_LEFT
width, height = A4
logo = 't1.png'
elements = []
print(f'Height={height}')
imgw = imgh = 100
im = Image(logo, width=imgw, height=imgh)
im.hAlign = 'LEFT'
elements.append(im)

headstyle = ParagraphStyle(
    name='MyHeader',
    fontName='THSarabun',
    fontSize=16,
    leading =10
)
doctorstyle = ParagraphStyle(
    name='MyDoctorHeader',
    fontName='THSarabun',
    fontSize=18,
    leading =10
)
data = [[Paragraph("Genover Program", style = headstyle)], [Paragraph("Dr A", style = doctorstyle)], [Paragraph("ข้อมูล หมอ แพทย์เชี่ยวชาญจาก รามา", style = doctorstyle)], [Paragraph("Ref No. 1563", style = doctorstyle)], [Paragraph("\n", style = doctorstyle)]]
elements.append(Table(data, repeatRows=1))
line1 = ("Costomer_ID", "Name", "Lastname", "Date_Time","Photo")
img1 = 't2.png'
gw = gh = 20
im1 = Image(img1, width=gw, height=gh)
line2 = ("01662", "Mr.A","B", "14-11-2018",im1)
data=[line1,line2]

patientdetailstable = Table(data)
patientdetailstable.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (4, 0), '#CFEAD4'),
    ('BACKGROUND', (0, 2), (4, 2), '#CFEAD4'),
    ('BOX',(0,0),(-1,-1), 0.5, '#CFEAD4'),
    ('GRID',(0,0),(-1,-1), 0.5, colr(12, 43, 8)),
]))
elements.append(patientdetailstable)
elements.append(Spacer(1, 20))
# We use paragraph style because we need to wrap text. We cant directly wrap cells otherwise
line1 = ["No.", "SNP-Name" , "Description", "Score", "Risk", "Note"]
snp1 = Paragraph('GAT-ATT-AAA', styleN)
snp2 = Paragraph('AAA-TTT', styleN)
line2 = ["1", snp1, "cancer-A", "80", "High", "No comments"]
line3 = ["2", snp2, "heart disease", "75", "Medium", "Re-check"]
data=[line1,line2, line3]
for i in range(3,10):
    temp = [str(i), "---", "-", "-", "-", "No comments"]
    data.append(temp)

medstable = Table(data, repeatRows=1)
medstable.setStyle(TableStyle([
    ('VALIGN',(0,0),(-1,-1), 'TOP'),
    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
    ('BACKGROUND', (0, 0), (-1, 0), colr(40, 196, 15)),
    ('GRID',(0,1),(-1,-1), 0.5, '#CFEAD4'),
                            ]))
elements.append(medstable)
doc = SimpleDocTemplate('output.pdf', pagesize=A4, rightMargin=20, leftMargin=20, \
    topMargin=20, bottomMargin=20, allowSplitting=1,\
    title="Prescription", author="MyOPIP.com")
doc.build(elements)

Popen('output.pdf', shell=True)
