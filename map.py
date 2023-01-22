class Map(object):
    def __init__(self, W, H):
        self.frames = []
        self.points = []
        self.max_frame = 0
        self.max_point = 0

    def add_point(self, point):
        ret = self.max_point
        self.max_point += 1
        self.points.append(point)
        return ret

    def add_frame(self, frame):
        ret = self.max_frame
        self.max_frame += 1
        self.frames.append(frame)
        return ret
