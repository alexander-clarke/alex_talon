from talon import Context, Module

mod = Module()
mod.apps.k9s = r"""
win.title: /k9s/i
"""

ctx = Context()
ctx.matches = r"""
app: k9s
"""
ctx.lists["user.kubectl_object"] = {
    "pod": "pod",
    "namespace": "namespace",
    "node": "node",
    "deployment": "deployment",
    "service": "service",
    "daemon set": "daemonset",
    "replica set": "replicaset",
    "stateful set": "statefulset",
    "job": "job",
    "event": "event",
    "config map": "configmap",
    "secret": "secret",
    "ingress": "ingress",
    "persistent volume": "persistentvolume",
    "persistent volume claim": "persistentvolumeclaim",
    "context": "ctx",
}
