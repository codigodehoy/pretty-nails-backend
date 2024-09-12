

class TestCategoryRoutes:

    def test_should_create_a_category(self, client, category):
        response = client.post("/category", json=category)
        status_code = response.status_code
        category_data = response.json()

        assert status_code == 200
        assert "id" in category_data
        assert "category_name" in category_data
