#!/usr/bin/env python3

from typing import List, Optional


class Attendee:
    def __init__(self, name: str):
        self.name: str = name
        self.subtotal: Optional[float] = None
        self.tax_portion: Optional[float] = None
        self.tip_portion: Optional[float] = None
        self._total: Optional[float] = None

    @property
    def total(self):
        self._total = self.subtotal + self.tax_portion + self.tip_portion
        return self._total

    def calculate_subtotal(self, bill_amounts: str):
        """Calculate subtotal from comma-separated string."""
        bill_amounts = [float(i.strip()) for i in bill_amounts.split(',')]
        subtotal = sum(bill_amounts)
        self.subtotal = subtotal
        return subtotal


class TaxCalculator:
    def __init__(self, tax_amount: float, tip_amount: float, attendees: List[Attendee]):
        self.tax= tax_amount
        self.tip = tip_amount
        self.attendees: List[Attendee] = attendees

        self._event_total: float = 0.0
        self._group_subtotal: float = 0.0

    def calculate(self):
        for attendee in self.attendees:
            self._group_subtotal += attendee.subtotal
        for attendee in self.attendees:
            attendee.tax_portion = self._calculate_tax_per(attendee)
            attendee.tip_portion = self._calculate_tip_per(attendee)

    def _calculate_tax_per(self, attendee: Attendee):
        return self.tax * attendee.subtotal / self._group_subtotal

    def _calculate_tip_per(self, attendee: Attendee):
        return self.tip * attendee.subtotal / self._group_subtotal

    @property
    def event_total(self):
        total = 0
        for attendee in self.attendees:
            total = total + attendee.total
        self._event_total = total
        return self._event_total

    def display_totals(self):
        print('\n')
        print(f"Subtotal: {round(self._group_subtotal, 2)}")
        for attendee in self.attendees:
            print(
                attendee.name 
                + ' | TAX: ' + str(round(attendee.tax_portion, 2)) 
                + ' | TIP: ' + str(round(attendee.tip_portion, 2)) 
                + ' | TOTAL: ' + str(round(attendee.total, 2))
            )
        print(f"Total bill: {round(self.event_total, 2)}")

