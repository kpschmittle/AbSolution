from .processing_step import ProcessingStep

class EnrichmentProcessingStep(ProcessingStep):
    def __init__(self, rounds):
        self.expected_rounds = rounds

    def run(self, working_df):
        pass