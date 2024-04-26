from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from caustaza_backend_project.feedbacks.models import Feedback


class FeedbackSetup(APITestCase):
    def setUp(self):
        self.index_url = reverse("api:feedbacks-list")
        self.client = APIClient()
        self.factory = APIRequestFactory()

        self.feedback = Feedback.objects.create(
            form="Feedback",
            designation="This is the about page subtitle.",
            quote="This is the about page description.",
            image="path_to_image",
        )
        self.feedback.save()

    def tearDown(self):
        return super().tearDown()
