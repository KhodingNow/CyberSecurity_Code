
import time 
# this module is used to measure elapsed time, controlling time related behaviou in the code

class RateLimter:
    def __init__(self, max_requests, refill_rate):
        self.max_requests = max_requests
        self.refill_rate = refill_rate
        self.tokens = max_requests
        self.last_refill_time = time.time()


# this Python class 'Ratelimiter' will encapsulate our rate limiting logic
# The '__init__' constructor initializes the rate limiter with two parameters
# * 'max_requests': controls the max number of requests allowed per specified time window
# * 'refill_rate' : In the token bucket, this controls the rate at token refill rate
# * we initialize an instance variable to keep track of current token count ('self.tokens'), the max allowed token count, 
#.. and time when tokens were last refilled


    def _refill(self):
        now = time.time()
        elapsed_time = now - self.last_refill_time
        tokens_to_add = elapsed_time * self.refill_rate
        self.tokens = min(self.max_requests, self.tokens + tokens_to_add)
        self.last_refill_time = now

# the 'refill' method calculates how many token shld be added to the bucket based on the elapsed time
# ..since the last refill AND then refills the bucket accordingly
# it retrieves the current time  using 'time.time()'
# it claculates the elapsed time since the last refill
# it calculates how many tokens should be added bsed on the elapsed time and the refill rate
# it ensures that the token count does not exceed the maximum allowed ('self.max_requests')
# it updates the last refill time to the current time  

    def check_request(self):
        self._refill()
        if self.tokens >=1:
            self.tokens -=1
            return True
        else:
            return False
    
# * The 'check_request' method checks whether a new request can be allowed:
# - it calls the '_refill' method to ensure that the token count is up to date
# - it checks if there is atleast one token available ('self.token >=1')
# - if there is at least one token , it decrements the token count by 1 ('self.tokens -= 1') and allows the request
# - if there are no tokens available, it returns 'FALSE' to indicate that the request should be rate limited (DENIED).

if __name__ == "__main__":
    max_requests_per_second = 10
    refill_rate = 1

    limiter = RateLimter(max_requests_per_second, refill_rate)

    for i in range(15):
        if limiter.check_request():
            print(f"Request {i + 1}: Allowed")
        else:
            print(f"Request {i + 1}: Rate Limited / (Denied)")
            time.sleep(0.1)

 
# this section is the MAIN part of the script that demonstrate the rate limiting logic
# we specify the rate liiting parameters: 'max_requests_per_second' (max allowed requests pers second)
#...and the 'refill_rate' (tokens added per second)
# we create a 'RateLimiter' instance called 'limiter' with these parameters
# we simulate 15 incoming requests using a 'FOR' loop.
# we print result to each request, indicating whether it's allowed or denied - rate limited.
# we introduce a delay of 100 milliseconds (0.1 seconds) between requests using 'time.sleep(0.1)' to simulate a more realistic request rate

