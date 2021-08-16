import datetime
from instapy import InstaPy
from instapy.util import smart_run

followingacc = [] #acc to be followed in order to monitor

tdyfwers = []
ytrfwers = []

tdyfwings = []
ytrfwings = []

session = InstaPy(username='nottttkevinnn',
                  password='georgeolsen123',
                  headless_browser=False) #dummy acc login

username1="wu_shu_master" #change this to ur acc to be monitor
tdydate = datetime.datetime.today().strftime('%Y-%m-%d')


session.login()
session.follow_by_list(followlist=followingacc, times=1, sleep_delay=2, interact=False)
fwers = session.grab_followers(username=username1, amount="full", live_match=True, store_locally=True)
#print(type(fwers))
fwings = session.grab_following(username=username1, amount="full", live_match=True, store_locally=True)

file = open(f"pgdata\{username1}-{tdydate}-followers.txt", 'a') 
file.close()

file = open(f"pgdata\{username1}-{tdydate}-followers.txt", 'w') 

#today
for i in fwers:
    file.write(i)
    file.write("\n")
file.close()
file = open(f"pgdata\{username1}-{tdydate}-followers.txt", 'r') 
for line in file:
    m = line.strip()
    tdyfwers.append(m)
file.close()

file = open(f"pgdata\{username1}-{tdydate}-followings.txt",'a')
file.close()

file = open(f"pgdata\{username1}-{tdydate}-followings.txt", 'w')

for i in fwings:
    file.write(i)
    file.write("\n")
file.close()
file = open(f"pgdata\{username1}-{tdydate}-followings.txt", 'r')
for line in file:
    m = line.strip()
    tdyfwings.append(m)
file.close()
#

#yesterday 
#yesterdaytime = (datetime.datetime.now() - datetime.timedelta(1)).strftime('%Y-%m-%d') remove the # when u run the pg in the second day
yesterdaytime = tdydate #use this for first day run
file = open(f"pgdata\{username1}-{yesterdaytime}-followers.txt", 'r')
for line in file:
    m = line.strip()
    ytrfwers.append(m)
file.close()

file = open(f"pgdata\{username1}-{yesterdaytime}-followings.txt", "r")
for line in file:
    m = line.strip()
    ytrfwings.append(m)
file.close()
#

#comparing yesterday followers and followings with tdy followers and following, vice versa
diffwers = set(tdyfwers)-set(ytrfwers) #getting the diff from tdy and ytr of ur followers
diffwers2 = set(ytrfwers)-set(tdyfwers)#getting the diff from ytr and tdy of ur followers
unfolwers = diffwers.union(diffwers2) #union of diffwers and diffwers2

diffwings = set(tdyfwings)-set(ytrfwings)
diffwings2 = set(ytrfwings)-set(tdyfwings)
removefollowings = diffwings.union(diffwings2)
print("everything done!")
print(unfolwers)
print(removefollowings)
