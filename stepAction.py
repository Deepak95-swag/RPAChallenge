# Import Modules
import read_Excel
import browsersSetUp
import automationSteps
import base_page as BasePage
import locators
from datetime import datetime


# Start the RPA Challenge Automation.
class rpaChallengeAutomation:
    def __init__(self):
        print("Start Automation")
        self.runAutomation()

    def runAutomation(self):
        print("Run Automation")

        #  Initialise Log sheet
        workbook, sheet_name, sheet, excel_file_path = BasePage.workBookconfig()

        # If the sheet is just created, write headers to cells A1,B1 & C1.
        if sheet.max_row == 1:
            sheet["A1"] = "UniqueKey"
            sheet["B1"] = "Status"
            sheet["C1"] = "TimeStamp"

        # log_info(log_info)
        key_value_dict, alistofkeycolumn = read_Excel.ReadExcel()

        driver, waitDriver, actiondriver, waitdriverForLogin, waitdriverForReport = (
            browsersSetUp.setUpBrowser()
        )
        clickStart = BasePage.findElementByXpath(
            waitDriver, locators.RPAChallenge.start
        )
        clickStart.click()

        # Find the next available row
        
        for uniqueKey in alistofkeycolumn:
            next_row = sheet.max_row + 1

            try:
                automationSteps.MoveToAutomation(waitDriver, key_value_dict, uniqueKey)

                # Write uniqueKey, Status & timeStamp in A1, B1, C1
                sheet.cell(row=next_row, column=1, value=uniqueKey)
                sheet.cell(row=next_row, column=2, value="Success")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                sheet.cell(row=next_row, column=3, value=timestamp)

            except Exception as e:
                
                # Write uniqueKey, Status & timeStamp in A1, B1, C1
                sheet.cell(row=next_row, column=1, value=uniqueKey)
                sheet.cell(row=next_row, column=2, value="Fail")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                sheet.cell(row=next_row, column=3, value=timestamp)

        workbook.save(excel_file_path)