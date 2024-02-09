from bs4 import BeautifulSoup
from collections.abc import Generator

def extract_option_attributes(option_html: BeautifulSoup) -> dict:
    return {
        'lable': option_html.text.strip('\n').split('\n')[0].strip(),
        'is_correct': bool(int(option_html.find('input')['value']))
    }


def extract_question_attributes(question_html: BeautifulSoup) -> dict:
    options = []
    for order, option_html in enumerate(question_html.find_all(attrs={'class': 'hdq_row'})):
        option_data = extract_option_attributes(option_html)
        option_data.update(order=order + 1)
        options.append(option_data)

    return {
        'text': question_html.find('h3').text.replace('\n', ''),
        'img': question_html.find('img')['src'],
        'options': options
    }


def extract_questions(html: bytes) -> list[dict]:
    soup = BeautifulSoup(html, 'html.parser')
    questions = soup.find_all(attrs={'class': 'hdq_question'})
    return [
        extract_question_attributes(question)
        for question in questions
    ]


def extract_exam_urls(html: bytes) -> Generator[str]:
    soup = BeautifulSoup(html, 'html.parser')
    return (
        url['href'] for url in soup.find_all(attrs={'class': 'aio-icon-box-link'})
    )

