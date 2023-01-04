


#import dnspython as dns
import dns.resolver
import time


## Get query time ##

answers = dns.resolver.resolve("cisco.com", "A")
print("DNS record is: " ,answers.rrset)
print('DNS time =' , answers.response.time * 1000,"ms")


## Include EDNS ECS

request = dns.message.make_query('cisco.com', 'A')
ecs = dns.edns.ECSOption.from_text("213.205.240.74/24")
request.use_edns(edns=True, options=[ecs])
response = dns.query.udp(request, "1.1.1.1")
print ("ECS Query Response = ", response.answer)
print ("Response Time = ", response.time * 1000, "ms")
