#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
GOAGENT_FETCHHOST_LIST = ["wcproxy-web.appspot.com", "benhot063.appspot.com", "cenjianneng11.appspot.com", "chankenvin.appspot.com", "cyanagt.appspot.com", "gokunkka.appspot.com", "ianbhullar.appspot.com", "jiegoa.appspot.com", "jndtydl005.appspot.com"]

gConfig = {
    "VERSION" : "20120624",
    "PROXY_TYPE": "goagent",# "goagent" or "socks5", can be created by `ssh -NfD 0.0.0.0:1234 user@hostname`
    "SOCKS_HOST": "localhost",
    "SOCKS_PORT": 1234,
    "GOAGENT_FETCHHOST": GOAGENT_FETCHHOST_LIST[random.randint(0, len(GOAGENT_FETCHHOST_LIST)-1)], 
    "GOAGENT_PASSWORD": "",
    "AUTORANGE_BUFSIZE": 8192,
    "AUTORANGE_WAITSIZE": 524288,
    "AUTORANGE_MAXSIZE": 1048576,
    "BLOCKED_DOMAINS_URI" : "https://raw.github.com/liruqi/west-chamber-season-3/master/west-chamber-proxy/status/timedout.txt",
    "ONLINE_CONFIG_URI" : "http://wcproxy.sinaapp.com/config.php",
    "REMOTE_DNS" : "168.95.1.1",
    "DNS_PROTOCOL": "udp",
    "DNS_PORT": 53,
    "DNS_CACHE_MAXSZ" : 1024,
    "SKIP_LOCAL_RESOLV" : True,
    "LOCAL_PORT" : 1998,
    "HOST" : {},
    "ADSHOSTON" : True,
    "ADSHOST" : {
        "stat.youku.com" : "0.0.0.0",
        "static.lstat.youku.com" : "0.0.0.0",
        "valb.atm.youku.com" : "0.0.0.0",
        "valc.atm.youku.com" : "0.0.0.0",
        "valf.atm.youku.com" : "0.0.0.0",
        "valo.atm.youku.com" : "0.0.0.0",
        "valp.atm.youku.com" : "0.0.0.0",
        "vid.atm.youku.com" : "0.0.0.0",
        "walp.atm.youku.com" : "0.0.0.0",
        "adextensioncontrol.tudou.com" : "127.0.0.1",
        "iwstat.tudou.com" : "127.0.0.1",
        "nstat.tudou.com" : "127.0.0.1",
        "stats.tudou.com" : "127.0.0.1",
        "*.p2v.tudou.com*" : "127.0.0.1",
        "at-img1.tdimg.com" : "127.0.0.1",
        "at-img2.tdimg.com" : "127.0.0.1",
        "at-img3.tdimg.com" : "127.0.0.1",
        "adplay.tudou.com" : "127.0.0.1",
        "adcontrol.tudou.com" : "127.0.0.1",
        "stat.tudou.com" : "127.0.0.1",
        "1.allyes.com.cn" : "127.0.0.1",
        "analytics.ku6.com" : "127.0.0.1",
        "gug.ku6cdn.com" : "127.0.0.1",
        "ku6.allyes.com" : "127.0.0.1",
        "ku6afp.allyes.com" : "127.0.0.1",
        "pq.stat.ku6.com" : "127.0.0.1",
        "st.vq.ku6.cn" : "127.0.0.1",
        "stat0.888.ku6.com" : "127.0.0.1",
        "stat1.888.ku6.com" : "127.0.0.1",
        "stat2.888.ku6.com" : "127.0.0.1",
        "stat3.888.ku6.com" : "127.0.0.1",
        "static.ku6.com" : "127.0.0.1",
        "v0.stat.ku6.com" : "127.0.0.1",
        "v1.stat.ku6.com" : "127.0.0.1",
        "v2.stat.ku6.com" : "127.0.0.1",
        "v3.stat.ku6.com" : "127.0.0.1",
        "afp.qiyi.com" : "127.0.0.1",
        "focusbaiduafp.allyes.com" : "127.0.0.1",
        "a.cctv.com" : "127.0.0.1",
        "a.cntv.cn" : "127.0.0.1",
        "ad.cctv.com" : "127.0.0.1",
        "d.cntv.cn" : "127.0.0.1",
        "adguanggao.eee114.com" : "127.0.0.1",
        "cctv.adsunion.com" : "127.0.0.1",
        "dcads.sina.com.cn" : "127.0.0.1",
        "pp2.pptv.com" : "127.0.0.1",
        "pro.letv.com" : "127.0.0.1",
        "images.sohu.com" : "127.0.0.1",
        "a.cctv.com" : "127.0.0.1",
        "a.cntv.cn" : "127.0.0.1",
        "ad.cctv.com" : "127.0.0.1",
        "d.cntv.cn" : "127.0.0.1",
        "adguanggao.eee114.com" : "127.0.0.1",
        "cctv.adsunion.com" : "127.0.0.1",
        "acs.56.com" : "127.0.0.1",
        "acs.agent.56.com" : "127.0.0.1",
        "acs.agent.v-56.com" : "127.0.0.1",
        "bill.agent.56.com" : "127.0.0.1",
        "bill.agent.v-56.com" : "127.0.0.1",
        "stat.56.com" : "127.0.0.1",
        "stat2.corp.56.com" : "127.0.0.1",
        "union.56.com" : "127.0.0.1",
        "uvimage.56.com" : "127.0.0.1",
        "v16.56.com" : "127.0.0.1",
        "pole.6rooms.com" : "127.0.0.1",
        "shrek.6.cn" : "127.0.0.1",
        "simba.6.cn" : "127.0.0.1",
        "union.6.cn" : "127.0.0.1",
        "86file.megajoy.com" : "127.0.0.1",
        "86get.joy.cn" : "127.0.0.1",
        "86log.joy.cn" : "127.0.0.1",
        "casting.openv.com" : "127.0.0.1",
        "m.openv.tv" : "127.0.0.1",
        "uniclick.openv.com" : "127.0.0.1",
        "mcfg.sandai.net" : "127.0.0.1",
        "biz5.sandai.net" : "127.0.0.1",
        "server1.adpolestar.net" : "127.0.0.1",
        "advstat.xunlei.com" : "127.0.0.1",
        "mpv.sandai.net" : "127.0.0.1",
        "asimgs.pplive.cn" : "127.0.0.1"
    },
    "HSTS_DOMAINS" : {
        "developers.facebook.com": 1,
        "groups.google.com": 1,
        "www.paypal.com" : 1,
        "www.elanex.biz" : 1,
        "jottit.com" : 1,
        "sunshinepress.org" : 1,
        "www.noisebridge.net" : 1,
        "neg9.org" : 1,
        "riseup.net" : 1,
        "factor.cc" : 1,
        "splendidbacon.com" : 1,
        "aladdinschools.appspot.com" : 1,
        "ottospora.nl" : 1,
        "www.paycheckrecords.com" : 1,
        "market.android.com" : 1,
        "lastpass.com" : 1,
        "www.lastpass.com" : 1,
        "keyerror.com" : 1,
        "entropia.de" : 1,
        "romab.com" : 1,
        "logentries.com" : 1,
        "stripe.com" : 1,
        "facebook.com": 1,
    },
    #collect domains that support HTTPS, to reduce usage of web proxy
    "HSTS_ON_EXCEPTION_DOMAINS" : {
        "s.ytimg.com": 1,
        "i1.ytimg.com": 1,
        "i2.ytimg.com": 1,
        "i3.ytimg.com": 1,
        "i4.ytimg.com": 1,
        "i1.tdimg.com": 1,
        "i2.tdimg.com": 1,
        "i3.tdimg.com": 1,
        "i4.tdimg.com": 1,
        "bits.wikimedia.org": 1,
        "www.wikipedia.org": 1,
        "www.google-analytics.com": 1,
        "apps.facebook.com": 1,
        "graph.facebook.com": 1,
        "www.youtube.com": 1,
        "m.facebook.com": 1,
    },
    "BLOCKED_DOMAINS": {
        "baidu.jp" : True,
        "search.twitter.com" : True,
        "www.baidu.jp" : True,
        "www.nicovideo.jp": True,
        "www.dailymotion.com": True,
        "ext.nicovideo.jp": True,
        "blog.roodo.com": True,
        "www.dwnews.com": True,
        "china.dwnews.com": True,
        "www.mediafire.com": True,
        "thepiratebay.org": True,
        "thepiratebay.se": True,
        "www.bbc.co.uk": True,
        "chinadigitaltimes.net": True,
        "www.wenxuecity.com": True,
        "bbs.wenxuecity.com": True,
        "www.blogger.com": True,
        "blogger.com": True,
    },
    "BLOCKED_IPS": {
        "23.21.220.40":1, "23.21.242.194":1, #dropbox
        "50.16.240.166":1, #dropbox
        "70.86.20.29" : 1, #www.bullogger.com
        "66.220.149.25": 1,
        "66.220.146.101": 1,
        "69.171.224.53": 1,
        "66.220.149.11": 1,
        "66.220.158.11": 1,
        "69.171.242.11": 1,
        "69.93.206.250": 1, #www.xys.org
        "69.163.141.215": 1, #www.zuola.com
        "174.121.98.156": 1,
        "50.22.53.157": 1,
        "50.22.53.155": 1,
        "50.63.43.1": 1,
        "72.32.231.8": 1,
        "72.233.2.58": 1,
        "74.125.31.141": 1,
        "74.125.39.102": 1,
        "174.121.66.230": 1,
        "107.20.170.126": 1,
        "180.235.96.30": 1,
        "204.236.224.226": 1,
        "69.163.223.11": 1, #letscorp.net
        "199.59.148.12": 1, "199.59.149.210": 1, #t.co
    },
    "CHINA_IP_LIST_FILE":"exclude-ip.json",
    "PAGE_RELOAD_HTML": """<html>
    <head>
        <script type="text/javascript" charset="utf-8">
            window.location.reload();
        </script>
    </head>
    <body>
    </body></html>""",
}

