# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fooocusapi_client.models.text2_img_request import Text2ImgRequest

class TestText2ImgRequest(unittest.TestCase):
    """Text2ImgRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Text2ImgRequest:
        """Test Text2ImgRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Text2ImgRequest`
        """
        model = Text2ImgRequest()
        if include_optional:
            return Text2ImgRequest(
                prompt = '',
                negative_prompt = '',
                style_selections = [
                    ''
                    ],
                performance_selection = 'Speed',
                aspect_ratios_selection = '1152*896',
                image_number = 1.0,
                image_seed = 56,
                sharpness = 0.0,
                guidance_scale = 1.0,
                base_model_name = 'juggernautXL_version6Rundiffusion.safetensors',
                refiner_model_name = 'None',
                refiner_switch = 0.1,
                loras = [
                    fooocusapi_client.models.lora.Lora(
                        model_name = '', 
                        weight = -2.0, )
                    ],
                advanced_params = None,
                require_base64 = True,
                async_process = True,
                webhook_url = None
            )
        else:
            return Text2ImgRequest(
        )
        """

    def testText2ImgRequest(self):
        """Test Text2ImgRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
