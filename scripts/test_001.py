import allure


class Test_001:
    @allure.step("这是一个项目")
    def test_001(self):
        print("---test_001")
        allure.attach("文件", "test_001")
        assert True
