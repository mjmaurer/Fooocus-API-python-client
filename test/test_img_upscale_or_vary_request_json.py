# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fooocusapi_client.models.img_upscale_or_vary_request_json import ImgUpscaleOrVaryRequestJson

class TestImgUpscaleOrVaryRequestJson(unittest.TestCase):
    """ImgUpscaleOrVaryRequestJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImgUpscaleOrVaryRequestJson:
        """Test ImgUpscaleOrVaryRequestJson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImgUpscaleOrVaryRequestJson`
        """
        model = ImgUpscaleOrVaryRequestJson()
        if include_optional:
            return ImgUpscaleOrVaryRequestJson(
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
                webhook_url = None,
                uov_method = 'Vary (Subtle)',
                upscale_value = None,
                input_image = '',
                image_prompts = [
                    null
                    ]
            )
        else:
            return ImgUpscaleOrVaryRequestJson(
                input_image = '',
        )
        """

    def testImgUpscaleOrVaryRequestJson(self):
        """Test ImgUpscaleOrVaryRequestJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
