from rest_framework import status

from caustaza_backend_project.feedbacks.tests.test_setup import FeedbackSetup


class TestViews(FeedbackSetup):
    """Test views for Feedback app."""

    def test_feedback_page(self):
        """Test that the feedback page APIs are working with the correct data."""

        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data[0]["form"], "Feedback")
        self.assertEqual(response.data[0]["designation"], "This is the about page subtitle.")
        self.assertEqual(response.data[0]["quote"], "This is the about page description.")
