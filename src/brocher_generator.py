from IPython.display import display, Markdown, update_display
from src.prompts import user_prompt_For_URL, user_prompt_to_create_brocher, system_prompt, System_prompt_for_brocher
from src.scraper import fetch_website_links, fetch_website_contents
from src.llm import call_llm, call_llm_stream
import json

# Function to fetch all the links present in the URL along with the prompt
def list_of_url(url):
    user_prompt= user_prompt_For_URL.format(url=url)
    links = fetch_website_links(url)
    user_prompt += "\n".join(links)
    return user_prompt

# Fetching pages

def get_pages_and_relevant_links(url):
    Links = get_relevant_urls(url)
    Content = fetch_website_contents(url)
    result=f"\n\n ### Landing Page:\n\n{Content}\n ### Relevant Links:\n"
    for link in Links["Links"]:
        result += f"\n\n Link : {link["type"]}"
        result += fetch_website_contents(link["url"])
    return result


# User prompt

def brocher_prompt (company_name, url):
    user_prompt= user_prompt_to_create_brocher.format(company_name=company_name)
    user_prompt += get_pages_and_relevant_links(url)
    user_prompt = user_prompt[:5000]
    return user_prompt


def create_broucher(company_name, url):
    for partial_output in call_llm_stream(System_prompt_for_brocher, brocher_prompt(company_name, url), stream=True):
        yield partial_output

def get_relevant_urls(url):
    response= call_llm(system_prompt,list_of_url(url) ) 
    return json.loads(response)

