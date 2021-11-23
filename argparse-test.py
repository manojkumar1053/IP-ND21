import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Say a Greeting.")
    parser.add_argument('name', type=str)
    parser.add_argument('--city',type=str,default="RTP",help="City Name")
    args = parser.parse_args()
    name = args.name
    city = args.city
    print(f'Hello {name} from {city} !')

