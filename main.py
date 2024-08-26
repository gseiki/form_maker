import sys  # Imported for "sys.path.append".
# Imported for "script_dir", "module_dir", and "creds_dir" variables.
import os
import subprocess  # Imported so I can run bash commands in my Python code.
from modules.dataframe import Dataframe
from modules.google import Google
from modules.magick import Magick
from modules.validate import Validate

script_name = os.path.basename(__file__)
script_dir = os.path.dirname(__file__)
module_dir = ("%s/modules" % (script_dir))
creds_dir = ("%s/creds" % (script_dir))
template_dir = ("%s/templates" % (script_dir))
output_dir = ("%s/output" % (script_dir))
tmp_dir = ("%s/tmp" % (script_dir))
tmp_ic = ("%s/tmp_extract.csv" % (tmp_dir))

### You need to change these variables to match your project ###
magick_path = ("/Path/To/ImageMagick") 
json = '/Name/of/Google/API/json/file' 
scanner_spreadsheet_id = 'spreadsheet_#1_id'
scanner_sheet_name = 'name_of_spreadsheet_#1_tab'
roster_spreadsheet_id = 'spreadsheet_#2_id'
roster_sheet_name = 'name_of_spreadsheet_#2_tab'

# Set your expected headers here.  If you change the headers on Google Sheets or in your Infinite Campus
# AdHoc report, you have to reflect it here.  "ic_header" is derived from "ic_dob_header"
# so the only difference between the two should be the "dob" field.
# If you changed any of these headers, you'll also have to change the headers of old_student_df in the main.
ic_dob_header = ("State ID\tFirst Name\tLast Name\tGrade\tHomeroom #\tTeacher Name\tBirthdate")
ic_header = ("State ID\tFirst Name\tLast Name\tGrade\tHomeroom #\tTeacher Name")
ds_header = ("School,DisplayName,UserName,Grade,Pass,First Name,Last Name,Alias")

# If you want to automat printing of forms, change boolean to True
print_forms = False

###################################################
## If you followed the README requirements . . . ##
## you shouldn't have to change anythin below    ##
###################################################

