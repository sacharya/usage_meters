import unittest

from usage_meters.image.glance import ImageSizePollster

fake_config = {
    'metadata_keys': [
        'meta_1',
        'meta_2',
        'meta_3'
    ]
}


class TestImageSizePollster(unittest.TestCase):
    def test_metadata_standard(self):

        class FakeImage(object):
            status = 'status'
            name = 'name'
            created_at = 'created_at'
            updated_at = 'updated_at'
            nonstandard = 'nonstandard'
            meta_1 = 'meta_1'
            meta_2 = 'meta_2'
            nonmeta = 'nonmeta'


        ImageSizePollster.STANDARD_KEYS = [
            'status',
            'name',
            'created_at',
            'updated_at',
        ]
        ImageSizePollster.METADATA_KEYS = [
            'meta_1',
            'meta_2'
        ]
        meta = ImageSizePollster.extract_image_metadata(FakeImage())
        self.assertFalse('nonstandard' in meta)
        self.assertFalse('properties.nonmeta' in meta)
        for s in ImageSizePollster.STANDARD_KEYS:
            self.assertEquals(s, meta[s])
        for o in ImageSizePollster.METADATA_KEYS:
            self.assertEquals(o, meta['properties.{}'.format(o)])
