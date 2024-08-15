import gspread
import pandas

class Google:
    def __init__(self):
        self.json = 'json'
        self.creds_dir = 'creds_dir'
        self.script_dir = 'scripts_dir'

    def set_json(self, new_json):
        self.json = new_json

    def set_creds_dir(self, new_creds_dir):
        self.creds_dir = new_creds_dir

    def set_script_dir(self, new_script_dir):
        self.script_dir = new_script_dir

    def import_sheet_to_dataframe(self, workbook_id, worksheet_name, df_name):
        json_path = ("%s/%s" % (self.creds_dir, self.json))
        service_account_file = json_path.format(self.script_dir)
        gc = gspread.service_account(filename=service_account_file)
        workbook = gc.open_by_key(workbook_id)
        worksheet = workbook.worksheet(worksheet_name)
        df_name = pandas.DataFrame(worksheet.get_all_records())
        return df_name

    def export_df_to_sheet(self, workbook_id, worksheet_name, df_name):
        json_path = ("%s/%s" % (self.creds_dir, self.json))
        service_account_file = json_path.format(self.script_dir)
        gc = gspread.service_account(filename=service_account_file)
        workbook = gc.open_by_key(workbook_id)
        worksheet = workbook.worksheet(worksheet_name)
        worksheet.clear()
        worksheet.update([df_name.columns.values.tolist()] + df_name.values.tolist())
