import re

print("This takes around 5 minutes to run on my machine, it is working...")

# Get the count of stuff
count = 0
day = 0
month = ""
year = 0
day_count = 0
month_count = 0
year_count = 0
error_count = 0
redir_count = 0

array = []
months = [[],[],[],[],[],[],[],[],[],[],[],[]]


with open("http_access_log.txt","r") as f:
     for line in f:
          count +=1
          # Look for a match in the line
          date = re.search(r'\[(\d+)/(.+)/(\d+).+\]\s\".+\s(.+\..+)\s.+\"\s(\d+)', line)
          # check if there was as match in the line
          if(date != None):
               d = date.group(1)
               m = date.group(2)
               y = date.group(3)
               f = date.group(4)
               # print(f)
               s = date.group(5)
               if(d != day):
                    day = d
                    day_count += 1
               if(m != month):
                    month = m
                    month_count += 1
               if(y != year):
                    year = y
                    year_count += 1
               if(s[0]=="4"):
                    error_count += 1
               if(s[0]=="3"):
                    redir_count += 1

               # # [      0     ,      1     ]
               # #  [  0  ,  1 ] [   0 ,  1 ]
               # # [["file",cnt],["file",cnt]]
               # found = False
               # for index in range(len(array)):
               #      if(array[index][0] == f):
               #           array[index][1] += 1
               #           found = True
               #           break
               # if(not found):
               #      array.append([f,1])
               if(m == "Jan"):
                    months[0].append(line)
               if(m == "Feb"):
                    months[1].append(line)
               if(m == "Mar"):
                    months[2].append(line)
               if(m == "Apr"):
                    months[3].append(line)
               if(m == "May"):
                    months[4].append(line)
               if(m == "Jun"):
                    months[5].append(line)
               if(m == "Jul"):
                    months[6].append(line)
               if(m == "Aug"):
                    months[7].append(line)
               if(m == "Sep"):
                    months[8].append(line)
               if(m == "Oct"):
                    months[9].append(line)
               if(m == "Nov"):
                    months[10].append(line)
               if(m == "Dec"):
                    months[11].append(line)

# print(months[0])


with open("jan.txt", "a") as f:
     for line in months[0]:
          f.write(line)
with open("feb.txt", "a") as f:
     for line in months[1]:
          f.write(line)
with open("mar.txt", "a") as f:
     for line in months[2]:
          f.write(line)
with open("apr.txt", "a") as f:
     for line in months[3]:
          f.write(line)
with open("may.txt", "a") as f:
     for line in months[4]:
          f.write(line)
with open("jun.txt", "a") as f:
     for line in months[5]:
          f.write(line)
with open("jul.txt", "a") as f:
     for line in months[6]:
          f.write(line)
with open("aug.txt", "a") as f:
     for line in months[7]:
          f.write(line)
with open("sep.txt", "a") as f:
     for line in months[8]:
        f.write(line)  
with open("oct.txt", "a") as f:
     for line in months[9]:
          f.write(line)
with open("nov.txt", "a") as f:
     for line in months[10]:
          f.write(line)
with open("dec.txt", "a") as f:
     for line in months[11]:
          f.write(line)

array.sort(key=lambda x: x[1])                   



                         

print("The # of lines: ", count)
print("The # of different days: ", day_count)
print("The # of different months: ", month_count)
print("The # of different years: ", year_count)
print("The # of error codes: ", error_count)
print("The # of redirected codes: ", redir_count)

print("Most searched: ", str(array[-1]))
print("Least searched: ", str(array[0]))