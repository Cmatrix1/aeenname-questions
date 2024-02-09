import json
import requests
from constance import headers, cookies
from parsers import extract_questions, extract_exam_urls


def aeenname_data_generator(exam_list_url: str, session: requests.Session = None):
    session = session or requests.Session()

    response = session.get(exam_list_url)
    exam_urls = extract_exam_urls(response.content)
    for exam_url in exam_urls:
        response = session.get(exam_url)
        questions = extract_questions(response.content)
        yield questions


def main():
    session = requests.Session()
    session.headers.update(headers)
    session.cookies.update(cookies)

    data_generator = aeenname_data_generator('https://test-drive.ir/آزمون-های-اصلی-آیین-نامه-2/',
                                             session=session)

    data = {}
    for index, exam in enumerate(data_generator, start=1):
        if exam:
            data.update({index: exam})
            print(f"[+] Extract data. exam_index= {index} question_count= {len(exam)}")

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)



if __name__ == '__main__':
    main()