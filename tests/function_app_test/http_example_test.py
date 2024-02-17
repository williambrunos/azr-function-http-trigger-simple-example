import unittest
import azure.functions as func

from ...function_app import HttpExample

class TestFunction(unittest.TestCase):
  def test_my_second_function(self):
    # Construct a mock HTTP request.
    req = func.HttpRequest(method='GET',
                           body=None,
                           url='localhost:7071/api/HttpExample',
                           params={'name': 'william'})
    # Call the function.
    func_call = HttpExample.build().get_user_function()
    resp = func_call(req)
    # Check the output.
    self.assertEqual(
        resp.status_code,
        200,
    )