# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fooocusapi_client.models.cn_weight2 import CnWeight2

class TestCnWeight2(unittest.TestCase):
    """CnWeight2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CnWeight2:
        """Test CnWeight2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CnWeight2`
        """
        model = CnWeight2()
        if include_optional:
            return CnWeight2(
            )
        else:
            return CnWeight2(
        )
        """

    def testCnWeight2(self):
        """Test CnWeight2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()