# 69.171.228.0/24 for facebook
blockedIpString = """69.171.228.5
69.171.228.6
69.171.228.11
69.171.228.12
69.171.228.15
69.171.228.16
69.171.228.19
69.171.228.20
69.171.228.23
69.171.228.24
69.171.228.27
69.171.228.28
69.171.228.31
69.171.228.35
69.171.228.36
69.171.228.50
69.171.228.51
69.171.228.70
69.171.228.71
69.171.228.74
69.171.228.75
69.171.228.79
69.171.228.229
69.171.228.230
69.171.228.231
69.171.228.232
69.171.228.233
69.171.228.234
69.171.228.244
69.171.228.245
69.171.228.246
69.171.228.247
69.171.228.248
69.171.228.249
69.171.228.250
69.171.228.251
69.171.228.252
69.171.228.253
69.171.228.254
"""

# 69.171.229.0/24 for facebook
blockedIpString += """69.171.229.11
69.171.229.12
69.171.229.13
69.171.229.14
69.171.229.15
69.171.229.16
69.171.229.20
69.171.229.23
69.171.229.24
69.171.229.27
69.171.229.28
69.171.229.31
69.171.229.32
69.171.229.46
69.171.229.47
69.171.229.51
69.171.229.70
69.171.229.71
69.171.229.72
69.171.229.73
69.171.229.74
69.171.229.76
69.171.229.77
69.171.229.229
69.171.229.230
69.171.229.231
69.171.229.232
69.171.229.233
69.171.229.234
69.171.229.244
69.171.229.245
69.171.229.246
69.171.229.247
69.171.229.248
69.171.229.249
69.171.229.250
69.171.229.251
69.171.229.252
69.171.229.253
69.171.229.254
"""

