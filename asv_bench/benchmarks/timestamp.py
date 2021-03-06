from .pandas_vb_common import *
from pandas import to_timedelta, Timestamp
import pytz
import datetime


class TimestampProperties(object):
    goal_time = 0.2

    params = [None, pytz.timezone('Europe/Amsterdam')]
    param_names = ['tz']

    def setup(self, tz):
        self.ts = Timestamp('2017-08-25 08:16:14', tzinfo=tz)

    def time_tz(self):
        self.ts.tz

    def time_offset(self):
        self.ts.offset

    def time_dayofweek(self):
        self.ts.dayofweek

    def time_weekday_name(self):
        self.ts.weekday_name

    def time_dayofyear(self):
        self.ts.dayofyear

    def time_week(self):
        self.ts.week

    def time_quarter(self):
        self.ts.quarter

    def time_days_in_month(self):
        self.ts.days_in_month

    def time_freqstr(self):
        self.ts.freqstr

    def time_is_month_start(self):
        self.ts.is_month_start

    def time_is_month_end(self):
        self.ts.is_month_end

    def time_is_quarter_start(self):
        self.ts.is_quarter_start

    def time_is_quarter_end(self):
        self.ts.is_quarter_end

    def time_is_year_start(self):
        self.ts.is_quarter_end

    def time_is_year_end(self):
        self.ts.is_quarter_end

    def time_is_leap_year(self):
        self.ts.is_quarter_end

    def time_microsecond(self):
        self.ts.microsecond


class TimestampOps(object):
    goal_time = 0.2

    params = [None, 'US/Eastern']
    param_names = ['tz']

    def setup(self, tz):
        self.ts = Timestamp('2017-08-25 08:16:14', tz=tz)

    def time_replace_tz(self):
        self.ts.replace(tzinfo=pytz.timezone('US/Eastern'))

    def time_replace_None(self):
        self.ts.replace(tzinfo=None)

    def time_to_pydatetime(self):
        self.ts.to_pydatetime()


class TimestampAcrossDst(object):
    goal_time = 0.2

    def setup(self):
        dt = datetime.datetime(2016, 3, 27, 1)
        self.tzinfo = pytz.timezone('CET').localize(dt, is_dst=False).tzinfo
        self.ts2 = Timestamp(dt)

    def time_replace_across_dst(self):
        self.ts2.replace(tzinfo=self.tzinfo)
