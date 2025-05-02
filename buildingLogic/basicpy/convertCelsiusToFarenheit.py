
#below i defined a function for converting celsius to farenheit
#and also showed about how to use argparse which is used to parse command line arguments


def ConvertCelsiusToFarenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32

if __name__=="__main__":
    import argparse
    parse=argparse.ArgumentParser(description="Convert Celsius to Fahrenheit")
    parse.add_argument(
        "-c","--celsius",metavar="celsius",type=float,help="Enter temperature in Celsius"
    )
    args=parse.parse_args()
    
    if args.celsius is not None:
        fahrenheit = ConvertCelsiusToFarenheit(args.celsius)
        print(f"{args.celsius}°C is equal to {fahrenheit}°F")
    else:
        print("Please provide a temperature in Celsius using -c or --celsius.")
