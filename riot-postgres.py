#pip3 install riotwatcher
#python3 riot_player_stats.py <api_key>  <player_name>
from riotwatcher import LolWatcher, ApiError
import sys
import json
import psycopg2

class LoL(object):
    def __init__(self, api_key, player_name, connection):
        #Riotwater Info
        self.api_key = api_key
        self.player_name = player_name
        self.my_region = 'na1'

        #Riotwatcher APIs Endpoints
        lol_watcher = LolWatcher(self.api_key)
        self.summoner = lol_watcher.summoner.by_name(self.my_region, self.player_name)
        self.league = lol_watcher.league.by_summoner(self.my_region, self.summoner['id'])

        #Psycopg2 connection
        self.connection = connection
        self.cursor = connection.cursor()

    def summoner_by_name(self):

        create_table =  """
                    CREATE TABLE IF NOT EXISTS summoner_by_name (
                    ids             TEXT     NOT NULL,
                    accountIds      TEXT     NOT NULL,
                    puuid           TEXT     NOT NULL,
                    name            TEXT     NOT NULL,
                    profileIconId   TEXT     NOT NULL,
                    revisionDate    TEXT     NOT NULL,
                    summonerLevel   TEXT     NOT NULL);
                    """

        insert_query =  """
                    INSERT INTO summoner_by_name
                    VALUES (%(id)s, %(accountId)s, %(puuid)s, %(name)s, %(profileIconId)s, %(revisionDate)s, %(summonerLevel)s)
                    """

        ###Create table
        self.cursor.execute(create_table)
        self.connection.commit()
        print("Table created successfully in PostgreSQL ")

        ###Insert record
        self.cursor.execute(insert_query, self.summoner)
        self.connection.commit()
        print("Records inserted successfully")

        # Fetch result
        self.cursor.execute("SELECT * from summoner_by_name")
        record = self.cursor.fetchall()
        print("Result ", record)


    def league_by_summoner(self):
        # find "queueType": "RANKED_SOLO_5x5"
        for x in range(len(self.league)):
            if self.league[x]['queueType'] == "RANKED_SOLO_5x5":
                ranked_solo = self.league[x]
                print(ranked_solo)

        create_table =  """
                    CREATE TABLE IF NOT EXISTS league_by_summoner (
                    leagueId        TEXT     NOT NULL,
                    queueType       TEXT     NOT NULL,
                    tier            TEXT     NOT NULL,
                    rank            TEXT     NOT NULL,
                    summonerId      TEXT     NOT NULL,
                    summonerName    TEXT     NOT NULL,
                    wins            TEXT     NOT NULL,
                    losses          TEXT     NOT NULL,
                    veteran         BOOLEAN     NOT NULL,
                    inactive        BOOLEAN     NOT NULL,
                    freshBlood      BOOLEAN     NOT NULL,
                    hotStreak       BOOLEAN     NOT NULL);
                    """

        insert_query =  """
                    INSERT INTO league_by_summoner
                    VALUES (%(leagueId)s, %(queueType)s, %(tier)s, %(rank)s, %(summonerId)s, %(summonerName)s, %(wins)s,%(losses)s, %(veteran)s, %(inactive)s, %(freshBlood)s, %(hotStreak)s  )
                    """

        ###Create table
        self.cursor.execute(create_table)
        self.connection.commit()
        print("Table created successfully in PostgreSQL ")

        ###Insert record
        self.cursor.execute(insert_query, ranked_solo)
        self.connection.commit()
        print("Records inserted successfully")

        # Fetch result
        self.cursor.execute("SELECT * from league_by_summoner")
        record = self.cursor.fetchall()
        print("Result ", record)

def main():
    connection = psycopg2.connect( user="admin", password="password123!", host="35.202.173.137", port="5432", database="my-postgres")
    summoner = LoL(sys.argv[1], sys.argv[2], connection)
    summoner.summoner_by_name()
    summoner.league_by_summoner()


if __name__ == "__main__":
	sys.argv[:]
	main()
