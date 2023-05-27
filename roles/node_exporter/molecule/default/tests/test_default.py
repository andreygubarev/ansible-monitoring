"""Role testing files using testinfra."""


def test_node_exporter_service(host):
    """Validate node_exporter service."""
    s = host.service("node_exporter")

    assert s.is_enabled
    assert s.is_running


def test_node_exporter_socket(host):
    """Validate node_exporter socket."""
    s = host.socket("tcp://0.0.0.0:9100")

    assert s.is_listening
