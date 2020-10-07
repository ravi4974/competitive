import csv

class Ads:
    domains={}

    @staticmethod
    def add_entry(domain_name,hits):
        if type(hits) is str:
            hits=int(hits)
        
        num_dots=len(domain_name)-len(domain_name.replace('.',''))
        actual_domain=domain_name

        #if more than one dots, it is a sub-domain
        if num_dots>1:
            idx=domain_name.rfind('.',0,domain_name.rfind('.'))
            actual_domain=domain_name[idx+1:]
        
        if actual_domain in Ads.domains:
            if domain_name in Ads.domains[actual_domain]:
                Ads.domains[actual_domain][domain_name]+=hits
            else:
                Ads.domains[actual_domain][domain_name]=hits
        else:
            Ads.domains[actual_domain]={domain_name:hits}
    
    @staticmethod
    def total(domain_name):
        return sum(Ads.domains.get(domain_name,{}).values())
    
    @staticmethod
    def details(domain_name):
        print(Ads.domains.get(domain_name,{}))


with open('domain_data.csv') as f:
    reader=csv.reader(f)
    for row in reader:
        Ads.add_entry(row[0],row[1])

print(Ads.total('domain-a.com'))
Ads.details('domain-b.com')