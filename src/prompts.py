system_prompt="""
- You are provied with a list of the links found on a webpage.
- You are able to decide which of the links would be most relevant to include in a brochure about the company, such
as links to about us page, or a career/job page.
- You should respond in JSON format as shown in below example.
{
    "Links":[{"type":"about page", "url":"https://full.url/about"}]
}
"""

user_prompt_For_URL= """
    Here is the list of the links on the website {url}
    You need to decide which of these are relevent to creater company brochure, and you respond with full https URL in JSON format.
    Dont include Terms of service, T&C, Privacy, email links.
    """

System_prompt_for_brocher="""
- You are an assistant that analyse the contents of several relevnt pages from a company website and
create a short broucher about the company for prospective customers, investors and recruits.
- You respond in markdown without code blocks.
- You inclde details of company culture, customers and career/jobs if you have the information
"""

user_prompt_to_create_brocher="""
- Your are looking at a company called {company_name}
- Here are the contents of its landing page and other relevant pages.
- You can use this information to build a short broucher of the company in MARKDOWN without code blocks. \n\n
"""