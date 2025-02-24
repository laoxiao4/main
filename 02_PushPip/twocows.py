#!/home/lee/python2025/bin/python

import argparse
import cowsay

def main():
    parser = argparse.ArgumentParser(description="Two Cowsay: Display two cows with messages.")

    parser.add_argument("message1", type=str, help="First message for the first cow.")

    parser.add_argument("message2", type=str, help="Second message for the second cow.")

    parser.add_argument("-e", "--eyes1", type=str, default="oo", help="Eyes for the first cow.")
    parser.add_argument("-f", "--cowfile1", type=str, default="default", help="Cowfile for the first cow.")
    parser.add_argument("-n", "--tongue1", type=str, default="  ", help="Tongue for the first cow.")

    parser.add_argument("-E", "--eyes2", type=str, default="oo", help="Eyes for the second cow.")
    parser.add_argument("-F", "--cowfile2", type=str, default="default", help="Cowfile for the second cow.")
    parser.add_argument("-N", "--tongue2", type=str, default="  ", help="Tongue for the second cow.")

    args = parser.parse_args()

    cow1 = cowsay.get_output_string(
        args.cowfile1,
        args.message1
    )

    cow2 = cowsay.get_output_string(
        args.cowfile2,
        args.message2
    )

    print(cow1)
    print(cow2)

if __name__ == "__main__":
    main()
