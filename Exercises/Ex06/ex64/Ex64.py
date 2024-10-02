class Station:
    def __init__(self, name="", latitude=0.0, longitude=0.0):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"站名: {self.name}, 緯度: {self.latitude}, 經度: {self.longitude}"

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


def main():
    stations = set()
    go = True
    while go:
        name = input("站名: ")
        latitude = float(input("緯度: "))
        longitude = float(input("經度: "))
        station = Station(name, latitude, longitude)
        if station in stations:
            print(f"{station.name}站已經存在")
            continue
        stations.add(station)
        print(station)
        match input("繼續輸入 ( Y | y ): "):
            case "Y" | "y":
                go = True
            case _:
                go = False

    print("車站依照緯度高到低排序如下: ")
    for station in sorted(stations, key=lambda s: s.latitude, reverse=True):
        print(station)

main()
