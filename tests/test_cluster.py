import pytest
from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException

def test_cluster_alive():

    try:
        config.load_kube_config()
    except ConfigException:
        pytest.skip("Kubeconfig non valido o cluster non disponibile")

    v1 = client.CoreV1Api()
    nodes = v1.list_node()

    assert len(nodes.items) > 0
