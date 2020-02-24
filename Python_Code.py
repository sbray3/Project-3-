import re

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

with open("http_access_log.txt","r") as f:
     for line in f:
          count +=1
          # Look for a match in the line
          date = re.search(r'\[(\d+)/(.+)/(\d+).+\]\s(\".+\")\s(\d+)', line)
          # check if there was as match in the line
          if(date != None):
               d = date.group(1)
               m = date.group(2)
               y = date.group(3)
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
               if( s[0]=="4"):
                    error_count += 1
               if( s[0]=="3"):
                    redir_count +=1

                         

print("The # of lines: ", count)
print("The # of different days: ", day_count)
print("The # of different months: ", month_count)
print("The # of different years: ", year_count)
print("The # of error codes: ", error_count)
print("The # of redirected codes: ", redir_count)

