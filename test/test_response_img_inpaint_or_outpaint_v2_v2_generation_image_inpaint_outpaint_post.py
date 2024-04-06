# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fooocusapi_client.models.response_img_inpaint_or_outpaint_v2_v2_generation_image_inpaint_outpaint_post import ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost

class TestResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost(unittest.TestCase):
    """ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost:
        """Test ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost`
        """
        model = ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost()
        if include_optional:
            return ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost(
                job_id = None,
                job_type = 'Text to Image',
                job_stage = 'WAITING',
                job_progress = None,
                job_status = None,
                job_step_preview = None,
                job_result = None
            )
        else:
            return ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost(
                job_id = None,
                job_type = 'Text to Image',
                job_stage = 'WAITING',
                job_progress = None,
        )
        """

    def testResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost(self):
        """Test ResponseImgInpaintOrOutpaintV2V2GenerationImageInpaintOutpaintPost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
