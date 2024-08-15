# form_maker
Form Maker creates student specific TRUF, SPVR, and CEP survey pdfs with QR codes for easy management and tracking of school forms.  Individual student forms output to their respective directories (TRUF, SPVR, and CEP) as PDFs and are named using the convention 'room-studentID'.  Additionally, individual student PDFs are grouped by type (TRUF, SPVR, and CEP) and sorted by classroom, then merged into print_truf.pdf, print_spvr.pdf, and print_survey.pdf documents for easy printing and distribution.  Each time this applicaiton is ran, new students are identified and forms are automatically created.  Printing of forms can also be automated if desired.  The print_spvr.pdf and print_cep.pdf documents will print double-sided, while print_truf.pdf will print single-sided.<br />

Form Maker also combines Infinite Campus' extracts and Data Studio's exports into sharable Google Sheets that allows teachers to easily sort and group student information.  <br />

Spreadsheet #1 is used by my inventory management system. <br /> 

Spreadsheet #2 is shared with my curriculum coordinator and is meant to convert Data studio's output from . . . <br />
**'School, DisplayName, UserName, Grade, Pass, First Name, Last Name, Alias'** 

to <br />

**'State ID, First Name, Last Name, Gmail Address, Gmail Password, Grade, Homeroom #, Teacher Name'** <br />

As you may have noticed, the Datastudio's export doesn't contain teacher/homeroom assignments.  This is an issue when teachers request their students Google credentials.  By consolidating the Datastudio export with Infinite Campus extract, students' Google credentials can be sorted by grade and homeroom making it much easier to share students' Google usernames and passwords with teachers.  <br />

## Requirements
This project was developed in a macOS environment using Python.  If you woujld like to use this project with minimal modification, ensure that the following requirements are met . . . <br />
1.  Install: <br />
        *  Gspread,
        *  ImageMagick,
        *  Pypdf, 
        *  Pandas, 
        *  Sengo 

2.  Configure you Google API: This project makes calls to a Google Workspace API. You can find information about setting up your Google API here . . . <br />
    https://developers.google.com/docs/api/quickstart/python <br />

3.  In main.py . . . 
        *  Configure your Google API by setting . . .
              google.json file name (google.json file should go into the creds directory of this project), <br />
              spreadsheet #1 id, <br />
              spreadsheet #2 id, <br />
              spreadsheet #1 tab_name, <br />
              spreadsheet #2 tab_name <br />

        *  Set the path of ImageMagick. 
        *  Decide if you want to automate printing of forms.  If you, set the boolean value of print_forms to True.

5.  Make sure template files (trug.jpg, spvr.jpg, cep.jpg) have a width of 1275 px, height of 1650 px, and a resolution of 150 pixel/inch.
    You can configure this in Preview by navigating to Tools > Adjust Size.  School year 2024-2025 template files are located in the templates directory, but must be updated as new form versions are released. <br />

6.  Infinite Campus extract should be in the following format <br />
    ("State ID\tFirst Name\tLast Name\tGrade\tHomeroom #\tTeacher Name\tBirthdate") <br />

7.  DataStudio extract should be in the following format <br />
    ("School,DisplayName,UserName,Grade,Pass,First Name,Last Name,Alias") <br />
