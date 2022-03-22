from pprint import pprint

import requests


if __name__ == '__main__':
    response = requests.get("https://api.stackexchange.com//2.3/questions",
        params={"fromdate": "1647734400",
            "todate": "1647907200",
            "order": "desc",
            "sort": "activity",
            "tagged": "python",
            "site": "stackoverflow"}
    )
    response.raise_for_status()
    data = response.json()
    # pprint(data)
    # print(len(data["items"]))
    questions = data["items"]
    for question in questions:
        print(f'{question["title"]}\n')



