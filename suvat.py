import requests as rq


def GetUniverseId(GameId):
    try:
        return rq.get(
            f"https://apis.roblox.com/universes/v1/places/{GameId}/universe"
        ).json()["universeId"]
    except Exception as nv:
        print(f"An error occured, See: {nv}")


def ThumbnailUrl(UniverseId):
    try:
        return rq.get(
            f"https://thumbnails.roblox.com/v1/games/icons?universeIds={UniverseId}&returnPolicy=PlaceHolder&size=512x512&format=Png&isCircular=false"
        ).json()["data"][0]["imageUrl"]
    except Exception as nv:
        print(f"An error occured, See: {nv}")


def GameCreatorName(UniverseId):
    try:
        return rq.get(
            f"https://games.roblox.com/v1/games?universeIds={UniverseId}"
        ).json()["data"][0]["creator"]["name"]
    except Exception as nv:
        print(f"An error occured, See: {nv}")


def GameName(UniverseId):
    try:
        return rq.get(
            f"https://games.roblox.com/v1/games?universeIds={UniverseId}"
        ).json()["data"][0]["name"]
    except Exception as nv:
        print(f"An error occured, See: {nv}")


def GameDescription(UniverseId):
    try:
        return rq.get(
            f"https://games.roblox.com/v1/games?universeIds={UniverseId}"
        ).json()["data"][0]["description"]
    except Exception as nv:
        print(f"An error occured, See: {nv}")


def GameVisits(UniverseId):
    try:
        return rq.get(
            f"https://games.roblox.com/v1/games?universeIds={UniverseId}"
        ).json()["data"][0]["visits"]
    except Exception as nv:
        print(f"An error occured, See: {nv}")


def IsGameVerified(UniverseId):
    try:
        return rq.get(
            f"https://games.roblox.com/v1/games?universeIds={UniverseId}"
        ).json()["data"][0]["creator"]["hasVerifiedBadge"]
    except Exception as nv:
        print(f"An error occured, See: {nv}")


def VipServersAllowed(UniverseId):
    try:
        return rq.get(
            f"https://games.roblox.com/v1/games?universeIds={UniverseId}"
        ).json()["data"][0]["createVipServersAllowed"]
    except Exception as nv:
        print(f"An error occured, See: {nv}")


def Genre(UniverseId):
    try:
        return rq.get(
            f"https://games.roblox.com/v1/games?universeIds={UniverseId}"
        ).json()["data"][0]["genre"]
    except Exception as nv:
        print(f"An error occured, See: {nv}")


def GameOwnerAccountOrGroup(UniverseId):
    try:
        return rq.get(
            f"https://games.roblox.com/v1/games?universeIds={UniverseId}"
        ).json()["data"][0]["creator"]["type"]
    except Exception as nv:
        print(f"An error occured, See: {nv}")


def CreationDate(UniverseId):
    try:
        return rq.get(
            f"https://games.roblox.com/v1/games?universeIds={UniverseId}"
        ).json()["data"][0]["created"][:10]
    except Exception as nv:
        print(f"An error occured, See: {nv}")


def MaxPlayersAllowed(UniverseId):
    try:
        return rq.get(
            f"https://games.roblox.com/v1/games?universeIds={UniverseId}"
        ).json()["data"][0]["maxPlayers"]
    except Exception as nv:
        print(f"An error occured, See: {nv}")


def FavoritedCount(UniverseId):
    try:
        return rq.get(
            f"https://games.roblox.com/v1/games?universeIds={UniverseId}"
        ).json()["data"][0]["favoritedCount"]
    except Exception as nv:
        print(f"An error occured, See: {nv}")


def LastUpdated(UniverseId):
    try:
        return rq.get(
            f"https://games.roblox.com/v1/games?universeIds={UniverseId}"
        ).json()["data"][0]["updated"][:10]
    except Exception as nv:
        print(f"An error occured, See: {nv}")


def SupportedLang(UniverseId):
    try:
        data = rq.get(
            f"https://gameinternationalization.roblox.com/v2/supported-languages/games/{UniverseId}"
        ).json()
        nms = ", ".join(language["languageFamily"]["name"] for language in data["data"])
        return nms
    except Exception as nv:
        print(f"An error occured, See: {nv}")


def AvatarType(UniverseId):
    avtype = rq.get(
        f"https://games.roblox.com/v1/games?universeIds={UniverseId}"
    ).json()["data"][0]["universeAvatarType"]
    if "MorphToR6" in avtype:
        return "R6"
    elif "MorphToR15" in avtype:
        return "R15"
    else:
        return "All"
