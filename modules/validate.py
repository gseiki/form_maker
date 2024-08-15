import subprocess

class Validate:    
    def __init__(self):
        self.file = "file.csv"
        self.delimiter = "-"
        self.expected_header = ""
        self.header = ""

    def set_file(self, new_file):
        self.file = new_file

    def set_delimiter(self, new_delimiter):
        self.delimiter = new_delimiter

    def set_header(self, new_header):
        self.expected_header = new_header.strip()

    def delimiter_bool(self):
        # Get the column names of the csv file
        command = ('cat %s | head -1' % (self.file))
        header_str = subprocess.check_output(command, shell=True)
        # Get the column names in string format
        header_row = header_str.decode('ascii')
        # Remove the line return character
        self.header = header_row.strip()
        # If delimiter is in header return true
        if self.delimiter in self.header:
            self.delimiter_pass = True
        else:
            self.delimiter_pass = False

    def header_bool(self):
        # If header is as expected return true
        if self.header == self.expected_header:
            self.header_pass = True
        else:
            self.header_pass = False

    def file_status(self):
        self.delimiter_bool()
        self.header_bool()
        # Return true if both header and delimiter passed conditional statements
        if not self.header_pass:
            print("Header for %s file is incorrect . . ." % self.file)
            print("It should look like this . . .")
            print("%s" % self.expected_header)
            print("But, I got this instead!")
            print("%s" % self.header)

        if not self.delimiter_pass:
            print("Delimiter for %s file is incorrect . . ." % self.file)
            print("Delimiter should be '%s' . . ." % self.delimiter)
            print("But, I got something else instead!" % self.delimiter)
        if self.header_pass and self.delimiter_pass:
            return True
        else:
            return False

    def data_frame(self, df):
        # Dataframe was created from a Google Sheet.
        # We need to make sure that the Google Sheet has the right . . .
        # headers or it will break the script.  Check the dataframe . . .
        # headers.  If the dataframe headers are correct, the Google . . .
        # Sheet headers were correct. 
        df_header = df.columns.tolist()
        expected_header = self.expected_header.split(self.delimiter)
        if df_header != expected_header:
            print("Check the Google Sheet headers . . .")
            print("It should look like this . . . ")
            print(expected_header)
            print("")
            print("But looks like this instead . . .")
            print(df_header)
            return False
        else:
            return True