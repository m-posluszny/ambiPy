class Normalizer:
    def _ratio_scaler(self, val, old_range: tuple, new_range: tuple):
        old_ratio = old_range[1] - old_range[0]
        new_ratio = new_range[1] - new_range[0]
        return (((val - old_range[0]) * new_ratio) / old_ratio) + new_range[0]

    def _range_cut(self, val, range):
        if val < range[0]:
            return range[0]
        if val > range[1]:
            return range[1]
        return val

    def normalize_brightness(self, bright) -> float:
        pass

    def normalize_temperature(self, temp) -> float:
        pass
