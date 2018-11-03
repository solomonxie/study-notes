# ❖ AWS 各种服务之间的沟通 [DRAFT]


## 「Lightsail」与「AWS S3」的传输

Lightsail是AWS的低端产品，但是又不属于AWS的服务系列，之间交杂不清。所以与AWS的S3之间传输到底怎么算，网上的详细解释很少。根据[Lightsail官方FAQ](https://aws.amazon.com/lightsail/faq/)的说法，Lightsail的每个Instance实例都有自己预设的免费传输额，比如最便宜的实例免费额是1TB传输（包括输入输出）。一旦超出1T，那么只对输出收费。但是这个输出指的是使用实例的Public IP输出。也就是说，如果使用Private IP传输，就出入都不收费。但是，只有Lightsail的同Region才能访问到这个Private IP。所以一切在AWS之外的、在AWS内不同区的，都无法访问到Private IP，只能访问Public IP，等同于与Internet传输了。

关于Private IP，[参考Lightsail官网：Public IP and private IP addresses in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en/articles/understanding-public-ip-and-private-ip-addresses-in-amazon-lightsail)。其中提到，如果要让Lightsail与AWS其它服务进行沟通，需要用到`VPC Peering`（Virtual Private Cloud）方法，注意，VPC也是一项单独的AWS服务，是按小时付费的。

[参考官网：Set up Amazon VPC peering to work with AWS resources outside of Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en/articles/lightsail-how-to-set-up-vpc-peering-with-aws-resources)
> "A VPC is a virtual network dedicated to your AWS account. Everything you create inside Lightsail is inside a VPC, and you can connect your Lightsail VPC to an Amazon VPC."
**"Some AWS resources, such as _`Amazon S3`_, Amazon CloudFront, and Amazon DynamoDB don't require VPC peering to be enabled."**

也就是说，从Lightsail访问S3，是不需要启用VPC的。

具体再参考[官网：Using Amazon Lightsail with other AWS services](https://lightsail.aws.amazon.com/ls/docs/en/articles/using-lightsail-with-other-aws-services)

