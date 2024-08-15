import warnings
# Pandas' "inplace" argument will be depricated. 
# Until I have time to revise this module, I'm surpressing the warning . . .
# so I can get forms printed for this school year.
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas

class Dataframe:
    def __init__(self):
        self.df = ""
        self.roster_df = "df"

    def convert_csv_to_df(self, file, delimeter):
        self.df = pandas.read_csv(file, sep=delimeter)
        self.df = self.df.dropna()  # Drop any rows with 'NaN' values.
        return self.df

    def convert_num_to_k(self, new_df):
        self.df = new_df.copy(deep=True)
        self.df['Grade'].replace([91, 92, 93, 94], 'K', inplace=True)
        return self.df
    
    def make_roster(self, new_ic_df, new_ds_df):
        # You need to make copies of ic_df & ds_df because, in Python, dataframe input variables
        # are references to the actual dataframe.  If you don't make a copy, you'll change the 
        # actual dataframe in the main.py
        ic_df = new_ic_df.copy(deep=True)
        ds_df = new_ds_df.copy(deep=True)
        # Drop columns that you don't need from ds_df. You only need "UserName" and "Pass".
        ds_df.drop(['School', 'DisplayName', 'Grade', 'First Name', 'Last Name', 'Alias'], axis=1, inplace=True)
        # Rename ds_df columns to match google df so you can merge both dataframes.
        ds_df.rename(columns={"UserName": "Gmail Address", "Pass": "Gmail Password"}, inplace=True)
        self.roster_df = ic_df
        # In the df, make a new column called "Domain" and populate it with HIDOE's domain as the default value.
        self.roster_df['Domain'] = '@k12.hi.us'
        # Concatenate "State ID" and "Domain" to create "Gmail Address".
        self.roster_df['Gmail Address'] = self.roster_df['State ID'].astype(
            str) + self.roster_df['Domain']
        # Drop "Domain" from df because you don't need it anymore.
        self.roster_df.drop(['Domain'], axis=1, inplace=True)
        self.roster_df = pandas.merge(self.roster_df, ds_df, on=[
            'Gmail Address'], how='left')
        # Re-order the columns in the df.
        self.roster_df = self.roster_df[['State ID', 'First Name', 'Last Name', 'Gmail Address',
            'Gmail Password', 'Grade', 'Homeroom #', 'Teacher Name']]
        # Fill any empty rows in the passwrod column with 'NaN'. If you don't do this, you won't be able to write df to Google Sheets.
        self.roster_df['Gmail Password'] = self.roster_df['Gmail Password'].fillna(
            'STUDENT NOT IN 429 Org. Unit')
        return self.roster_df