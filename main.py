from api.amsterdam_api import AmsterdamApi
import statistics


def main():
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

    print("\nTotal amount of trash bins : ", list_trash_bins.__len__())
    print("Total amount of Papier trash bins : ", sum(trash_bin['type'] == 'Papier' for trash_bin in list_trash_bins))
    print("Total amount of Rest trash bins : ", sum(trash_bin['type'] == 'Rest' for trash_bin in list_trash_bins))
    print("Average id number : ", statistics.mean(trash_bin['id'] for trash_bin in list_trash_bins), "\n")

    for monument in list_monuments:
        print(
            str(monument['id']) + "\t" +
            monument['address']
        )


if __name__ == "__main__":
    main()
