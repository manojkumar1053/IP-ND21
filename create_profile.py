def create_profile(given_name, *surnames, **details):
    print(given_name, *surnames)
    for key, value in details.items():
        print(key, value, sep=':')


if __name__ == '__main__':
    create_profile("sam")
    create_profile("Martin", "Luther", "King", "Jr.", born=1929, died=1996)
    create_profile("James", "bond", cofounder="007")
