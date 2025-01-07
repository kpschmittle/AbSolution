from absolution.processing_steps.processing_step import ProcessingStep


class ClusteringProcessingStep(ProcessingStep):
    def __init__(self, algorithm, min_cluster_size, max_cluster_size): #
        self.algorithm = algorithm
        self.min_cluster_size = min_cluster_size
        self.max_cluster_size = max_cluster_size

    def run(self, working_df):
        pass




