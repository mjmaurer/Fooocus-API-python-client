# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fooocusapi_client.models.cn_weight3 import CnWeight3

class TestCnWeight3(unittest.TestCase):
    """CnWeight3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CnWeight3:
        """Test CnWeight3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CnWeight3`
        """
        model = CnWeight3()
        if include_optional:
            return CnWeight3(
            )
        else:
            return CnWeight3(
        )
        """

    def testCnWeight3(self):
        """Test CnWeight3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
