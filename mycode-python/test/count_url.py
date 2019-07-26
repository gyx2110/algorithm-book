urls = [('www.zuoyebang.com',1),('www.zuoyebang.com',2),
('zhibo.zuoyebang.com',2),('www.zuoyebang.com',3),
('www.zuoyebang.com',1)]
m1 = {}
m2 = {}
for url in urls:
    m1[url[0]] = m1.get(url[0],0)+1
    key = str(url[0])+str(url[1])
    m2[key] = 1

res = []
for url,pv in m1.items():
    uv = 0
    for k,v in m2.items():
        if url in k:
            uv+=1
    res.append((url,uv,pv))
print res
