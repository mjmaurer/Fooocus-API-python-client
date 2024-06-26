# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fooocusapi_client.models.async_job_response import AsyncJobResponse

class TestAsyncJobResponse(unittest.TestCase):
    """AsyncJobResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AsyncJobResponse:
        """Test AsyncJobResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AsyncJobResponse`
        """
        model = AsyncJobResponse()
        if include_optional:
            return AsyncJobResponse(
                job_id = '',
                job_type = 'Text to Image',
                job_stage = 'WAITING',
                job_progress = 56,
                job_status = None,
                job_step_preview = None,
                job_result = None
            )
        else:
            return AsyncJobResponse(
                job_id = '',
                job_type = 'Text to Image',
                job_stage = 'WAITING',
                job_progress = 56,
        )
        """

    def testAsyncJobResponse(self):
        """Test AsyncJobResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
