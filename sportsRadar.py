import http.client
import sys, json
import requests
from collections import Counter

url = 'https://api.sportradar.us//nba/trial/v4/en/players/0afbe608-940a-4d5d-a1f7-468718c67d91/profile.json?api_key=ujyv72ke4uas2mdvwq6h7tjp'
apiKey = "?api_key=ujyv72ke4uas2mdvwq6h7tjp"
baseURL = "https://api.sportradar.us//nba/trial/v4/en/players/"

def getPlayerProfile(playerID):
    requestType = "/profile.json"
    requestBody = baseURL + playerID + requestType + apiKey
    response = requests.get(requestBody)
    data = response.json()
    # We want to use dataStr for uploading a valid JSON object to Keen
    # We want a dict to manipulate objects in Python
    dataStr = json.dumps(data)
    dataDict = json.loads(response.content.decode('utf-8'))
    # data2 = json.dumps(dataDict)
    print("Retrieving player profile for " + dataDict["first_name"], dataDict["last_name"])
    # print(type(data))
    return dataStr, dataDict

def getSeasonTotals(playerProfile):
    # Method for combining stats when players have multiple teams in a season
    seasonTotals = []

    # for season in playerProfile["seasons"]:
    #     seasonSummary = {}
    #     seasonSummary.update({
    #         # Add a random string to make the year an iso standard datetime
    #         "keen":{
    #             "timestamp": str(season["year"]) + "-04-12T19:10:39.205Z"
    #         }
    #     })
    #     # Create a holder counter to add stats for players that get traded
    #     sumOfStats = Counter({})
    #     for team in season["teams"]:
    #         sumOfStats = sumOfStats + Counter(team["total"])
    #     sumOfStats = dict(sumOfStats)
    #     seasonSummary.update(sumOfStats)
    #     seasonTotals.append(seasonSummary)

    print(seasonTotals)
    return seasonTotals

def getSeasonAverages(playerProfile):
    seasonAverages = []
    for season in playerProfile[1]['seasons']:
        seasonSummary = {}
        seasonSummary.update({
            # Add a random string to make the year an iso standard datetime
            "keen":{
                "timestamp": str(season["year"]) + "-04-12T19:10:39.205Z"
            }
        })
        seasonSummary.update(season["teams"][-1]["average"])
        seasonAverages.append(seasonSummary)
    print(seasonAverages)
    return seasonAverages

#
# harden = getPlayerProfile("a52b2c84-9c3d-4d6e-8a3b-10e75d11c2bc")
# a = getSeasonAverages(harden)
