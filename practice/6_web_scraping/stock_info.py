"""
There is a list of most active Stocks on Yahoo Finance https://finance.yahoo.com/most-active.
You need to compose several sheets based on data about companies from this list.
To fetch data from webpage you can use requests lib. To parse html you can use beautiful soup lib or lxml.
Sheets which are needed:
1. 5 stocks with most youngest CEOs and print sheet to output. You can find CEO info in Profile tab of concrete stock.
    Sheet's fields: Name, Code, Country, Employees, CEO Name, CEO Year Born.
2. 10 stocks with best 52-Week Change. 52-Week Change placed on Statistics tab.
    Sheet's fields: Name, Code, 52-Week Change, Total Cash
3. 10 largest holds of Blackrock Inc. You can find related info on the Holders tab.
    Blackrock Inc is an investment management corporation.
    Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
    All fields except first two should be taken from Holders tab.


Example for the first sheet (you need to use same sheet format):
==================================== 5 stocks with most youngest CEOs ===================================
| Name        | Code | Country       | Employees | CEO Name                             | CEO Year Born |
---------------------------------------------------------------------------------------------------------
| Pfizer Inc. | PFE  | United States | 78500     | Dr. Albert Bourla D.V.M., DVM, Ph.D. | 1962          |
...

About sheet format:
- sheet title should be aligned to center
- all columns should be aligned to the left
- empty line after sheet

Write at least 2 tests on your choose.
Links:
    - requests docs: https://docs.python-requests.org/en/latest/
    - beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - lxml docs: https://lxml.de/
"""

import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re, pytest


def sheet_creator(title: str, data: dict):
    # lenghts of every column
    col_lens = []
    for col in data:
        col_lens.append(max(max([len(el) for el in data[col]]), len(col)))
    # full lenghth of one row
    full_len = sum(col_lens) + 3*len(col_lens) + 1
    top_frame = '=' * int((full_len - len(title) - 2)/2)
    # printing title
    print(top_frame, title, top_frame)
    # printing header
    for col in range(len(data.keys())):
        print('| ' + list(data.keys())
              [col] + ' '*(col_lens[col]-len(list(data.keys())[col])), end=' ')
    print('|\n' + '-' * full_len)
    # printing rows
    for i in range(len(data[list(data.keys())[0]])):
        for j, key in enumerate(data):
            print('| ' + data[key][i] + ' ' *
                  (col_lens[j]-len(data[key][i])), end=' ')
        print('|')


def get_max_cols(data: dict, column: str, num: int, title : str):
    # converting to int
    converted_list = [
        float(el) if el != 'N/A' else 0 for el in data[column]]
    max_ind = converted_list.index(min(converted_list))
    top_num_indices = []
    # creating list of indices of the 5 youngest
    for _ in range(num):
        for i in range(25):
            if converted_list[i] > converted_list[max_ind]:
                max_ind = i
        top_num_indices.append(max_ind)
        converted_list[max_ind] = 0
    # output dictionary
    table = dict()
    for key in data:
        table[key] = []
        for ind in top_num_indices:
            table[key].append(data[key][ind])
    sheet_creator(title, table)
    return table

def name_and_code_filler(data : dict, company : object, subsite :str):
    # adding names and code to output data
        data["Name"].append(company.find("td", {"aria-label": "Name"}).text)
        data["Code"].append(company.find("td", {"aria-label": "Symbol"}).text)

        # creating bs4 object for subsite
        url_suffix = company.find("a")["href"]
        profile_url = "https://finance.yahoo.com" + \
            url_suffix[:url_suffix.index('?')] + subsite
        session2 = HTMLSession()
        comp_page = session2.get(profile_url)
        comp_soup = BeautifulSoup(comp_page.content, "html.parser")
        return comp_soup


def first_task(companies):
    # first sheet
    # creating dict with data
    data = dict()
    data = data.fromkeys(
        ["Name", "Code", "Country", "Employees", "CEO Name", "CEO Year Born"])
    for key in data:
        data[key] = []
    for company in companies:
        comp_soup = name_and_code_filler(data, company, "/profile")
        comp_results_country = comp_soup.find(
            "p", class_="D(ib) W(47.727%) Pend(40px)")
        if comp_results_country == None:
            data["CEO Year Born"].append('0')
            continue
        string_list = str(comp_results_country).split("<br/>")
        country = string_list[len(string_list)-3]
        data["Country"].append(country)

        # employees
        comp_results_emp = comp_soup.find_all("span", class_="Fw(600)")
        employees = comp_results_emp[2].text
        data["Employees"].append(employees)

        # ceo
        executives = comp_soup.find("table", class_="W(100%)")
        ceo = executives.find("td", string=re.compile("CEO"))
        try:
            ceo_name = [*ceo.parent.children][0].text
            ceo_year = [*ceo.parent.children][4].text
        except AttributeError:
            ceo_name = "N/A"
            ceo_year = "N/A"
        data["CEO Name"].append(ceo_name)
        data["CEO Year Born"].append(ceo_year)
    get_max_cols(data, "CEO Year Born", 5, "5 stocks with most youngest CEOs")


def second_task(companies):
    data = dict()
    data = data.fromkeys(
        # I have decided to change "52-Week Change" for "52-Week High"
        # because of the site protection system
        ["Name", "Code", "52-Week High", "Total Cash"])
    for key in data:
        data[key] = []
    for company in companies:
        comp_soup = name_and_code_filler(data, company, "/key-statistics")
        comp_lines = comp_soup.find_all("tr", class_="Bxz(bb) H(36px) BdB Bdbc($seperatorColor)")
        week_high= comp_lines[2].text[14:]
        data["52-Week High"].append(week_high.replace(',',''))

        #total cash
        comp_lines2 = comp_soup.find("span", string="Total Cash").parent.parent
        total_cash = comp_lines2.text[16:]
        data["Total Cash"].append(total_cash)
    get_max_cols(data, "52-Week High", 10, "10 stocks with best 52-Week Change")
    
def third_task(companies):
    data = dict()
    data = data.fromkeys(
        ["Name", "Code", "Shares", "Date Reported", "% Out", "Value"])
    for key in data:
        data[key] = []

    for company in companies:
        comp_soup = name_and_code_filler(data, company, "/holders")
        try:
            comp_data = comp_soup.find("td", string="Blackrock Inc.").parent.children
        except AttributeError:
            data["Shares"].append("N/A")
            data["Date Reported"].append("N/A")
            data["% Out"].append("N/A")
            data["Value"].append("N/A")
            continue
        comp_list = [*comp_data]
        data["Shares"].append(comp_list[1].text)
        data["Date Reported"].append(comp_list[2].text)
        data["% Out"].append(comp_list[3].text)
        data["Value"].append(comp_list[4].text.replace(',',''))
    get_max_cols(data, "Value", 10, "10 largest holds of Blackrock Inc.")
    


if __name__ == "__main__":
    # connecting to url
    url = f"https://finance.yahoo.com/most-active"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find("div", id="scr-res-table")
    companies = results.find_all("tr", class_="simpTblRow")
    first_task(companies)
    print("\n")
    second_task(companies)
    print("\n")
    third_task(companies)

