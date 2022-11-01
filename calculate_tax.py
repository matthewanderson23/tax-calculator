#!/usr/bin/env python3

from tax_calculator import Attendee, TaxCalculator


def _split_by_comma_and_remove_whitespace(string: str):
    new = string.strip().split(',')
    new = ' '.join(new).split()
    return new


def ask_for_attendees():
    prompt = "Enter the names of attendees at the event, separated by commas: "
    attendees_str = input(prompt)
    attendees = _split_by_comma_and_remove_whitespace(attendees_str)
    return attendees


def prompt_for_subtotal(attendee: Attendee):
    prompt = f"Enter the amount of each item for {attendee.name}, separated by commas: "
    amounts_str = input(prompt)
    amounts = _split_by_comma_and_remove_whitespace(amounts_str)
    subtotal = sum([float(eval(i)) for i in amounts])
    return subtotal


def prompt_for_tax():
    tax = float(input("What was the amount in taxes paid? "))
    return tax


def prompt_for_tips():
    tips = float(input("What was the amount in tips/gratuities paid? "))
    return tips


def prompt_for_discounts():
    prompt = "What was the amount in discounts applied? (Will be applied to whole bill) "
    amt_discount = float(input(prompt))
    return amt_discount


def main():
    people = ask_for_attendees()
    
    attendees: List[Attendee] = []
    for name in people:
        attendee = Attendee(name)
        attendee.subtotal = prompt_for_subtotal(attendee)
        attendees.append(attendee)

    tax = prompt_for_tax()
    tips = prompt_for_tips()
    amt_discount = prompt_for_discounts()

    tc = TaxCalculator(tax, tips - amt_discount, attendees)
    tc.calculate()
    tc.display_totals()


if __name__ == "__main__":
    main()

