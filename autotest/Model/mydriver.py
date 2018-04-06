from jbhautotest.UIautotest.Model.Model import Basicmodel
from jbhautotest.UIautotest.Data.basicdate import basicconfig


def driver():
    driver = Basicmodel(basicconfig.driver_name)
    return driver

if __name__ == '__main__':
    dr = driver()