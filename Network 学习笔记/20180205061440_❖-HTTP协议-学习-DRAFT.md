# ❖ HTTP协议 学习 [DRAFT]

主要看阮一峰入门：
http://www.ruanyifeng.com/blog/2012/05/internet_protocol_suite_part_i.html

http://www.ruanyifeng.com/blog/2012/06/internet_protocol_suite_part_ii.html

http://www.ruanyifeng.com/blog/2016/08/http.html

互联网协议，实际上不管是7层还是5层，
说白了就是一个洋葱，一层一层被剥开。
不管二进制码怎么样，直接用json直白一点：
```javascript
{ //实体层
    “Head”: "头",
    “Data: { //链接层
        “Head”: “头”,
	    “Data: { //网络层
	        "Head": "头",
	        "Data": { // 传输层
	        	"Head": "头", 
	        	"Data": { //应用层
	        		"Head": "头",
	        		"Data": ""
	        	}
	        }
	    }
    }
}

```
