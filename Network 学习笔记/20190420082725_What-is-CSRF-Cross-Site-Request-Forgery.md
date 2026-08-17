# What is CSRF (Cross Site Request Forgery)

[Refer to: Cross Site Request Forgery - Computerphile](https://www.youtube.com/watch?v=vRBihr41JTo)

The attack is to make your own web page including a _hidden_ `<form>` that includes your _id, password_ or any other necessary information, and when a user open this malicious page it'll submit the form to the original site, say your bank site, and do something you unexpected.

Usually it won't work because the HTTP asks to have a `referrer` in each request's _header_, so that the "bank" will notice the request is not from the "bank"'s page but your malicious fake page.
But the thing is, in the modern network that there's `private mode` or `adblocker` in the browser that stops including the `referrer` in header of your request, so that the "bank" wouldn't know where's the request comes from & wouldn't stop you to login just because you're in `private mode`.
This allows the `CSRF` to work like what's described above.

How to stop that request from other sites if they don't have the `referrer` in _header_?
That solution is to add a random **token** in each form of the "bank"'s site. Any user opens up a page from the "bank", it'll generate a token hidden in the form, and it'll be changed each time you refresh the page as well.
So the attacker is not possible to fake that token in their own malicious web page. Because when you send a token made by yourself and send to the "bank", they'll decode it and find out that's not what they have generated and notice that this request is not from the official website.

And here comes the brief summary:
**The CSRF protection is simply to add a random token in each form that only the server can understand, which stops requests from other sites.**
