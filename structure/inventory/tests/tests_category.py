"""
API test case for category endpoint
"""
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from structure.inventory.models import Category
from structure.inventory.api.category_api import CategorySerializer
from structure.inventory.api.dependency_api import ProductTypeSerializer


class CategoryAPIBase(APITestCase):
    def create_category(self):
        payload = {"name": "Laptop", "slug": "laptop", "parent": ""}
        response = self.client.post("/api/v1/inventory/category/", data=payload)
        return response


class CategoryAPITestCase(CategoryAPIBase):
    def setUp(self):
        self.payload = {
            "name": "HP 51",
            "slug": "hp-51",
            "parent": self.create_category().data["id"],
        }

    def test_create_categoryLists(self):
        response = self.client.post("/api/v1/inventory/category/", data=self.payload)
        # check if the status code match
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # check if the comming data is equal to response data
        self.assertEqual(response.data["name"], "HP 51")

    def test_get_list_category(self):
        response = self.client.get("/api/v1/inventory/category/")
        # check if the status code match
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # check if the comming data is equal to response data
        self.assertIsInstance(response.data["results"], list)

    def test_get_single_category(self):
        product = self.create_category()
        idm = product.data["id"]
        print(idm)
        print(product.data)
        # response = self.client.get(reverse("c", kwargs={"pk": product.data["id"]}))
        response = self.client.get(
            "/api/v1/inventory/category/",
        )
        print(response.data["results"])
        # check if the status code match
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # check if the comming data is equal to response data
        # self.assertEqual(response.data,)
