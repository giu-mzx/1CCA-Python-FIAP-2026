musicas = [
    ["Chicago", "Michael Jackson"],
    ["Sorry", "Justin Bieber"],
    ["Judas", "Lady Gaga"]
]

print(musicas[1][0])

print()

for musica in musicas:
    for info in musica:
        print(info)
    print()

for musica in musicas:
    print(f"{musica[0]} - {musica[1]}")