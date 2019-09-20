from api.amsterdam_api import AmsterdamApi
from api.ns_api import NSApi
import statistics


def trash_bins():
    amsterdam_api = AmsterdamApi()
    list_trash_bins = amsterdam_api.get_trash_bins()
    list_monuments = amsterdam_api.get_monuments()

    print("Overview of trash bins in Amsterdam")

    for trash_bin in list_trash_bins:
        print(
            str(trash_bin['id']) + "\t" +
            trash_bin['name'] + "\t" +
            trash_bin['type'] + "\t" +
            trash_bin['address']
        )

    print("\nTotal amount of trash bins : ", len(list_trash_bins))
    print("Total amount of Papier trash bins : ", sum(trash_bin['type'] == 'Papier' for trash_bin in list_trash_bins))
    print("Total amount of Rest trash bins : ", sum(trash_bin['type'] == 'Rest' for trash_bin in list_trash_bins))
    print("Average id number : ", statistics.mean(trash_bin['id'] for trash_bin in list_trash_bins), "\n")

    for monument in list_monuments:
        print(
            str(monument['id']) + "\t" +
            monument['address']
        )


def main():
    ns_api = NSApi()
    list_train_stations = ns_api.get_train_stations()
    list_disruptions = ns_api.get_disruptions()

    disrupted_stations = []
    amount_of_stations_affected = 0

    # Create list of all stations, duplicates possible, that are affected by the disruptions
    for disruption in list_disruptions:
        for station in disruption['stations']:
            disrupted_stations.append(station)

    count_disruptions_per_station = []
    # Count how many times a station occurs in the disruptions list and add it to count_disruptions
    for station in list_train_stations:
        if station['code'].lower() in disrupted_stations:
            amount_of_stations_affected += 1
            count_disruptions_per_station.append({
                'code': station['code'].lower(),
                'disruptions': disrupted_stations.count(station['code'].lower()),
                'name': station['name']
            })

    # Sort by disruption
    count_disruptions_per_station.sort(key=sort_by_disruption, reverse=True)

    print(str(len(count_disruptions_per_station)) + " van de " + str(len(list_train_stations)) +
          " (" + '{0:.3g}'.format(percentage(len(count_disruptions_per_station), len(list_train_stations))) +
          "%) stations zijn beinvloed door vertraging.\nDe volgende 10 stations hebben het meeste last van "
          "vertragingen:\n")
    # Print top 10 of most disrupted stations (nicely)
    for station in count_disruptions_per_station[0:10]:
        print('{:<20s}{}'.format(station['name'], str(station['disruptions'])))


def sort_by_disruption(val):
    return val['disruptions']


def percentage(part, whole):
    return 100 * float(part)/float(whole)


if __name__ == "__main__":
    main()
