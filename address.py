#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: May 10, 2022
# This program gets many parameters and then formats your shipping address


def format_address(
    name, street_number, street_name, city, province, postal_code, apartment_number=None
):
    # format the address
    if apartment_number != None:
        format_address = (
            name
            + " \n"
            + apartment_number
            + "-"
            + street_number
            + " "
            + street_name
            + " \n"
            + city
            + " "
            + province
            + " "
            + postal_code
        )
    else:
        format_address = (
            name
            + " \n"
            + street_number
            + " "
            + street_name
            + " \n"
            + city
            + " "
            + province
            + " "
            + postal_code
        )

    return format_address


def main():
    # get a users address info and print it out
    apartment_number = None

    # get all the credentials
    name = input("Enter your name: ")
    question = input("Do you live in an apartment? (y/n): ")
    if question == "y" or question == "yes":
        apartment_number = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input(
        "Enter your street name AND type (Main St., Heron Road, etc.): "
    )
    city = input("Enter your city: ")
    province = input(
        "Enter your province (as an abbreviation, i.e. ON, QC, BC, etc.): "
    )
    postal_code = input("Enter your postal code (K3L 9H2): ")
    print("")

    # if the user does lives in an apartment then it will format with the apartment address
    if apartment_number != None:
        address = format_address(
            name,
            street_number,
            street_name,
            city,
            province,
            postal_code,
            apartment_number,
        )
    # If the user does not live in an apartment then it will format without the apartment address
    else:
        address = format_address(
            name, street_number, street_name, city, province, postal_code
        )

    # display the output
    print("Your canadian mailing address is: ")
    print(address)


if __name__ == "__main__":
    main()
