import base_page as BasePage
import time
import locators



def MoveToAutomation(waitDriver, key_value_dict, uniqueKey):

    # Start Entering Data in the fields.
    BasePage.enterValueInGivenField(
        locators.RPAChallenge.FirstName,
        key_value_dict,
        uniqueKey,
        "First Name",
        waitDriver,
    )

    BasePage.enterValueInGivenField(
        locators.RPAChallenge.LastName,
        key_value_dict,
        uniqueKey,
        "Last Name",
        waitDriver,
    )

    BasePage.enterValueInGivenField(
        locators.RPAChallenge.CompanyName,
        key_value_dict,
        uniqueKey,
        "Company Name",
        waitDriver,
    )

    BasePage.enterValueInGivenField(
        locators.RPAChallenge.RoleInCompany,
        key_value_dict,
        uniqueKey,
        "Role in Company",
        waitDriver,
    )

    BasePage.enterValueInGivenField(
        locators.RPAChallenge.Address, key_value_dict, uniqueKey, "Address", waitDriver
    )

    BasePage.enterValueInGivenField(
        locators.RPAChallenge.Email, key_value_dict, uniqueKey, "Email", waitDriver
    )

    BasePage.enterValueInGivenField(
        locators.RPAChallenge.PhoneNumber,
        key_value_dict,
        uniqueKey,
        "Phone Number",
        waitDriver,
    )

    submit = BasePage.findElementByXpath(waitDriver, locators.RPAChallenge.click)

    submit.click()
    time.sleep(1)

    