class Filter(object):
    def filter(self, x, a, b, c):
        raise NotImplementedError

    def reconstruct(self, x, a, b, c):
        raise NotImplementedError


class NoneFilter(Filter):
    def filter(self, x, a, b, c):
        return x

    def reconstruct(self, x, a, b, c):
        return x


class SubFilter(Filter):
    def filter(self, x, a, b, c):
        return (x - a) % 256

    def reconstruct(self, x, a, b, c):
        return (x + a) % 256


class UpFilter(Filter):
    def filter(self, x, a, b, c):
        return (x - b) % 256

    def reconstruct(self, x, a, b, c):
        return (x + b) % 256


class AverageFilter(Filter):
    def filter(self, x, a, b, c):
        return (x - (a + b) // 2) % 256

    def reconstruct(self, x, a, b, c):
        return (x + (a + b) // 2) % 256


class PaethFilter(Filter):
    def filter(self, x, a, b, c):
        return (x - self.paeth_predictor(a, b, c)) % 256

    def reconstruct(self, x, a, b, c):
        return (x + self.paeth_predictor(a, b, c)) % 256

    @staticmethod
    def paeth_predictor(a, b, c):
        p = a + b - c
        pa = abs(p - a)
        pb = abs(p - b)
        pc = abs(p - c)
        if pa <= pb and pa <= pc:
            pr = a
        elif pb <= pc:
            pr = b
        else:
            pr = c
        return pr


FILTER = {
    0: NoneFilter(),
    1: SubFilter(),
    2: UpFilter(),
    3: AverageFilter(),
    4: PaethFilter()
}


def reconstruct_scanline(filter, scanline, prev_scanline=None, pixel_size=1):
    """reconstruct filtered scanline(line of pixels)"""
    res = []
    for i in range(len(scanline)):
        a = res[i - pixel_size] if i >= pixel_size else 0
        b = prev_scanline[i] if prev_scanline else 0
        c = prev_scanline[i - pixel_size] if prev_scanline \
            and i >= pixel_size else 0
        res.append(filter.reconstruct(scanline[i], a, b, c))
    return res
