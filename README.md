# form_maker
Form Maker creates student specific TRUF, SPVR, and CEP survey pdfs with QR codes for easy management and tracking of school forms. Individual student forms output to their respective directories (TRUF, SPVR, and CEP) and named using 
the convention 'room-studentID'.  Additionally, forms are sorted by classroom and merged into one pdf document for easy printing and distribution. Each time this applicaiton is ran, new students are identified and forms are automatically created.<br />

Form Maker also combines Infinite Campus' extracts and Data Studio's exports into sharable Google Sheets that allows teachers members to easily sort and group student information.  <br />

Spreadsheet #1 is used by Princess Nahienaena Elementary's inventory management system. <br /> 

Spreadsheet #2 is meant to convert Data studio's output from . . . <br />
**'School, DisplayName, UserName, Grade, Pass, First Name, Last Name, Alias'** 

to <br />

**'State ID, First Name, Last Name, Gmail Address, Gmail Password, Grade, Homeroom #, Teacher Name'** <br />

This makes it much easier to sort and share students' Google credentials with their teachers.  <br />

## Requirements
This project was developed in a macOS environment using Python.  If you woujld like to use this application with the least amount of modification, ensure that the following requirements are met . . . <br />
1.  Install: <br />
        Gspread, <br />
        ImageMagick, <br />
        Pypdf, <br />
        Pandas, <br />
        Sengo, <br />

2.  Configure you Google API: This app makes calls to a Google Workspace API. You can find information about setting up your Google API here . . . <br />
    https://developers.google.com/docs/api/quickstart/python <br />

3.  In main.py, set the path of your <br />
        google.json file, <br />
        spreadsheet #1 id, <br />
        spreadsheet #2 id, <br />
        spreadsheet #1 tab_name, <br />
        spreadsheet #2 tab_name <br />

4.  Make sure template files (trug.jpg, spvr.jpg, cep.jpg) have a width of 1275 px, height of 1650 px, and a resolution of 150 pixel/inch.
    You can configure this in Preview by navigating to Tools > Adjust Size. <br />

5.  Infinite Campus extract should be in the following format <br />
    ("State ID\tFirst Name\tLast Name\tGrade\tHomeroom #\tTeacher Name\tBirthdate") <br />

6.  DataStudio extract should be in the following format <br />
    ("School,DisplayName,UserName,Grade,Pass,First Name,Last Name,Alias") <br />

7.  If you want Roster Maker to automatically print your forms, you must uncomment the following lines in main.py . . . <br />
    magick.print_trug() <br />
    magick.print_spvr() <br />
    magick.print_survey() <br />
