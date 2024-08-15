# form_maker
Form Maker creates unique TRUF, SPVR, and CEP survey pdfs for each new student.  
<br />
Form Maker also combines HIDOE's Infinite Campus' extract and Data Studio's export into sharable Google Sheets that allows staff members to easily sort and group student information.  <br />

Spreadsheet #1 is used by Princess Nahienaena Elementary's inventory management system. <br /> 

Spreadsheet #2 is meant to convert Data studio's output from . . . <br />
**'School, DisplayName, UserName, Grade, Pass, First Name, Last Name, Alias'** 

<center>to</center> <br />

**'State ID, First Name, Last Name, Gmail Address, Gmail Password, Grade, Homeroom #, Teacher Name'** <br />

This makes it much easier to sort and share students' Google credentials with their teachers.  <br />

## Requirements
This project was developed in a macOS environment using Python.  If you woujld like to use this application with the least amount of modification, ensure that the following requirements are met . . . <br />
1.  Install: <br />
        Gspread, <br />
        Sengo, <br />
        Pypdf, <br />
        Pandas <br />

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
