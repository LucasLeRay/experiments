from kedro.pipeline import Pipeline, node, pipeline


def preprocess(taxi):
    return taxi



def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess,
                inputs="taxi",
                outputs="processed_taxi",
                name="preprocess_taxi_node",
            ),
        ]
    )
