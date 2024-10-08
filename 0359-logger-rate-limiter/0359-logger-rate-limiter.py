class Logger:

    def __init__(self):
        self.hash_map = {}   #will store string and timestamp

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.hash_map or timestamp >= self.hash_map[message]:
            self.hash_map[message] = timestamp + 10
            return True
        return False
            
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)