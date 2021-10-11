from typing import Type
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.test import APITestCase


class TestCourses(APITestCase):

    @classmethod
    def setUp(self) -> None:
        self.valid_data: dict = {
            "course_name": "Physics",
            "professor_name": "someone",
            "description": "School Sucks "
        }
        self.invalid_data: dict = {
            "course_name": "only course name is not enough."
        }

    def create_course(self) -> Response:
        return self.client.post(reverse("api:course-list"), self.valid_data)

    def test_course_can_be_added(self):
        res: Type[Response] = self.create_course()
        self.assertEqual(res.status_code, 201)

    def test_fail_if_incorrect_data(self):
        res: Type[Response] = self.client.post(reverse("api:course-list"), self.invalid_data)
        self.assertEqual(res.status_code, 400)

    def test_course_deletion(self):
        course: Type[ReturnDict] = self.create_course().data
        res: Type[Response] = self.client.delete(
                                reverse("api:course-detail", kwargs={'pk': course.get("id")}))
        self.assertEqual(res.status_code, 204)

    def test_update_course(self):
        course: Type[ReturnDict] = self.create_course().data
        new_course_name: str = "Updated course name"
        res: Type[Response] = self.client.patch(
            reverse("api:course-detail", kwargs={'pk': course.get("id")}),
            data={"course_name": new_course_name})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["course_name"], new_course_name)


class TestStudents(APITestCase):

    @classmethod
    def setUp(self):
        self.data: dict = {
            "student_name": "Somoene",
            "student_email": "kikouchia58@gmail.com",
            "phone_number": "1313123421342",
        }

    def add_student(self) -> Response:
        return self.client.post(reverse("api:student-list"), self.data)

    def test_student_can_be_added(self):
        res: Type[Response] = self.add_student()
        self.assertEqual(res.status_code, 201)

    def test_student_deletion(self):
        student: Type[ReturnDict] = self.add_student().data
        res: Type[Response] = self.client.delete(
                                reverse("api:student-detail", kwargs={'pk': student.get("id")}))
        self.assertEqual(res.status_code, 204)

    def test_student_info_can_be_updated(self):
        student: Type[ReturnDict] = self.add_student().data
        new_email: str = "new_email@gmail.com"
        res: Type[Response] = self.client.patch(
            reverse("api:student-detail", kwargs={'pk': student.get("id")}),
            {"student_email": new_email}
            )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["student_email"], new_email)