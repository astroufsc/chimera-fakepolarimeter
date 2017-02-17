# example of a fake polarimeter
# it is actually composed by three independent filterwheels. don't know if this is the best way to do it
import itertools
from chimera.instruments.fakefilterwheel import FakeFilterWheel
from chimera.instruments.filterwheel import FilterWheelBase


class FakePolarimeter(FilterWheelBase):
    def __init__(self):
        FilterWheelBase.__init__(self)
        self["device"] = "/FilterWheel/1,/FilterWheel/2,/FilterWheel/3,/FilterWheel/4"
        self["filters"] = None

    def __start__(self):
        self._wheels = [self.getManager().getProxy(wheel, lazy=True) for wheel in self["device"].split(',')]
        filters = [wheel["filters"].split() for wheel in self._wheels]
        self["filters"] = ' '.join([','.join(comb) for comb in itertools.product(*filters)])

    def setFilter(self, filter):
        f = filter.split(',')
        for wheel_num, wheel in enumerate(self._wheels):
            self._wheels[wheel_num].setFilter(f[wheel_num])
        return True

    def getFilter(self):
        filters = ""
        for wheel_num, wheel in enumerate(self._wheels):
            filters += "," + self._wheels[wheel_num].getFilter()
        return filters[1:]

    # def getMetadata(self, request):
    #     md = list()
    #     for wheel in self._wheels:
    #         for header in wheel.getMetadata(request):
    #             md.append(header)
    #     print md
    #     return md


class FakePolarimeterFilterWheel(FakeFilterWheel):
    def __init__(self):
        FakeFilterWheel.__init__(self)
        self["device"] = None
        self['filter_wheel_model'] = "Fake Polarimeter Filter Wheel"
        self["filters"] = "U B V R I"

    # def getMetadata(self, request):
    #     return [('FILTER', str(self.getFilter()), 'Filter used for this observation')]
        # ('FWHEEL', str(self['filter_wheel_model']), 'FilterWheel Model'),


class FakePolarimeterAnalyzerWheel(FakeFilterWheel):
    def __init__(self):
        FakeFilterWheel.__init__(self)
        self["device"] = None
        self['filter_wheel_model'] = "Fake Polarimeter Analyzer Wheel"
        self["filters"] = "CLEAR CALCITE VIS RED"

    # def getMetadata(self, request):
    #     return [('POLARIZER_TYPE', str(self.getFilter()), 'Polarizer type')]
        # ('FWHEEL', str(self['filter_wheel_model']), 'FilterWheel Model'),


class FakePolarimeterWavePlate(FakeFilterWheel):
    def __init__(self):
        FakeFilterWheel.__init__(self)
        self["device"] = None
        self['filter_wheel_model'] = "Fake Polarimeter Wave Plate Wheel"
        self[
            "filters"] = "0.0 22.5 45.0 67.5 90.0 112.5 135.0 157.5 180.0 202.5 225.0 247.5 270.0 292.5 315.0 337.5"

    # def getMetadata(self, request):
    #     return [('HWAVE_PLATE', str(self.getFilter()), 'Wave Plate position')]
        # ('FWHEEL', str(self['filter_wheel_model']), 'FilterWheel Model'),


class FakePolarimeterDither(FakeFilterWheel):
    # Maybe this one should override the method setFilter to a float number which is the dither position in mm

    def __init__(self):
        FakeFilterWheel.__init__(self)
        self["device"] = None
        self['filter_wheel_model'] = "Fake Polarimeter Dithering position"
        self["filters"] = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17"

    # def getMetadata(self, request):
    #     return [('POL_DITHER', str(self.getFilter()), 'Polarimeter Dither position')]
        # ('FWHEEL', str(self['filter_wheel_model']), 'FilterWheel Model'),