def main():
    # Check to see if user provided the necessary arguments to run the script.
    try:
        ic_dob_file = sys.argv[1]
        ds_file = sys.argv[2]
    except:
        print("")
        print("Usage: %s <infinite_campus.csv> <data_studios.csv>" % script_name)
        print("")
        sys.exit(1)

    # In order to print NEW CEP forms, I needed to include birthdate on IC extract.
    # But, the extra field caused all kinds of problems else where in this app.
    # So, I'm sucking birthdate in above as an argument, then making a tmp file with
    # it removed so I can I basically have two extracts.  One with, and one without,
    # birthdate.

    # Create a copy of IC extract with birthdate column removed and call it ic_file
    tmp_dir_exists = os.path.exists(tmp_dir)
    if tmp_dir_exists:
        subprocess.run(['rm', '-r', tmp_dir])
        subprocess.run(['mkdir', '-p', tmp_dir])
    else:
        subprocess.run(['mkdir', '-p', tmp_dir])
    bash_command = ('cat %s | cut -f 1,2,3,4,5,6 > %s' % (ic_dob_file, tmp_ic))
    subprocess.check_output(bash_command, shell=True)
    ic_file = tmp_ic

    # Make sure the ic extract with birthdates has the correct header and delimiter
    validate_ic = Validate()
    validate_ic.set_file(ic_dob_file)
    validate_ic.set_delimiter("\t")
    validate_ic.set_header(ic_dob_header)
    ic_validated = validate_ic.file_status()

    # Make sure the ic extract has the correct header and delimiter
    validate_ic = Validate()
    validate_ic.set_file(ic_file)
    validate_ic.set_delimiter("\t")
    validate_ic.set_header(ic_header)
    ic_validated = validate_ic.file_status()

    # Make sure the ds export has the correct header and delimiter
    validate_ds = Validate()
    validate_ds.set_file(ds_file)
    validate_ds.set_delimiter(",")
    validate_ds.set_header(ds_header)
    ds_validated = validate_ds.file_status()

    if ic_validated and ds_validated:
        # Read csv files into DataFrames.
        ic_dataframe = Dataframe()
        ic_df = ic_dataframe.convert_csv_to_df(ic_file, "\t")
        ic_df = ic_dataframe.convert_num_to_k(ic_df)
        ds_df = Dataframe()
        ds_df = ds_df.convert_csv_to_df(ds_file, ",")
        ic_dob_dataframe = Dataframe()
        ic_dob_df = ic_dob_dataframe.convert_csv_to_df(ic_dob_file, "\t")
        ic_dob_df = ic_dob_dataframe.convert_num_to_k(ic_dob_df)

        # Make a DataFrame to update the shared student roster spreadsheet.
        # Datastudios has students' Google credentials, but no class information.
        # This dataframe combines student class info with their google info for
        # easy sharing of Google passwords with teachers.
        roster_df = Dataframe()
        roster_df = roster_df.make_roster(ic_df, ds_df)

        # Create your Google object and set credentials.
        google = Google()
        google.set_json(json)
        google.set_creds_dir(creds_dir)
        # Pass script_dir to Google object so it knows where to find creds.
        google.set_script_dir(script_dir)
        # Backup the old student roster from the scanner Google Sheet.
        validate_google_sheet = Validate()
        # use the same delimiter as ic_header because you're comparing
        validate_google_sheet.set_delimiter("\t")
        # dataframe to ic_header.
        validate_google_sheet.set_header(ic_header)
        old_student_df = google.import_sheet_to_dataframe(
            scanner_spreadsheet_id, scanner_sheet_name, "old_student_df")
        # Check to see if Sheet is empty.  If it is, you'll need to create a df with column headings.
        sheet_empty = old_student_df.empty
        if sheet_empty:
            old_student_df['State ID'] = 'state_id'
            old_student_df['First Name'] = 'first_name'
            old_student_df['Last Name'] = 'last_name'
            old_student_df['Grade'] = 'grade'
            old_student_df['Homeroom #'] = 'homeroom_#'
            old_student_df['Teacher Name'] = 'teacher_name'
            google_df_validated = validate_google_sheet.data_frame(
                old_student_df)
        else:
            google_df_validated = validate_google_sheet.data_frame(
                old_student_df)

        if google_df_validated:
            # Compare ic_df to old_student_df.  If they differ, identify changes.
            # The ic_df index is off.  Before you compare the two DFs, reset . . .
            # the ic_df index or you'll receive and incorrect boolean value.
            ic_df.reset_index(drop=True, inplace=True)
            the_same = ic_df.equals(old_student_df)
            if not the_same:
                # Next two lines were added so you can create survey pdfs.
                new_survey_df = ic_dob_df[~ic_dob_df['State ID'].isin(
                    old_student_df['State ID'])]
                new_survey_df.reset_index(drop=True, inplace=True)
                new_students_df = ic_df[~ic_df['State ID'].isin(
                    old_student_df['State ID'])]
                new_students_df.reset_index(drop=True, inplace=True)
                new_student_df_is_empty = new_students_df.empty
                if new_student_df_is_empty:
                    print("No new students were found . . .")
                    print(
                        "but roster changes were detected, and necessary Google Sheets were updated!")
                    google.export_df_to_sheet(
                        scanner_spreadsheet_id, scanner_sheet_name, ic_df)
                    google.export_df_to_sheet(
                        roster_spreadsheet_id, roster_sheet_name, roster_df)
                else:
                    print(
                        "Found new students! Creating forms and updating Google Sheets!")
                    magick = Magick()
                    magick.set_script_dir(script_dir)
                    magick.set_magick_path(magick_path)
                    magick.make_truf_dir(output_dir)
                    magick.make_spvr_dir(output_dir)
                    magick.make_survey_dir(output_dir)
                    magick.set_template_dir(template_dir)
                    magick.make_truf(new_students_df)
                    magick.make_spvr(new_students_df)
                    magick.make_survey(new_survey_df.astype(str))
                    magick.combine_truf_pdfs()  # Combine all truf forms into one pdf
                    magick.combine_spvr_pdfs()  # Combine all SPVR forms into one pdf
                    magick.combine_survey_pdfs()  # Combine all CEP survey forms into one pdf
                    if print_forms:
                        print("Printing  PDF forms . . . ")
                        magick.print_truf()
                        magick.print_spvr()
                        magick.print_survey()
                    google.export_df_to_sheet(
                        scanner_spreadsheet_id, scanner_sheet_name, ic_df)
                    google.export_df_to_sheet(
                        roster_spreadsheet_id, roster_sheet_name, roster_df)


if __name__ == '__main__':
    main()
