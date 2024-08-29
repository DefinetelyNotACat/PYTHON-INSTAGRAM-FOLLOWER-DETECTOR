import json
file = open("list.txt", "w")
num = 0
with open('following.json') as following:
    with open('followers_1.json') as followers:
        followingdata = json.load(following)
        followerdata = json.load(followers)
        #print(type(followingdata["relationships_following"]))
        #print(followingdata["relationships_following"])
        for x in followingdata["relationships_following"]:
            following_account = (x["string_list_data"][0]["value"])
            for y in followerdata:
                found = False
                follower_account = (y["string_list_data"][0]["value"])
                if following_account == follower_account:
                    found = True
                    break
            if found == False:
                print(following_account + "DOESN'T FOLLOW YOU")
                num+=1
                file.write(following_account + "\n")

print(f"ACCOUNT YOU'RE FOLLOWING BUT DON'T FOLLOW YOU BACK : {num}")
file.write(f"ACCOUNT YOU'RE FOLLOWING BUT DON'T FOLLOW YOU BACK : {num}")
file.close()       
        
    
    