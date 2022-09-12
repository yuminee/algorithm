class Logger:
    
    def __init__(self):
        self.msg_map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.msg_map:
            if timestamp >= self.msg_map[message] + 10:
                self.msg_map[message] = timestamp
                return True
            else:
                return False
        else:
            self.msg_map[message] = timestamp
            return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)