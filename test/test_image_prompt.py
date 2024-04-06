# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fooocusapi_client.models.image_prompt import ImagePrompt

class TestImagePrompt(unittest.TestCase):
    """ImagePrompt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImagePrompt:
        """Test ImagePrompt
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImagePrompt`
        """
        model = ImagePrompt()
        if include_optional:
            return ImagePrompt(
                cn_img = None,
                cn_stop = None,
                cn_weight = None,
                cn_type = 'ImagePrompt'
            )
        else:
            return ImagePrompt(
        )
        """

    def testImagePrompt(self):
        """Test ImagePrompt"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()