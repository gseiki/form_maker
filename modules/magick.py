# Documentation for segno can be found here "https://segno.readthedocs.io/en/1.3.3/index.html"
import segno # To install segno, run "python -m pip install segno"
import os
import subprocess
from pypdf import PdfWriter

class Magick:
    def __init__(self):
        self.magick_path = "magick_path"
        self.script_dir = "dir_path"
        self.template_dir = "dir_path"
        self.trug_dir = "dir_path"
        self.spvr_dir = "dir_path"
        self.survey_dir = "dir_path"
        self.png_path = ("image_path")
        self.jpg_path = ("image_path")
        self.trug_path = ("file_path")
        self.spvr_front = ("file_path")
        self.spvr_back = ("file_path")
        self.survey_front = ("file_path")
        self.survey_back = ("file_path")
        self.trug_result_path = ("file_path")
        self.spvr_result_path = ("file_path")
        self.survey_result_path = ("file_path")

    def set_magick_path(self, new_path):
        self.magick_path = new_path

    def set_script_dir(self, new_dir):
        self.script_dir = new_dir
        self.png_path = ("%s/qr.png" % (self.script_dir))
        self.jpg_path = ("%s/qr.jpg" % (self.script_dir))

    def make_trug_dir(self, new_dir):
        self.trug_dir = ("%s/trug-pdfs" % (new_dir))
        trug_dir_exists = os.path.exists(self.trug_dir)
        if trug_dir_exists:
            subprocess.run(['rm', '-r', self.trug_dir])
            subprocess.run(['mkdir', '-p', self.trug_dir])
        else:
            subprocess.run(['mkdir', '-p', self.trug_dir])

    def make_spvr_dir(self, new_dir):
        self.spvr_dir = ("%s/spvr-pdfs" % (new_dir))
        spvr_dir_exists = os.path.exists(self.spvr_dir)
        if spvr_dir_exists:
            subprocess.run(['rm', '-r', self.spvr_dir])
            subprocess.run(['mkdir', '-p', self.spvr_dir])
        else:
            subprocess.run(['mkdir', '-p', self.spvr_dir])

    def make_survey_dir(self, new_dir):
        self.survey_dir = ("%s/survey-pdfs" % (new_dir))
        survey_dir_exists = os.path.exists(self.survey_dir)
        if survey_dir_exists:
            subprocess.run(['rm', '-r', self.survey_dir])
            subprocess.run(['mkdir', '-p', self.survey_dir])
        else:
            subprocess.run(['mkdir', '-p', self.survey_dir])


    def set_template_dir(self, new_dir):
        self.template_dir = new_dir
        self.trug_path = ("%s/trug.jpg" % (self.template_dir))
        self.spvr_front = ("%s/spvr_front.jpg" % (self.template_dir))
        self.spvr_back = ("%s/spvr_back.jpg" % (self.template_dir))
        self.survey_front = ("%s/survey_front.jpg" % (self.template_dir))
        self.survey_back = ("%s/survey_back.jpg" % (self.template_dir))

    def make_trug(self, df_name):
        for index, row in df_name.iterrows():
            qr = (row['State ID'])
            fName = (row['First Name'])
            lName = (row['Last Name'])
            room = (row['Homeroom #'])
            name_and_id = ("%s %s (%s)" % (fName, lName, qr))
            name = ("%s %s" % (fName, lName))
            output_path = ("%s/%s_%s.pdf" % (self.trug_dir, room, qr))
            qr_png = segno.make_qr(qr) # Make the qr code
            qr_png.save( # Write the qr code to file
                       "qr.png",
                       scale=3, # "scale=5" will create a 5x5 pixel qr code
                       border=3, # "Border=0" will output no border.  If no border is specified, a default border will be created. Border is also called quietzone.
                       light="white", # Makes all white space in qr code light blue.
                       dark="black", # Makes all dark space in qr dark blue.
                       quiet_zone="white", # Quiet zone is the border of the qr code.  This command will change its color.:w

                       data_dark="blue", # Not all the modules in a qr code house the data that's encoded. Use "data_dark" to change the color of the dark data modules.
                       data_light="white", # Not all the modules in a qr code house the data that's encoded. Use "data_light" to change the color of the light data modules.
                       )
            subprocess.run([self.magick_path, self.png_path, self.jpg_path]) # Convert QR from jpg to png
            subprocess.run([self.magick_path, self.trug_path, 
                            "-font", "/Library/Fonts/Arial Unicode.ttf", "-fill", "blue", 
                            "-pointsize", "20", "-annotate", "+555+1225", "Princess Nahienaena Elementary", 
                            "-pointsize", "18", "-annotate", "+535+1360", name_and_id, 
                            "-pointsize", "26", "-annotate", "+50+50", name, 
                            "-annotate", "+50+85", room, 
                            self.jpg_path, "-geometry", "+1150+25", 
                            "-composite", "-matte", output_path])
            

    def make_spvr(self, df_name):
        for index, row in df_name.iterrows():
            qr = (row['State ID'])
            fName = (row['First Name'])
            lName = (row['Last Name'])
            room = (row['Homeroom #'])
            name_and_id = ("%s %s (%s)" % (fName, lName, qr))
            name = ("%s %s" % (fName, lName))
            output_path = ("%s/%s_%s.pdf" % (self.spvr_dir, room, qr))
            qr_png = segno.make_qr(qr) # Make the qr code
            qr_png.save( # Write the qr code to file
                       "qr.png",
                       scale=2, # "scale=5" will create a 5x5 pixel qr code
                       border=2, # "Border=0" will output no border.  If no border is specified, a default border will be created. Border is also called quietzone.
                       light="white", # Makes all white space in qr code light blue.
                       dark="black", # Makes all dark space in qr dark blue.
                       quiet_zone="white", # Quiet zone is the border of the qr code.  This command will change its color.:w

                       data_dark="blue", # Not all the modules in a qr code house the data that's encoded. Use "data_dark" to change the color of the dark data modules.
                       data_light="white", # Not all the modules in a qr code house the data that's encoded. Use "data_light" to change the color of the light data modules.
                       )
            subprocess.run([self.magick_path, self.png_path, self.jpg_path]) # Convert QR from png to jpg
            subprocess.run([self.magick_path, self.spvr_front, "-font", "/Library/Fonts/Arial Unicode.ttf", "-fill", "blue", 
                            "-pointsize", "20", "-annotate", "+125+1345", name_and_id, 
                            "-annotate", "+125+1410", "Princess Nahienaena Elementary", 
                            "-pointsize", "24", "-annotate", "+210+65", name, 
                            "-annotate", "+210+95", room, 
                            self.jpg_path, "-geometry", "+1120+45", 
                            "-composite", "-matte", self.spvr_back, output_path])
            
    def make_survey(self, df_name):
        for index, row in df_name.iterrows():
            qr = (row['State ID'])
            fName = (row['First Name'])
            lName = (row['Last Name'])
            grade = (row['Grade'])
            room = (row['Homeroom #'])
            birthdate = (row['Birthdate'])
            output_path = ("%s/%s_%s.pdf" % (self.survey_dir, room, qr))
            qr_png = segno.make_qr(qr) # Make the qr code
            qr_png.save( # Write the qr code to file
                       "qr.png",
                       scale=3, # "scale=5" will create a 5x5 pixel qr code
                       border=3, # "Border=0" will output no border.  If no border is specified, a default border will be created. Border is also called quietzone.
                       light="white", # Makes all white space in qr code light blue.
                       dark="black", # Makes all dark space in qr dark blue.
                       quiet_zone="white", # Quiet zone is the border of the qr code.  This command will change its color.:w

                       data_dark="blue", # Not all the modules in a qr code house the data that's encoded. Use "data_dark" to change the color of the dark data modules.
                       data_light="white", # Not all the modules in a qr code house the data that's encoded. Use "data_light" to change the color of the light data modules.
                       )
            subprocess.run([self.magick_path, self.png_path, self.jpg_path]) # Convert QR from png to jpg
            subprocess.run([self.magick_path, self.survey_front, "-font", "/Library/Fonts/Arial Unicode.ttf", "-fill", "blue", 
                            "-pointsize", "26", "-annotate", "+540+150", "Princess Nahienaena Elementary", 
                            "-annotate", "+110+310", lName, 
                            "-annotate", "+760+310", fName, 
                            "-annotate", "+140+430", grade,  
                            "-annotate", "+330+430", birthdate,  
                            "-annotate", "+630+430", room, 
                            "-annotate", "+900+430", 
                            qr, self.jpg_path, "-geometry", "+1150+35", 
                            "-composite", "-matte", self.survey_back, output_path])

    def combine_trug_pdfs(self):
        self.trug_result_path = ("%s/print_trug.pdf" % (self.trug_dir))
        pdf_array = sorted(os.listdir(self.trug_dir))
        merger = PdfWriter()
        for pdf in pdf_array:
            file = ("%s/%s" % (self.trug_dir, pdf))
            merger.append(file)
        merger.write(self.trug_result_path)
        merger.close()

    def combine_spvr_pdfs(self):
        self.spvr_result_path = ("%s/print_spvr.pdf" % (self.spvr_dir))
        pdf_array = sorted(os.listdir(self.spvr_dir))
        merger = PdfWriter()
        for pdf in pdf_array:
            file = ("%s/%s" % (self.spvr_dir, pdf))
            merger.append(file)
        merger.write(self.spvr_result_path)
        merger.close()

    def combine_survey_pdfs(self):
        self.survey_result_path = ("%s/print_survey.pdf" % (self.survey_dir))
        pdf_array = sorted(os.listdir(self.survey_dir))
        merger = PdfWriter()
        for pdf in pdf_array:
            file = ("%s/%s" % (self.survey_dir, pdf))
            merger.append(file)
        merger.write(self.survey_result_path)
        merger.close()

    def print_trug(self):
        subprocess.run(["lpr", "-o", "sides=one-sided", self.trug_result_path])

    def print_spvr(self):
        subprocess.run(["lpr", "-o", "sides=two-sided-long-edge", self.spvr_result_path])

    def print_survey(self):
        subprocess.run(["lpr", "-o", "sides=two-sided-long-edge", self.survey_result_path])