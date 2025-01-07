from absolution.processing_steps.processing_step import ProcessingStep

class LiabilitiesProcessingStep(ProcessingStep):
    def __init__(self, custom_liability_list):
        self.custom_liability_list = custom_liability_list

    def run(self, working_df):
        pass