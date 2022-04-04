import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

import discord
import os
from discord.ext import commands
from datetime import datetime
import typing
from utils.assets import Assets
from utils.data import Data
from utils.pie import Pie

class info(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.covidInfo = Data.getData()


    @commands.command(name = "info", aliases = ["covid"])
    async def _info(self, ctx, *, countryName: str):
        

        countryName = countryName.capitalize()
        try:
            tmp = self.covidInfo[countryName]
        except:
            await ctx.send(f"{Assets.red_tick} **Invalid Input Provided**")
            return

        totalCasesInt = int(self.covidInfo[countryName]['TotalCases'].replace(',', '').replace('N/A', '0'))
        activeCasesInt = int(self.covidInfo[countryName]['ActiveCases'].replace(',', '').replace('N/A', '0'))
        totalRecoveredInt = int(self.covidInfo[countryName]['TotalRecovered'].replace(',', '').replace('N/A', '0'))
        totalDeathsInt = int(self.covidInfo[countryName]['TotalDeaths'].replace(',', '').replace('N/A', '0'))
        popCount = int(self.covidInfo[countryName]['TotalCases'].replace(",", ""))//int(self.covidInfo[countryName]['TotCases/1M pop'].replace(",", ""))

        embed = discord.Embed(
            title = f"Covid statistics for {countryName}:",
            description = "/1M: per 1 million people",
            color = 0xe67e22,
            timestamp = ctx.message.created_at
        )
        
        embed.add_field(
            name = "Population (Approx.)",
            value = f"{popCount} million" + ("s" if popCount > 1 else ""),
            inline = True
        )
        embed.add_field(
            name = "Total Cases",
            value = f"{totalCasesInt}",
            inline = True
        )
        
        embed.add_field(
            name = "Total Cases/1M",
            value = f"{self.covidInfo[countryName]['TotCases/1M pop'].replace(',', '').replace('N/A', '0')}",
            inline = True
        )

        embed.add_field(
            name = "Active Cases",
            value = f"{activeCasesInt}",
            inline = True
        )
        embed.add_field(
            name = "Total Recovered",
            value = f"{totalRecoveredInt}",
            inline = True
        )
        embed.add_field(
            name = "Total Deaths",
            value = f"{totalDeathsInt}",
            inline = True
        )
        embed.add_field(
            name = "Active Cases/1M",
            value = f"{activeCasesInt//popCount}",
            inline = True
        )
        embed.add_field(
            name = "Total Recovered/1M",
            value = f"{totalRecoveredInt//popCount}",
            inline = True
        )
        embed.add_field(
            name = "Total Deaths/1M",
            value = f"{self.covidInfo[countryName]['Deaths/1M pop']}",
            inline = True
        )

        embed.set_footer(
            text = ctx.author,
            icon_url = ctx.author.avatar_url
        )

        Pie(activeCasesInt, totalRecoveredInt, totalDeathsInt).pieChart()

        file = discord.File("./potato.png", filename = "potato.png")
        embed.set_image(
            url = "attachment://potato.png"
        )

        await ctx.send(file = file, embed = embed)
        


def setup(client):
    client.add_cog(info(client))
