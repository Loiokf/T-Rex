class Stats:
    start_score = 0

    def __init__(self):
        self.run = True
        self.pause = False
        self.score = Stats.start_score
        self.time = 0

    @staticmethod
    def get_record():
        file = open("record.txt", "r")
        record = file.readline()
        file.close()
        return record

    @staticmethod
    def rewrite_record(new_record):
        file = open("record.txt", "w")
        file.write(str(new_record))
        file.close()

    def update_score(self):
        self.score += 1

    def get_score(self):
        return str(self.score // 10).zfill(5)

    def update_time(self):
        self.time += 1

    def restart(self):
        self.time = 0
        self.score = Stats.start_score
        self.run = True
