#!/usr/bin/env python

import re
import sys
import pytest
import math
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
)

logger = logging.getLogger()

from collections import namedtuple


def is_passport_valid(passport, valid_fields):
    optional_fields = set(["cid"])

    fields = set(passport.keys()).union(optional_fields)

    return fields == valid_fields


def is_passport_valid_2(passport, valid_fields):
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    optional_fields = set(["cid"])

    fields = set(passport.keys()).union(optional_fields)
    diff = valid_fields.difference(fields)

    if diff:
        logger.warn("Invalid %s", passport)
        logger.warn("Missing fields %s", diff)
        return False

    match_patterns = {
        "byr": r'^19[2-9][0-9]|200[0-2]$',
        "iyr": r'^201[0-9]|2020$',
        "eyr": r'^202[0-9]|2030$',
        "hgt": r'^1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in$',
        "hcl": r'^#[0-9a-f]{6}$',
        "ecl": r'^(amb|blu|brn|gry|grn|hzl|oth)$',
        "pid": r'^[0-9]{9}$',
    }

    try:
        for pass_field, pattern in match_patterns.items():
            val = passport[pass_field].strip()
            matched = re.match(pattern, val)

            if not matched:
                logger.warn("Invalid %s", passport)
                logger.warn("%s=%s not matches to %s", pass_field, val, pattern)
                return False

    except KeyError:
        return False

    logger.warn("Valid %s", passport)

    return True


def get_valid_passports(iterator, is_valid_pass_func=is_passport_valid):
    """
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
    """
    valid_passports = 0

    valid_fields = set(
        [
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid",
            "cid",
        ]
    )

    fields_split = "({}):".format("|".join(valid_fields))

    passport = dict()

    for line in iterator:
        line = line.strip()

        if not line:
            if is_valid_pass_func(passport, valid_fields):
                valid_passports += 1

            passport = dict()

        parts = re.split(fields_split, line)

        assert not parts[0]

        for k, v in zip(parts[1::2], parts[2::2]):
            passport[k] = v

    if passport and is_valid_pass_func(passport, valid_fields):
        valid_passports += 1

    return valid_passports


@pytest.mark.parametrize(
    'lines,expected',
    [
        (
            [
                "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
                "byr:1937 iyr:2017 cid:147 hgt:183cm",
                "",
                "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
                "hcl:#cfa07d byr:1929",
                "",
                "hcl:#ae17e1 iyr:2013",
                "eyr:2024",
                "ecl:brn pid:760753108 byr:1931",
                "hgt:179cm",
                "",
                "hcl:#cfa07d eyr:2025 pid:166559648",
                "iyr:2011 ecl:brn hgt:59in",
            ],
            2,
        ),
        (
            ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd"],
            0,
        ),
        (
            [
                "hcl:#ae17e1 iyr:2013",
                "eyr:2024",
                "ecl:brn pid:760753108 byr:1931",
                "hgt:179cm",
            ],
            1,
        ),
    ],
)
def test_valid_passports(lines, expected):
    assert get_valid_passports(lines) == expected


@pytest.mark.parametrize(
    'lines,expected',
    [
        # All invalid passports
        pytest.param(
            [
                "eyr:1972 cid:100",
                "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
                "",
                "iyr:2019",
                "hcl:#602927 eyr:1967 hgt:170cm",
                "ecl:grn pid:012533040 byr:1946",
                "",
                "hcl:dab227 iyr:2012",
                "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
                "",
                "hgt:59cm ecl:zzz",
                "eyr:2038 hcl:74454a iyr:2023",
                "pid:3556412378 byr:2007",
            ],
            0,
            id="invalid",
        ),
        # All valid passports
        pytest.param(
            [
                "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
                "hcl:#623a2f",
                "",
                "eyr:2029 ecl:blu cid:129 byr:1989",
                "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
                "",
                "hcl:#888785",
                "hgt:164cm byr:2001 iyr:2015 cid:88",
                "pid:545766238 ecl:hzl",
                "eyr:2022",
                "",
                "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
            ],
            4,
            id="valid",
        ),
    ],
)
def test_valid_passports_2(lines, expected):
    assert get_valid_passports(lines, is_passport_valid_2) == expected


if __name__ == "__main__":
    num = get_valid_passports(sys.stdin, is_passport_valid_2)

    print("{0}".format(num))
