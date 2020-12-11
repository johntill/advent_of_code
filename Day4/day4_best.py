import sys
import re

eye_colours = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

fields = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x.endswith("cm") and 150 <= int(x[:-2]) <= 193) or
                     (x.endswith("in") and 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: re.fullmatch(r"#[\da-f]{6}", x),
    "ecl": lambda x: x in eye_colours,
    "pid": lambda x: re.fullmatch(r"\d{9}", x),
}

present = valid = 0

for line in sys.stdin.read().split("\n\n"):
    passport = dict(l.split(":") for l in line.split())

    if not passport.keys() >= fields.keys():
        continue

    present += 1
    valid += all(data(passport[field]) for field, data in fields.items())

print(present)
print(valid)