from unittest.mock import MagicMock

from pykube.objects import NamespacedAPIObject

from pykube import Deployment, StatefulSet
from kube_downscaler.resources.stack import Stack


def test_deployment():
    api_mock = MagicMock(spec=NamespacedAPIObject, name="APIMock")
    scalable_mock = {"spec": {"replicas": 3}}
    api_mock.obj = MagicMock(name="APIObjMock")
    d = Deployment(api_mock, scalable_mock)
    r = d.replicas
    assert r == 3

    d.replicas = 10
    assert scalable_mock["spec"]["replicas"] == 10


def test_statefulset():
    api_mock = MagicMock(spec=NamespacedAPIObject, name="APIMock")
    scalable_mock = {"spec": {"replicas": 3}}
    api_mock.obj = MagicMock(name="APIObjMock")
    d = StatefulSet(api_mock, scalable_mock)
    r = d.replicas
    assert r == 3
    d.replicas = 10
    assert scalable_mock["spec"]["replicas"] == 10


def test_stack():
    api_mock = MagicMock(spec=NamespacedAPIObject, name="APIMock")
    scalable_mock = {"spec": {"replicas": 3}}
    api_mock.obj = MagicMock(name="APIObjMock")
    d = Stack(api_mock, scalable_mock)
    r = d.replicas
    assert r == 3
    d.replicas = 10
    assert scalable_mock["spec"]["replicas"] == 10
