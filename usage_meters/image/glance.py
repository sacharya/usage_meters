#
# Copyright 2012 New Dream Network, LLC (DreamHost)
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""Common code for working with images
"""

from __future__ import absolute_import
from ceilometer.agent import plugin_base
from ceilometer import sample
from usage_meters.config import load


_CONFIG_FILE = '/etc/usage_meters/usage_meters.yaml'
_CONFIG = load(_CONFIG_FILE)
_STANDARD_KEYS = ['status', 'name', 'created_at', 'updated_at']
try:
    _METADATA_KEYS = _CONFIG['metadata_keys']
except KeyError:
    _METADATA_KEYS = []
    pass


class _Base(plugin_base.PollsterBase):

    # For ease of testing without mock
    STANDARD_KEYS = _STANDARD_KEYS
    METADATA_KEYS = _METADATA_KEYS

    @property
    def default_discovery(self):
        return 'images'

    @classmethod
    def extract_image_metadata(cls, image):
        meta = dict((k, getattr(image, k)) for k in cls.STANDARD_KEYS)
        meta.update(
            dict(('properties.{}'.format(k), getattr(image, k, ''))
            for k in cls.METADATA_KEYS)
        )
        return meta


class ImageSizePollster(_Base):
    def get_samples(self, manager, cache, resources):
        for image in resources:
            yield sample.Sample(
                name='image.size.custom',
                type=sample.TYPE_GAUGE,
                unit='B',
                volume=image.size,
                user_id=None,
                project_id=image.owner,
                resource_id=image.id,
                resource_metadata=self.extract_image_metadata(image),
            )
