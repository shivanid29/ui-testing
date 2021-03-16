import pytest
from Pages.DomainPage import PurchaseDomain
from Base.BasePage import Base


@pytest.mark.usefixtures('setup')
class TestDomain(Base):
    def test_addingdomain(self):
        driver = self.driver
        Adding = PurchaseDomain(driver)
        Adding.enter_the_domain_name()