# 69.171.224.0/24 for facebook
blockedIpString += """69.171.224.1
69.171.224.2
69.171.224.3
69.171.224.4
69.171.224.5
69.171.224.6
69.171.224.32
69.171.224.33
69.171.224.34
69.171.224.35
69.171.224.36
69.171.224.37
69.171.224.38
69.171.224.39
69.171.224.40
69.171.224.41
69.171.224.48
69.171.224.49
69.171.224.50
69.171.224.51
69.171.224.52
69.171.224.53
69.171.224.54
69.171.224.55
69.171.224.56
69.171.224.57
69.171.224.64
69.171.224.65
69.171.224.66
69.171.224.67
69.171.224.68
69.171.224.80
69.171.224.81
69.171.224.82
69.171.224.83
69.171.224.84
69.171.224.96
69.171.224.97
69.171.224.98
69.171.224.99
69.171.224.100
69.171.224.112
69.171.224.113
69.171.224.114
69.171.224.115
69.171.224.116"""

# 69.171.234.0/24 for facebook
blockedIpString += """
69.171.234.16
69.171.234.17
69.171.234.19
69.171.234.32
69.171.234.35
69.171.234.48
69.171.234.49
69.171.234.64
69.171.234.65
69.171.234.68
69.171.234.80
69.171.234.82
69.171.234.83
69.171.234.96
69.171.234.98"""

