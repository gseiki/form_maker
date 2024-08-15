# form_maker
Form Maker creates unique TRUF, SPVR, and CEP survey pdfs for each new student.  

Form Maker also combines HIDOE's Infinite Campus' extract and Data Studio's export into sharable Google Sheets that allows staff members to easily sort and group student information.  
Spreadsheet #1 is used by Princess Nahienaena Elementary's inventory management system.  Spreadsheet #2 is meant to convert Data studio's output from . . .
'School, DisplayName, UserName, Grade, Pass, First Name, Last Name, Alias' 

to 

'State ID, First Name, Last Name, Gmail Address, Gmail Password, Grade, Homeroom #, Teacher Name'

This makes it much easier to sort and share students' Google credentials with their teachers. Please adjust code to fit your needs. 

## Requirements
If you woujld like to use this application with the least amount of modification, ensure that the following requirements are met . . .
1.  Install:
        Gspread,
        Sengo,
        Pypdf,
        Pandas

2.  This app makes calls to a Google Workspace API. You can find information about setting up your Google API here . . .
    https://developers.google.com/docs/api/quickstart/python

3.  In main.py, set the path of your
        google.json file
        spreadsheet #1 id
        spreadsheet #2 id
        spreadsheet #1 tab_name
        spreadsheet #2 tab_name

4.  Make sure template files (trug.jpg, spvr.jpg, cep.jpg) have a width of 1275 px, height of 1650 px, and a resolution of 150 pixel/inch.
    You can configure this in Preview by navigating to Tools > Adjust Size.

5.  Infinite Campus extract should be in the following format ("State ID\tFirst Name\tLast Name\tGrade\tHomeroom #\tTeacher Name\tBirthdate")

6.  DataStudio extract should be in the following format ("School,DisplayName,UserName,Grade,Pass,First Name,Last Name,Alias")

7.  If you want Roster Maker to automatically print your forms, you must uncomment the following lines in main.py . . .
        magick.print_trug()
        magick.print_spvr()
        magick.print_survey()
