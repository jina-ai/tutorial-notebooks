from jina import Flow

flow = (
    Flow(monitoring=True)
    .add(uses="jinahub+docker://CLIPEncoder")
    .add(uses="jinahub+docker://SimpleIndexer")
)

flow.to_k8s_yaml("config", k8s_namespace="clip-search")
