"""Descarga de Scryfall las imágenes, el texto y los rulings de las cartas que usa la app.

Guarda todo en cards/: las imágenes (art_crop y normal) y cards.json con los datos.
Se corre desde GitHub Actions (.github/workflows/scryfall.yml).
"""
import json
import pathlib
import time
import urllib.parse
import urllib.request

API = "https://api.scryfall.com"
HEADERS = {"User-Agent": "prowesstracker/1.0 (github.com/GabrielConforte/prowesstracker)", "Accept": "application/json"}
OUT = pathlib.Path(__file__).resolve().parent.parent / "cards"

# clave en la app -> nombre en Scryfall
CARDS = {
    "swiftspear": "Monastery Swiftspear",
    "slickshot": "Slickshot Show-Off",
    "drc": "Dragon's Rage Channeler",
    "cutter": "Cori-Steel Cutter",
    "rage": "Monstrous Rage",
}
# fichas que se buscan entre las partes relacionadas de otra carta: clave -> (carta, nombre de la ficha)
TOKENS = {
    "monk": ("cutter", "Monk"),
    "role": ("rage", "Monster"),
}


def get(url, binary=False):
    req = urllib.request.Request(url, headers=HEADERS if not binary else {"User-Agent": HEADERS["User-Agent"]})
    with urllib.request.urlopen(req, timeout=30) as res:
        data = res.read()
    time.sleep(0.12)  # Scryfall pide 50-100 ms entre pedidos
    return data if binary else json.loads(data)


def spanish(name):
    q = urllib.parse.quote(f'!"{name}" lang:es')
    try:
        found = get(f"{API}/cards/search?q={q}&unique=prints")
    except Exception:
        return None
    for card in found.get("data", []):
        if card.get("printed_text") or card.get("printed_name"):
            return {
                "name": card.get("printed_name"),
                "type_line": card.get("printed_type_line"),
                "text": card.get("printed_text"),
            }
    return None


def images(card):
    uris = card.get("image_uris") or (card.get("card_faces") or [{}])[0].get("image_uris") or {}
    return uris.get("art_crop"), uris.get("normal")


def save(key, card):
    art_url, full_url = images(card)
    # Cartas de dos caras (como los roles): se usa la primera cara.
    face = card if card.get("oracle_text") is not None or not card.get("card_faces") else card["card_faces"][0]
    entry = {
        "name": face["name"],
        "mana_cost": face.get("mana_cost", ""),
        "type_line": face.get("type_line", ""),
        "oracle_text": face.get("oracle_text", ""),
        "power": card.get("power"),
        "toughness": card.get("toughness"),
        "set_name": card.get("set_name"),
        "artist": card.get("artist"),
        "scryfall_uri": card.get("scryfall_uri"),
        "es": spanish(card["name"]) if "Token" not in card.get("type_line", "") else None,
        "rulings": [
            {"date": r["published_at"], "text": r["comment"]}
            for r in get(card["rulings_uri"]).get("data", [])
        ],
    }
    for kind, url in (("art", art_url), ("full", full_url)):
        if url:
            path = OUT / f"{key}-{kind}.jpg"
            path.write_bytes(get(url, binary=True))
            entry[kind] = f"cards/{path.name}"
    return entry


def main():
    OUT.mkdir(exist_ok=True)
    data, raw = {}, {}
    for key, name in CARDS.items():
        card = get(f"{API}/cards/named?exact={urllib.parse.quote(name)}")
        raw[key] = card
        data[key] = save(key, card)
        print("ok", key, card["name"], len(data[key]["rulings"]), "rulings")
    for key, (parent, token_name) in TOKENS.items():
        part = next((p for p in raw[parent].get("all_parts", [])
                     if p["component"] == "token" and p["name"].lower().startswith(token_name.lower())), None)
        if not part:
            print("no token", key)
            continue
        card = get(part["uri"])
        data[key] = save(key, card)
        print("ok", key, card["name"])
    (OUT / "cards.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