# 74.125.0.0/16
blockedIpString += """74.125.71.88
74.125.71.89
74.125.71.99
74.125.71.100
74.125.71.101
74.125.71.106
74.125.71.113
74.125.71.116
74.125.71.121
74.125.71.128
74.125.71.138
74.125.71.139
74.125.71.150
74.125.71.160
74.125.71.161
74.125.71.162
74.125.71.163
74.125.71.188
74.125.71.192
74.125.127.16
74.125.127.19
74.125.127.27
74.125.127.83
74.125.127.91
74.125.127.93
74.125.127.99
74.125.127.101
74.125.127.102
74.125.127.105
74.125.127.108
74.125.127.109
74.125.127.113
74.125.127.121
74.125.127.128
74.125.127.130
74.125.127.132
74.125.127.136
74.125.127.138
74.125.127.141
74.125.127.150
74.125.127.160
74.125.127.161
74.125.127.162
74.125.127.163
74.125.127.188
74.125.127.190
74.125.127.192
74.125.127.204
74.125.127.205
74.125.127.206
74.125.127.207
74.125.127.208
"""

# 199.59.150.0/24
blockedIpString += """199.59.150.7
199.59.150.8
199.59.150.9
199.59.150.10
199.59.150.11
199.59.150.12
199.59.150.39
199.59.150.40
199.59.150.41
199.59.150.42
199.59.150.43
199.59.150.44
"""

# 199.59.149.0/24
blockedIpString += """199.59.149.65
199.59.149.66
199.59.149.67
199.59.149.68
199.59.149.70
199.59.149.76
199.59.149.77
199.59.149.81
199.59.149.82
199.59.149.83
199.59.149.84
199.59.149.86
199.59.149.87
199.59.149.88
199.59.149.89
199.59.149.90
199.59.149.91
199.59.149.92
199.59.149.93
199.59.149.94
199.59.149.97
199.59.149.98
199.59.149.99
199.59.149.100
199.59.149.101
199.59.149.105
199.59.149.106
199.59.149.107
199.59.149.108
199.59.149.109
199.59.149.110
199.59.149.111
199.59.149.112
199.59.149.113
199.59.149.114
199.59.149.115
199.59.149.116
199.59.149.117
199.59.149.118
199.59.149.119
199.59.149.120
199.59.149.121
199.59.149.122
199.59.149.123
199.59.149.124
199.59.149.125
199.59.149.129
199.59.149.130
199.59.149.131
199.59.149.132
199.59.149.133
199.59.149.134
199.59.149.135
199.59.149.136
199.59.149.138
199.59.149.139
199.59.149.161
199.59.149.162
199.59.149.163
199.59.149.164
199.59.149.165
199.59.149.166
199.59.149.193
199.59.149.194
199.59.149.195
199.59.149.225
199.59.149.226
199.59.149.227
199.59.149.228
199.59.149.229
199.59.149.230
199.59.149.231
199.59.149.232
199.59.149.233
199.59.149.234
199.59.149.235
199.59.149.240
199.59.149.243
199.59.149.245
199.59.149.246
"""

# 199.59.148.0/24
blockedIpString += """199.59.148.6
199.59.148.7
199.59.148.8
199.59.148.9
199.59.148.10
199.59.148.11
199.59.148.12
199.59.148.15
199.59.148.20
199.59.148.21
199.59.148.22
199.59.148.23
199.59.148.60
199.59.148.69
199.59.148.82
199.59.148.84
199.59.148.85
199.59.148.87
199.59.148.88
199.59.148.89
199.59.148.92
199.59.148.96
199.59.148.97
199.59.148.102
199.59.148.104
199.59.148.105
199.59.148.106
199.59.148.124
199.59.148.125
199.59.148.126
199.59.148.129
199.59.148.130
199.59.148.131
199.59.148.132
199.59.148.133
199.59.148.135
199.59.148.139
199.59.148.140
199.59.148.181
199.59.148.193
199.59.148.194
199.59.148.195
199.59.148.201
199.59.148.204
199.59.148.206
199.59.148.207
199.59.148.208
199.59.148.209
199.59.148.213
199.59.148.215
199.59.148.216
199.59.148.217
199.59.148.218
199.59.148.219
199.59.148.222
199.59.148.224
199.59.148.226
199.59.148.230
199.59.148.231
199.59.148.232
199.59.148.233
199.59.148.234
199.59.148.235
199.59.148.236
199.59.148.237
199.59.148.238
199.59.148.239
199.59.148.240
199.59.148.241"""


for ip in blockedIpString.split("\n"):
    if len(ip) > 0:
        gConfig["BLOCKED_IPS"][ip] = 1


