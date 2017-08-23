from cauldron import steptest
from unittest.mock import patch
from unittest.mock import MagicMock
import cauldron as cd


class MockResponse:

    def __init__(self):
        self.text = 'a,b,user_id\n1,2,3\n1,2,3'


class TestExampleDataPull(steptest.StepTestCase):
    """Test suite for my notebook"""

    @patch('requests.get')
    def test_simple_run(self, requests_get: MagicMock):
        """Should run notebook step without error"""

        requests_get.return_value = MockResponse()

        self.run_step('S01-Pull.py')
        self.assertIsNotNone(cd.shared.df)
        self.assertEqual(2 * 26, len(cd.shared.df))
