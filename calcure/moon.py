"""Module that controls display of the moon phases"""

from datetime import datetime


# Dictionary of moon phases taken from:
# https://github.com/PanderMusubi/lunar-phase-calendar/blob/master/GB/en/moon-phases.tsv

moon_phases = {
    "2024-06-29": "Last quarter",
    "2024-07-06": "New moon",
    "2024-07-14": "First quarter",
    "2024-07-21": "Full moon",
    "2024-07-28": "Last quarter",
    "2024-08-04": "New moon",
    "2024-08-13": "First quarter",
    "2024-08-20": "Full moon",
    "2024-08-26": "Last quarter",
    "2024-09-03": "New moon",
    "2024-09-11": "First quarter",
    "2024-09-18": "Full moon",
    "2024-09-25": "Last quarter",
    "2024-10-03": "New moon",
    "2024-10-11": "First quarter",
    "2024-10-18": "Full moon",
    "2024-10-24": "Last quarter",
    "2024-11-01": "New moon",
    "2024-11-09": "First quarter",
    "2024-11-16": "Full moon",
    "2024-11-23": "Last quarter",
    "2024-12-01": "New moon",
    "2024-12-09": "First quarter",
    "2024-12-15": "Full moon",
    "2024-12-23": "Last quarter",
    "2024-12-31": "New moon",
    "2025-01-07": "First quarter",
    "2025-01-14": "Full moon",
    "2025-01-22": "Last quarter",
    "2025-01-30": "New moon",
    "2025-02-05": "First quarter",
    "2025-02-13": "Full moon",
    "2025-02-21": "Last quarter",
    "2025-02-28": "New moon",
    "2025-03-07": "First quarter",
    "2025-03-14": "Full moon",
    "2025-03-22": "Last quarter",
    "2025-03-30": "New moon",
    "2025-04-05": "First quarter",
    "2025-04-13": "Full moon",
    "2025-04-21": "Last quarter",
    "2025-04-28": "New moon",
    "2025-05-05": "First quarter",
    "2025-05-13": "Full moon",
    "2025-05-21": "Last quarter",
    "2025-05-27": "New moon",
    "2025-06-03": "First quarter",
    "2025-06-11": "Full moon",
    "2025-06-19": "Last quarter",
    "2025-06-26": "New moon",
    "2025-07-03": "First quarter",
    "2025-07-11": "Full moon",
    "2025-07-18": "Last quarter",
    "2025-07-25": "New moon",
    "2025-08-01": "First quarter",
    "2025-08-09": "Full moon",
    "2025-08-16": "Last quarter",
    "2025-08-23": "New moon",
    "2025-08-31": "First quarter",
    "2025-09-08": "Full moon",
    "2025-09-14": "Last quarter",
    "2025-09-22": "New moon",
    "2025-09-30": "First quarter",
    "2025-10-07": "Full moon",
    "2025-10-14": "Last quarter",
    "2025-10-21": "New moon",
    "2025-10-30": "First quarter",
    "2025-11-06": "Full moon",
    "2025-11-12": "Last quarter",
    "2025-11-20": "New moon",
    "2025-11-28": "First quarter",
    "2025-12-05": "Full moon",
    "2025-12-12": "Last quarter",
    "2025-12-20": "New moon",
    "2025-12-28": "First quarter",
    "2026-01-04": "Full moon",
    "2026-01-11": "Last quarter",
    "2026-01-19": "New moon",
    "2026-01-26": "First quarter",
    "2026-02-02": "Full moon",
    "2026-02-09": "Last quarter",
    "2026-02-18": "New moon",
    "2026-02-25": "First quarter",
    "2026-03-04": "Full moon",
    "2026-03-11": "Last quarter",
    "2026-03-19": "New moon",
    "2026-03-26": "First quarter",
    "2026-04-02": "Full moon",
    "2026-04-10": "Last quarter",
    "2026-04-18": "New moon",
    "2026-04-24": "First quarter",
    "2026-05-02": "Full moon",
    "2026-05-10": "Last quarter",
    "2026-05-17": "New moon",
    "2026-05-23": "First quarter",
    "2026-05-31": "Full moon",
    "2026-06-08": "Last quarter",
    "2026-06-15": "New moon",
    "2026-06-22": "First quarter",
    "2026-06-30": "Full moon",
    "2026-07-08": "Last quarter",
    "2026-07-15": "New moon",
    "2026-07-21": "First quarter",
    "2026-07-30": "Full moon",
    "2026-08-06": "Last quarter",
    "2026-08-13": "New moon",
    "2026-08-20": "First quarter",
    "2026-08-28": "Full moon",
    "2026-09-04": "Last quarter",
    "2026-09-11": "New moon",
    "2026-09-19": "First quarter",
    "2026-09-27": "Full moon",
    "2026-10-04": "Last quarter",
    "2026-10-11": "New moon",
    "2026-10-19": "First quarter",
    "2026-10-26": "Full moon",
    "2026-11-02": "Last quarter",
    "2026-11-09": "New moon",
    "2026-11-17": "First quarter",
    "2026-11-25": "Full moon",
    "2026-12-01": "Last quarter",
    "2026-12-09": "New moon",
    "2026-12-17": "First quarter",
    "2026-12-24": "Full moon",
    "2026-12-31": "Last quarter",
    "2027-01-08": "New moon",
    "2027-01-16": "First quarter",
    "2027-01-23": "Full moon",
    "2027-01-29": "Last quarter",
    "2027-02-07": "New moon",
    "2027-02-14": "First quarter",
    "2027-02-21": "Full moon",
    "2027-02-28": "Last quarter",
    "2027-03-08": "New moon",
    "2027-03-16": "First quarter",
    "2027-03-22": "Full moon",
    "2027-03-30": "Last quarter",
    "2027-04-07": "New moon",
    "2027-04-14": "First quarter",
    "2027-04-21": "Full moon",
    "2027-04-29": "Last quarter",
    "2027-05-06": "New moon",
    "2027-05-13": "First quarter",
    "2027-05-20": "Full moon",
    "2027-05-29": "Last quarter",
    "2027-06-05": "New moon",
    "2027-06-11": "First quarter",
    "2027-06-19": "Full moon",
    "2027-06-27": "Last quarter",
    "2027-07-04": "New moon",
    "2027-07-11": "First quarter",
    "2027-07-19": "Full moon",
    "2027-07-27": "Last quarter",
    "2027-08-03": "New moon",
    "2027-08-09": "First quarter",
    "2027-08-17": "Full moon",
    "2027-08-25": "Last quarter",
    "2027-09-01": "New moon",
    "2027-09-08": "First quarter",
    "2027-09-16": "Full moon",
    "2027-09-23": "Last quarter",
    "2027-09-30": "New moon",
    "2027-10-07": "First quarter",
    "2027-10-16": "Full moon",
    "2027-10-23": "Last quarter",
    "2027-10-30": "New moon",
    "2027-11-06": "First quarter",
    "2027-11-14": "Full moon",
    "2027-11-21": "Last quarter",
    "2027-11-28": "New moon",
    "2027-12-06": "First quarter",
    "2027-12-14": "Full moon",
    "2027-12-20": "Last quarter",
    "2027-12-28": "New moon",
    "2028-01-05": "First quarter",
    "2028-01-12": "Full moon",
    "2028-01-19": "Last quarter",
    "2028-01-27": "New moon",
    "2028-02-04": "First quarter",
    "2028-02-11": "Full moon",
    "2028-02-17": "Last quarter",
    "2028-02-25": "New moon",
    "2028-03-04": "First quarter",
    "2028-03-11": "Full moon",
    "2028-03-18": "Last quarter",
    "2028-03-26": "New moon",
    "2028-04-03": "First quarter",
    "2028-04-09": "Full moon",
    "2028-04-17": "Last quarter",
    "2028-04-25": "New moon",
    "2028-05-02": "First quarter",
    "2028-05-09": "Full moon",
    "2028-05-16": "Last quarter",
    "2028-05-24": "New moon",
    "2028-05-31": "First quarter",
    "2028-06-07": "Full moon",
    "2028-06-15": "Last quarter",
    "2028-06-23": "New moon",
    "2028-06-30": "First quarter",
    "2028-07-07": "Full moon",
    "2028-07-15": "Last quarter",
    "2028-07-22": "New moon",
    "2028-07-29": "First quarter",
    "2028-08-05": "Full moon",
    "2028-08-13": "Last quarter",
    "2028-08-21": "New moon",
    "2028-08-27": "First quarter",
    "2028-09-04": "Full moon",
    "2028-09-12": "Last quarter",
    "2028-09-19": "New moon",
    "2028-09-26": "First quarter",
    "2028-10-04": "Full moon",
    "2028-10-11": "Last quarter",
    "2028-10-18": "New moon",
    "2028-10-25": "First quarter",
    "2028-11-02": "Full moon",
    "2028-11-10": "Last quarter",
    "2028-11-17": "New moon",
    "2028-11-24": "First quarter",
    "2028-12-02": "Full moon",
    "2028-12-09": "Last quarter",
    "2028-12-16": "New moon",
    "2028-12-24": "First quarter",
    "2029-01-01": "Full moon",
    "2029-01-08": "Last quarter",
    "2029-01-15": "New moon",
    "2029-01-23": "First quarter",
    "2029-01-30": "Full moon",
    "2029-02-06": "Last quarter",
    "2029-02-13": "New moon",
    "2029-02-22": "First quarter",
    "2029-03-01": "Full moon",
    "2029-03-07": "Last quarter",
    "2029-03-15": "New moon",
    "2029-03-23": "First quarter",
    "2029-03-30": "Full moon",
    "2029-04-06": "Last quarter",
    "2029-04-14": "New moon",
    "2029-04-22": "First quarter",
    "2029-04-29": "Full moon",
    "2029-05-05": "Last quarter",
    "2029-05-14": "New moon",
    "2029-05-21": "First quarter",
    "2029-05-28": "Full moon",
    "2029-06-04": "Last quarter",
    "2029-06-12": "New moon",
    "2029-06-19": "First quarter",
    "2029-06-26": "Full moon",
    "2029-07-04": "Last quarter",
    "2029-07-12": "New moon",
    "2029-07-19": "First quarter",
    "2029-07-26": "Full moon",
    "2029-08-02": "Last quarter",
    "2029-08-10": "New moon",
    "2029-08-17": "First quarter",
    "2029-08-24": "Full moon",
    "2029-09-01": "Last quarter",
    "2029-09-08": "New moon",
    "2029-09-15": "First quarter",
    "2029-09-23": "Full moon",
    "2029-10-01": "Last quarter",
    "2029-10-08": "New moon",
    "2029-10-14": "First quarter",
    "2029-10-22": "Full moon",
    "2029-10-30": "Last quarter",
    "2029-11-06": "New moon",
    "2029-11-13": "First quarter",
    "2029-11-21": "Full moon",
    "2029-11-29": "Last quarter",
    "2029-12-06": "New moon",
    "2029-12-13": "First quarter",
    "2029-12-21": "Full moon",
    "2029-12-28": "Last quarter",
    "2030-01-04": "New moon",
    "2030-01-12": "First quarter",
    "2030-01-20": "Full moon",
    "2030-01-27": "Last quarter",
    "2030-02-03": "New moon",
    "2030-02-10": "First quarter",
    "2030-02-18": "Full moon",
    "2030-02-25": "Last quarter",
    "2030-03-04": "New moon",
    "2030-03-12": "First quarter",
    "2030-03-20": "Full moon",
    "2030-03-26": "Last quarter",
    "2030-04-03": "New moon"
    }

def get_moon_phase(year, month, day):
    """Return the icon and the description of the moon phase for given day"""
    date_str = f"{year}-{month:02}-{day:02}"
    if date_str not in moon_phases:
        return ""
    if moon_phases[date_str] == "New moon":
        return " 🌑"
    elif moon_phases[date_str] == "First quarter":
        return " 🌓"
    elif moon_phases[date_str] == "Full moon":
        return " 🌕"
    elif moon_phases[date_str] == "Last quarter":
        return " 🌗"
    else:
        return ""
