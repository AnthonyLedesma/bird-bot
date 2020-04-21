import requests,time,lxml.html,json,sys,settings,send_sms,logging,re

logging.basicConfig(filename='r.text.log',level=logging.DEBUG)

class Target:
    def __init__(self,task_id,status_signal,image_signal,product,profile,proxy,monitor_delay,error_delay):
        self.status_signal,self.image_signal,self.product,self.profile,self.monitor_delay,self.error_delay = status_signal,image_signal,product,profile,float(monitor_delay),float(error_delay)
        self.session = requests.Session()
        if proxy != False:
            self.session.proxies.update(proxy)
        self.status_signal.emit({"msg":"Starting","status":"normal"})
        while True:
            self.monitor()
            time.sleep(20)

    def monitor(self):
            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
                "cache-control": "max-age=0",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.69 Safari/537.36"
            }
            image_found = False
            product_image = ""
            while True:
                self.status_signal.emit({"msg":"Loading Product Page","status":"normal"})
                try:
                    r = self.session.get(self.product,headers=headers)
                    #logging.debug(r.text)
                    if r.status_code == 200:
                        doc = lxml.html.fromstring(r.text)
                        # if not image_found:
                        #     product_image = doc.xpath('//meta[@property="og:image"]/@content')[0]
                        #     self.image_signal.emit(product_image)
                        #     image_found = True
                        #price = float(doc.xpath('//span[@itemprop="price"]/@content')[0])
                        #if re.search("Add.to.cart",r.text):
                        if "Add to cart" in r.text:
                            #offer_id = json.loads(doc.xpath('//script[@id="item"]/text()')[0])["item"]["product"]["buyBox"]["products"][0]["offerId"]

                            # personalized code. If we got here, the item is in stock. With BB we cannot checkout with the bot,
                            # so instead we will send griffin a text message alerting him
                            send_sms.send_text("Target Switch in stock at URL {}".format(self.product))
                            self.status_signal.emit({"msg":"In Stock, sending SMS...","status":"normal"})
                            return

                        self.status_signal.emit({"msg":"Waiting For Restock","status":"normal"})
                        self.session.cookies.clear()
                        time.sleep(self.monitor_delay)
                    else:
                        self.status_signal.emit({"msg":"Product Not Found","status":"normal"})
                        time.sleep(self.monitor_delay)
                except Exception as e:
                    self.status_signal.emit({"msg":"Error Loading Product Page (line {} {} {})".format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e),"status":"error"})
                    time.sleep(self.error_delay)




