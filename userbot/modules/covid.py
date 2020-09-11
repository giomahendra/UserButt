# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Port to UserBot by @MoveAngel

from covid import Covid
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.covid (.*)")
async def corona(event):
    await event.edit("`Processing...`")
    input = event.pattern_match.group(1)
    country = input.capitalize()
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
        confirm = "{:,}".format(int(country_data['confirmed']))
        active = "{:,}".format(int(country_data['active']))
        deaths = "{:,}".format(int(country_data['deaths']))
        recovered = "{:,}".format(int(country_data['recovered']))
        newcases = "{:,}".format(int(country_data['new_cases']))
        newdeaths = "{:,}".format(int(country_data['new_deaths']))
        critical = "{:,}".format(int(country_data['critical']))
        totaltests = "{:,}".format(int(country_data['total_tests']))
        output_text = (
            f"`Confirmed   : {confirm}`\n" +
            f"`Active      : {active}`\n" +
            f"`Deaths      : {deaths}`\n" +
            f"`Recovered   : {recovered}`\n\n" +
            f"`New Cases   : {newcases}`\n" +
            f"`New Deaths  : {newdeaths}`\n" +
            f"`Critical    : {critical}`\n" +
            f"`Total Tests : {totaltests}`\n\n" +
            f"`Data provided by` [Worldometer](https://www.worldometers.info/coronavirus/country/{country})")
        await event.edit(f"`Corona Virus Info in {country} :`\n\n{output_text}")
    except ValueError:
        await event.edit(f"No information found for: {country}!")


CMD_HELP.update({
    "covid":
    "`.covid` <country>"
    "\nUsage: Get an information about data covid-19 in your country."
})
