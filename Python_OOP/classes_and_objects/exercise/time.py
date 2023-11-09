# class Time:
#     max_hours = 23
#     max_minutes = 59
#     max_seconds = 59
#
#     def __init__(self, hours: int, minutes: int, seconds: int):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def set_time(self, hours: int, minutes: int, seconds: int):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def next_second(self):
#         if self.seconds >= Time.max_seconds:
#             self.seconds = 0
#             self.minutes += 1
#
#             if self.minutes >= Time.max_minutes:
#                 self.minutes = 0
#                 self.hours += 1
#
#                 if self.hours >= Time.max_hours:
#                     self.hours = 0
#
#         else:
#             self.seconds += 1
#
#         return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

# GPT Code
class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.set_time(hours, minutes, seconds)

    def set_time(self, hours, minutes, seconds):
        if 0 <= hours <= Time.max_hours and 0 <= minutes <= Time.max_minutes and 0 <= seconds <= Time.max_seconds:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
        else:
            raise ValueError("Invalid time values")

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())

time = Time(1, 20, 30)
print(time.next_second())
