import random
import time


class server:
    self.cache = {}

    def processGetReques(self, url):
        if url in self.cache:
            print(url + ' is already in the cache')
            return self.cache(url)
        print(url + 'is not cached yet. computing...')
        self.cache[url] = self.deExpensiveComputation(url)
        print('caching' + url + 'with value' + str(self.cache[url]))
        return self.cache(url)

    def deExpensiveComputation(self, url):
        time.sleep(5)
        return random.randint(0, 100)


server = server()
server.processGetReques("google.com")
server.processGetReques("google.com")
server.processGetReques("facebook.com")
