import re
# This counts the # of lines
f = open("http_access_log.txt", "r")
count = 0
for line in f:
     count +=1
print("Number of lines: ",count)
f.close()

# Get the count of stuff

day = 0
month = ""
year = 0
day_count = 0
month_count = 0
year_count = 0

with open("http_access_log.txt","r") as f:
     for line in f:
          # Look for a match in the line
          date = re.search(r'\[(\d+)/(.+)/(\d+).+\]', line)
          # check if there was as match in the line
          if(date != None):
               d = date.group(1)
               m = date.group(2)
               y = date.group(3)
               if(d != day):
                    day = d
                    day_count += 1
               if(m != month):
                    month = m
                    month_count += 1
               if(y != year):
                    year = y
                    year_count += 1

print("The # of different days: ", day_count)
print("The # of different months: ", month_count)
print("The # of different years: ", year_count)

