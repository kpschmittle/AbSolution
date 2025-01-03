import os
import pandas as pd


class FormattedInput:

    abxtract_output_filepaths = []
    def __init__(self, input_folder, format_together):
        self.input_folder = input_folder
        self.format_together = format_together

    def format(self):
        self.filter_input_by_type()
        if self.format_together:
            dfs = self.combine_dfs()
        else:
            dfs = self.individual_dfs()
        return dfs

    def filter_input_by_type(self):
        for filename in os.listdir(self.input_folder):
            if filename.startswith('down.sanger'):
                self.abxtract_output_filepaths.append(os.path.join(self.input_folder, filename))

    def combine_dfs(self):
        abxtract_dfs = []
        for abxtract_filepath in self.abxtract_output_filepaths:
            abxtract_dfs.append(pd.read_csv(abxtract_filepath))
        return [pd.concat(abxtract_dfs)]

    def individual_dfs(self):
        abxtract_dfs = []
        for abxtract_filepath in self.abxtract_output_filepaths:
            abxtract_dfs.append(pd.read_csv(abxtract_filepath))
        return abxtract_dfs