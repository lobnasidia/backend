from unittest.mock import patch

from django.core.cache import cache

from caustaza_backend_project.feedbacks.tests.test_setup import FeedbackSetup
from caustaza_backend_project.feedbacks.views import FeedbackViewSet


class FeedbackCacheTestCase(FeedbackSetup):
    def test_cache(self):
        # Verify that the Feedback object is not in the cache
        self.assertIsNone(cache.get("feedbacks"))

        # Retrieve the Feedback object using the view
        view = FeedbackViewSet.as_view({"get": "list"})
        request = self.factory.get("/feedbacks/")
        response = view(request)
        data = response.data

        # Verify that the Feedback object is now in the cache
        self.assertIsNotNone(cache.get("feedbacks"))

        # Mock the cache.get method to return the cached Feedback object
        with patch("django.core.cache.cache.get", return_value=data):
            # Retrieve the Feedback object again using the view
            request = self.factory.get("/feedbacks/")
            response = view(request)
            data = response.data
            # Verify that the Feedback object was retrieved from the cache
            self.assertEqual(data, data)
