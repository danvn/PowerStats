from keen.client import KeenClient
import sportsRadar
import json

client = KeenClient(
    project_id="5ad53b33c9e77c00017c7f18",
    write_key="C45BD93F638CE4332874AE2F2DC375431A3BB79553C9FAA30BBD527356185170238BBF1F1E121A29FDD71EF1FE8AEB19CC3C5F792F0330AABB536D56B082EFABE2432C5AB9D66AF4E8AA9BD68DC3F7DA79C35E037A495E8A7B07240915109298",
    read_key="1E750240E2DC88FEC6AE0927C57A3152BF578C59D825A9FB9BAD96E230E8B0886C722FDD31852ED880058CF752C30D7D6EBAD67E968FA093E543BB70F9A03C84FFEC6DC76139B0C3AC9F208FC49818A557E1FCC906063DAC87551EFAF9758BA7"
)

# player = sportsRadar.getPlayerProfile("a52b2c84-9c3d-4d6e-8a3b-10e75d11c2bc")
# playerEventCollection = sportsRadar.getSeasonAverages(player)
#
# client.add_events({
#   "JamesHarden_Season_Averages": playerEventCollection
# })

with open('data/AllTeamsBoxScore_short3.json') as json_data:
    d = json.load(json_data)


client.add_events({
  "All_Players_Box_Scores_17_18": d
})
