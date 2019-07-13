def main():
    # имена штатов
    states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
    # радиостанции : {покрывают штаты}
    stations = {
        'kone': {'id', 'nv', 'ut'},
        'ktwo': {'wa', 'id', 'mt'},
        'kthree': {'or', 'nv', 'ca'},
        'kfour': {'nv', 'ut'},
        'kfive': {'ca', 'az'}
    }

    # окончательноме множество радиостанций
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = set()
        for station_name, states in stations.items():
            print(station_name + ' / ' + ', '.join(states))
            # штаты из списка необходимых, которые покрывает радиостанция
            covered = states_needed & states
            # поиск радиостанции с самым большим покрытием
            if len(covered) > len(states_covered):
                best_station = station_name
                states_covered = covered
        # убрать штаты покрываетмые best_station из списка необходимых
        states_needed -= states_covered
        final_stations.add(best_station)

    print(final_stations)


if __name__ == '__main__':
    main()
