__author__ = 'dongnanzhy'

from RiotAPI import RiotAPI

def main():
    api = RiotAPI('57da0ecc-8a65-48f8-9881-c0f7c9d4bd18')
    r = api.get_summoner_by_name('lazylearning')
    print r

if __name__ == '__main__':
    main()