#apex legends tracker

import requests

#user_ID = (print"Please Enter your PSN/XBOX/Switch/PC Account Name: ")
user_ID = input("What is the users ID?: ")

#user_platform = (print"Please Enter your Platform (PS4,X1,PC): ")
user_platform = input("What is the users platform? (For Xbox:X1, PS5/4:PS4, PC:PC): ")

#api url
base_url = ("https://api.mozambiquehe.re/")

#api key
headers = {"Authorization": "apikeyhere"}

#searching for a name
name = requests.get(base_url + f"bridge?player={user_ID}&platform={user_platform}", headers = headers)

#accesing the content 
name_content = name.text
#print(name_content)      #print this when you need to inspect the raw data prior to being grouped to its respective place

print("All Stats Below will relate to the Legend of which the user has equipped!!.")

#name and platform from the beginning 
keywords_to_search = ["name", "platform",]
print("_________________Name and Platform_________________")
for keyword in keywords_to_search:
        if keyword in name_content:
            index = name_content.index(keyword)
            value_start = name_content.index(":", index) + 1
            value_end = name_content.index(",", value_start)
            value = name_content[value_start:value_end].strip('"\n ')
            print(f"{keyword}: {value}")



#main stats 
keywords_to_search2 = ["Account Level","level","rankName","toNextLevelPercent","rankScore",
                       "BR Damage","BR Wins","BR Kills","BR Games played","BR Headshots","BR Revives",
                       "selectedLegend","gameInfo"]
print("_________________Main Stats_________________")
for keyword in keywords_to_search2:
        if keyword in name_content:
            index = name_content.index(keyword)
            value_start = name_content.index(":", index) + 1
            value_end = name_content.index(",", value_start)
            value = name_content[value_start:value_end].strip('"\n ')
            print(f"{keyword}: {value}")

#Kills
keywords_to_search3 = [f"Season {k} kills" for k in range (0,20)]
print("_________________Seasonal Kills_________________")
for keyword in keywords_to_search3:
        if keyword in name_content:
            index = name_content.index(keyword)
            value_start = name_content.index(":", index) + 1
            value_end = name_content.index(",", value_start)
            value = name_content[value_start:value_end].strip('"\n ')
            print(f"{keyword}: {value}")

#Wins
keywords_to_search4 = [f"BR Season {w} Wins" and f"BR Season {w} wins" for w in range(0,20)]
print("_________________Seasonal Wins_________________")
for keyword in keywords_to_search4:
      if keyword in name_content:
            index = name_content.index(keyword)
            value_start = name_content.index(":", index) + 1
            value_end = name_content.index(",", value_start)
            value = name_content[value_start:value_end].strip('"\n ')
            print(f"{keyword}: {value}")

#ar kills
keywords_to_search5 = ["Nemesis Burst AR Kills","R-301 Kills","Hemlok Kills","Flatline Kills","Havoc Kills","AR kills"]
print("_________________AR Kills Counter_________________")
for keyword in keywords_to_search5:
      if keyword in name_content:
            index = name_content.index(keyword)
            value_start = name_content.index(":", index) + 1
            value_end = name_content.index(",", value_start)
            value = name_content[value_start:value_end].strip('"\n ')
            print(f"{keyword}: {value}")

#smg kills
keywords_to_search6 = ["Alternator Kills","Prowler Kills","R99 Kills","Volt Kills","Car Kills","BR SMG kills"]
print("_________________SMG Kills Counter_________________")
for keyword in keywords_to_search6:
      if keyword in name_content:
            index = name_content.index(keyword)
            value_start = name_content.index(":", index) + 1
            value_end = name_content.index(",", value_start)
            value = name_content[value_start:value_end].strip('"\n ')
            print(f"{keyword}: {value}")





