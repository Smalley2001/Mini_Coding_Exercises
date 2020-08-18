secs_str = input("Input seconds: ") 
secs_int=int(secs_str)
days= secs_int//86400
secs_int%=86400
hours = secs_int//3600
secs_int%=3600
minutes = secs_int//60
secs_int%=60
seconds = secs_int//1
print(str(secs_str) + " seconds is equivalent to: " + str(days), "days:", str(hours),"hours:",str(minutes)," minutes:",str(seconds), " seconds.")