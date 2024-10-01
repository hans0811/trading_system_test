


account: william, 周杰伦
password: 1234abcd!
invitecode: !@1w2i3l4l5i6a7m8#$


### Pytest

``
pytest ./testcase/test_pytest_m.py::TestPytestMClass::test_open_baidu


pytest -m test001
pytest -m "test001 or test002" 
pytest -m "test001 and test002" 
pytest -m "not test001"
pytest testcase/test_pytest_m.py -m "not test001"
pytest -k open
pytest -s -m -v baidu
pytest --collect-only

Pytest Assert
==, !=, <. >, >=, <=
``


### Fixture

``
    @pytest.fixture()
    def driver(self):
        get_driver = DriverConfig().driver_config()
        return get_driver
``
``
    @pytest.mark.test001
    def test_open_bing(self, driver):
        # driver = DriverConfig().driver_config()
        driver.get("https://google.com")
        sleep(3)
``
- session
- class
- module
- function(default)

### conftest.py

Find closet conftest.py
pytest -s -q ./testcase/my_conftest/test_add_goods.py


### pytest-xdist

Install pytest-xdist

````
pytest -n 3 

pytest -n auto

pytest -n auto --dist=loadscope

`````


### pytest-rerunfailures

pytest ./testcase/test_rerun.py --reruns 5 --reruns-delay 1

@pytest.mark.flaky(reruns=5, reruns_delay=1)


### pytest-assume


### pytest-html

````
pytest -s -q ./testcase/test_switch_window_handle.py --html=report.html --self-contained-html
````


### aircv
````
pip install aircv==1.4.6
pip install opencv-python==4.1.0.25
pip install opencv-python==4.10.0.84
````


### Allure

````
docker pull frankescobar/allure-docker-service

docker run -d \
    -p 4040:4040 \
    -v /Users/hans/Desktop/code/python/automation/imooc_pytest/trading_system_test/UIreport:/app/allure-results \
    --name=allure-server frankescobar/allure-docker-service
    
pip install allure-pytest

pytest ./testcase/test_switch_window_handle.py --alluredir=UIreport

allure generate UIreport -o UIreport/report

allure servert UIreport
````

### Jenkins

````
docker pull jenkins/jenkins:lts

docker volume create jenkins-data

docker run -d \
    --name jenkins \
    -p 8080:8080 -p 50000:50000 \
    -v jenkins-data:/var/jenkins_home \
    jenkins/jenkins:lts
    
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
````

### GIT

git config --global http.postBuffer 524288000