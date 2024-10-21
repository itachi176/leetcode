# ==================================== Brute Force ===========================
class TimeMap:

    def __init__(self):
        self.dict_map = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict_map.append([key, value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        for d in self.dict_map:
            if d[0] == key and d[2] <= timestamp:
                res = d[1]
        return res


#======================= Binary Search =============================
class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        # for d in self.dict_map:
        #     if d[0] == key and d[2] <= timestamp:
        #         res = d[1]
        num_element = len(values)
        l, r = 0, num_element - 1 
        while l <= r:
            m = (l + r) // 2
            if int(values[m][1]) <= timestamp:  # Tìm trong khoảng thời gian hợp lệ
                
                res = values[m][0]   # Cập nhật kết quả
                l = m + 1  # Tiếp tục tìm bên phải
            else:
                r = m - 1  # Tìm bên trái nếu timestamp lớn hơn giá trị yêu cầu

        return res