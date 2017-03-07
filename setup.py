from setuptools import setup
from usage_meters.meta import version
from usage_meters.meta import description

entry_points = {
    'ceilometer.poll.central': [
        'image.size.custom = usage_meters.image.glance:ImageSizePollster',
        'storage.containers.objects.size.custom = usage_meters.objectstore.swift:ContainersSizePollster'
    ]
}

setup(
    name="usage_meters",
    version=version,
    author="james absalon",
    author_email="james.absalon@rackspace.com",
    packages=[
        'usage_meters',
        'usage_meters.image',
        'usage_meters.objectstore'
    ],
    entry_points=entry_points,
    long_description=description
)
