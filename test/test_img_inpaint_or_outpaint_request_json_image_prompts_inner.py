# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fooocusapi_client.models.img_inpaint_or_outpaint_request_json_image_prompts_inner import ImgInpaintOrOutpaintRequestJsonImagePromptsInner

class TestImgInpaintOrOutpaintRequestJsonImagePromptsInner(unittest.TestCase):
    """ImgInpaintOrOutpaintRequestJsonImagePromptsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImgInpaintOrOutpaintRequestJsonImagePromptsInner:
        """Test ImgInpaintOrOutpaintRequestJsonImagePromptsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImgInpaintOrOutpaintRequestJsonImagePromptsInner`
        """
        model = ImgInpaintOrOutpaintRequestJsonImagePromptsInner()
        if include_optional:
            return ImgInpaintOrOutpaintRequestJsonImagePromptsInner(
                cn_img = None,
                cn_stop = None,
                cn_weight = None,
                cn_type = 'ImagePrompt'
            )
        else:
            return ImgInpaintOrOutpaintRequestJsonImagePromptsInner(
        )
        """

    def testImgInpaintOrOutpaintRequestJsonImagePromptsInner(self):
        """Test ImgInpaintOrOutpaintRequestJsonImagePromptsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
