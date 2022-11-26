import requests as re
import datetime
import time # in case we need time.sleep()

base_url = "https://api.stackexchange.com/2.3/questions"

def GetTwoYearCount(tag, base_url="https://api.stackexchange.com/2.3/questions"):

    current_date = datetime.datetime.now(datetime.timezone.utc)
    two_years_ago = current_date - datetime.timedelta(days=730)
    cur_date = int(current_date.timestamp())
    tya = int(two_years_ago.timestamp())

    request_params = {
        "page": 1,
        "pagesize": 1,
        "fromdate": tya,
        "todate": cur_date,
        "order": "desc",
        "sort": "activity",
        "tagged": tag,
        "site": "stackoverflow",
        "filter": "!nKzQUR693x"
        
    }

    get_request = re.get(base_url, params=request_params)

    formatted_response = get_request.json()

    two_year_count = formatted_response['total']

    return two_year_count


def Get24HourCount(tag, base_url="https://api.stackexchange.com/2.3/questions"):

    current_date = datetime.datetime.now(datetime.timezone.utc)
    yesterday = current_date - datetime.timedelta(days=1)
    cur_date = int(current_date.timestamp())
    yd = int(yesterday.timestamp())

    request_params = {
        "page": 1,
        "pagesize": 1,
        "fromdate": yd,
        "todate": cur_date,
        "order": "desc",
        "sort": "activity",
        "tagged": tag,
        "site": "stackoverflow",
        "filter": "!nKzQUR693x"
        
    }

    get_request = re.get(base_url, params=request_params)

    formatted_response = get_request.json()

    today_count = formatted_response['total']

    return today_count

def GetWeekStats(tag: str, base_url: str) -> "list[dict]":

    now = datetime.datetime.now(datetime.timezone.utc)
    today = datetime.datetime(year=now.year, month=now.month, day=now.day)

    weekly_stats=[]
    quota=[]

    for i in range(0, 7):
        fromdate = today - datetime.timedelta(days=i+1)
        todate = today - datetime.timedelta(days=i)

        fromdate = int(fromdate.timestamp())
        todate = int(todate.timestamp())


        request_params = {
            "page": 1,
            "pagesize": 1,
            "fromdate": fromdate,
            "todate": todate,
            "order": "desc",
            "sort": "activity",
            "tagged": tag,
            "site": "stackoverflow",
            "filter": "!nKzQUR693x"
            
        }

        get_request = re.get(base_url, params=request_params)

        formatted_response = get_request.json()

        day_count = formatted_response['total']
        quota = [formatted_response['quota_max'], formatted_response['quota_remaining']]

        weekly_stats.append({
            "date": fromdate,
            "question_count": day_count
        })

    # keep an eye on quota
    weekly_stats.append({
        "quota_max": quota[0],
        "quota_remaining": quota[1]
    })

    return weekly_stats
    

def GetStackOverflowStats():
    pass

if __name__ == "__main__":
    # print(GetTwoYearCount("python", base_url))

    print(GetWeekStats("python", base_url))