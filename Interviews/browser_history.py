user_1='''
https://someurl.com/asdbjhabsdhbajdbjasbdjabdjhbasjdhbjabd
https://someurl.com/asdbjhabsdhbajdbjasbd12331231bdjhbasjdhbjabd
https://someurl.com/asdbjhabsdhbajdbjasbdjabdjhbasjdhbjabd
https://someurl.com/asdbjhabsdhbajdbjasbdjabdjhbasjdhbjabd
https://someurl.com/asdbjhabsdhbajdbjasbdjabd5656565sjdhbjabd
https://someurl.com/asdbjhabsdhbajdbjasbdjabdjhbasjdhbjabd
https://someurl.com/asdbjhabsdhbajdbjasbdjabdjhbasjdhbjabd
https://someurl.com/asdbjhabsdhbajdbjasbdjabdjhba576767hbjabd
https://someurl.com/asdbjhabsdhbajdbjasbdjabdjhbasj12abd
'''
user_2='''
https://someurl.com/asdbjhabsdhbajdbjasbdjabdjhbasjdhbjerd
https://someurl.com/asdbjhabsdhbajdbjasbd12331231bdjhbasjdhbjabd
https://someurl.com/asdbjhabsdhbajdbjasbdjabdjhbasjdhbjfgd
https://someurl.com/asdbjhabsdhbajdbjasbdjabdjhbasjdhbjabvd
https://someurl.com/asdbjhabsdhbajdbjasbdjabd5656565sjdhabd
https://someurl.com/asdbjhabsdhbajdbjasbdjabdjhbasjdhbfgbd
https://someurl.com/asdbjhabsdhbajdbjasbdjabdjhbasjdhbjabd
https://someurl.com/asdbjhabsdhbajdbjasbdjabdjhba576767hbjabd
https://someurl.com/asdbjhabsdhbajdbjasbdjabdjhbasj12abd
'''

user_1_urls=set(user_1.strip().split('\n'))
user_2_urls=set(user_2.strip().split('\n'))

common_urls=user_1_urls.intersection(user_2_urls)
common_urls=sorted(common_urls,key=len,reverse=True)

print(common_urls[0])