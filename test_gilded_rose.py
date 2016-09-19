# -*- coding: utf-8 -*-
import pytest
from gilded_rose import GildedRose

def test_normal_item_before_sell_date():
    gilded_rose = GildedRose("normal", 10, 5)
    gilded_rose.tick()

    assert 9 == gilded_rose.quality
    assert 4 == gilded_rose.days_remaining

def test_normal_item_on_sell_date():
    gilded_rose = GildedRose("normal", 10, 0)
    gilded_rose.tick()

    assert 8 == gilded_rose.quality
    assert -1 == gilded_rose.days_remaining

def test_normal_item_after_sell_date():
    gilded_rose = GildedRose("normal", 10, -10)
    gilded_rose.tick()

    assert 8 == gilded_rose.quality
    assert -11 == gilded_rose.days_remaining

def test_normal_item_of_zero_quality():
    gilded_rose = GildedRose("normal", 0, 5)
    gilded_rose.tick()

    assert 0 == gilded_rose.quality
    assert 4 == gilded_rose.days_remaining

def test_brie_before_sell_date():
    gilded_rose = GildedRose("Aged Brie", 10, 5)
    gilded_rose.tick()

    assert 11 == gilded_rose.quality
    assert 4 == gilded_rose.days_remaining

def test_brie_before_sell_date_with_max_quality():
    gilded_rose = GildedRose("Aged Brie", 50, 5)
    gilded_rose.tick()

    assert 50 == gilded_rose.quality
    assert 4 == gilded_rose.days_remaining

def test_brie_on_sell_date():
    gilded_rose = GildedRose("Aged Brie", 10, 0)
    gilded_rose.tick()

    assert 12 == gilded_rose.quality
    assert -1 == gilded_rose.days_remaining

def test_brie_on_sell_date_near_max_quality():
    gilded_rose = GildedRose("Aged Brie", 49, 0)
    gilded_rose.tick()

    assert 50 == gilded_rose.quality
    assert -1 == gilded_rose.days_remaining

def test_brie_on_sell_date_with_max_quality():
    gilded_rose = GildedRose("Aged Brie", 50, 0)
    gilded_rose.tick()

    assert 50 == gilded_rose.quality
    assert -1 == gilded_rose.days_remaining

def test_brie_after_sell_date():
    gilded_rose = GildedRose("Aged Brie", 10, -10)
    gilded_rose.tick()

    assert 12 == gilded_rose.quality
    assert -11 == gilded_rose.days_remaining

def test_brie_after_sell_date_with_max_quality():
    gilded_rose = GildedRose("Aged Brie", 50, -10)
    gilded_rose.tick()

    assert 50 == gilded_rose.quality
    assert -11 == gilded_rose.days_remaining

def test_sulfuras_before_sell_date():
    gilded_rose = GildedRose("Sulfuras, Hand of Ragnaros", 80, 5)
    gilded_rose.tick()

    assert 80 == gilded_rose.quality
    assert 5 == gilded_rose.days_remaining

def test_sulfuras_on_sell_date():
    gilded_rose = GildedRose("Sulfuras, Hand of Ragnaros", 80, 0)
    gilded_rose.tick()

    assert 80 == gilded_rose.quality
    assert 0 == gilded_rose.days_remaining

def test_sulfuras_after_sell_date():
    gilded_rose = GildedRose("Sulfuras, Hand of Ragnaros", 80, -10)
    gilded_rose.tick()

    assert 80 == gilded_rose.quality
    assert -10 == gilded_rose.days_remaining

def test_backstage_pass_long_before_sell_date():
    gilded_rose = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 11)
    gilded_rose.tick()

    assert 11 == gilded_rose.quality
    assert 10 == gilded_rose.days_remaining

def test_backstage_pass_medium_close_to_sell_date_upper_bound():
    gilded_rose = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 10)
    gilded_rose.tick()

    assert 12 == gilded_rose.quality
    assert 9 == gilded_rose.days_remaining

def test_backstage_pass_medium_close_to_sell_date_uppper_bound_at_max_quality():
    gilded_rose = GildedRose("Backstage passes to a TAFKAL80ETC concert", 50, 10)
    gilded_rose.tick()

    assert 50 == gilded_rose.quality
    assert 9 == gilded_rose.days_remaining

def test_backstage_pass_medium_close_to_sell_date_lower_bound():
    gilded_rose = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 6)
    gilded_rose.tick()

    assert 12 == gilded_rose.quality
    assert 5 == gilded_rose.days_remaining

def test_backstage_pass_medium_close_to_sell_date_lower_bound_at_max_quality():
    gilded_rose = GildedRose("Backstage passes to a TAFKAL80ETC concert", 50, 6)
    gilded_rose.tick()

    assert 50 == gilded_rose.quality
    assert 5 == gilded_rose.days_remaining

def test_backstage_pass_very_close_to_sell_date_upper_bound():
    gilded_rose = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 5)
    gilded_rose.tick()

    assert 13 == gilded_rose.quality
    assert 4 == gilded_rose.days_remaining

def test_backstage_pass_very_close_to_sell_date_upper_bound_at_max_quality():
    gilded_rose = GildedRose("Backstage passes to a TAFKAL80ETC concert", 50, 5)
    gilded_rose.tick()

    assert 50 == gilded_rose.quality
    assert 4 == gilded_rose.days_remaining

def test_backstage_pass_very_close_to_sell_date_lower_bound():
    gilded_rose = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 1)
    gilded_rose.tick()

    assert 13 == gilded_rose.quality
    assert 0 == gilded_rose.days_remaining

def test_backstage_pass_very_close_to_sell_date_lower_bound_at_max_quality():
    gilded_rose = GildedRose("Backstage passes to a TAFKAL80ETC concert", 50, 1)
    gilded_rose.tick()

    assert 50 == gilded_rose.quality
    assert 0 == gilded_rose.days_remaining

def test_backstage_pass_on_sell_date():
    gilded_rose = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 0)
    gilded_rose.tick()

    assert 0 == gilded_rose.quality
    assert -1 == gilded_rose.days_remaining

def test_backstage_pass_after_sell_date():
    gilded_rose = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, -10)
    gilded_rose.tick()

    assert 0 == gilded_rose.quality
    assert -11 == gilded_rose.days_remaining

def test_conjured_item_before_sell_date():
    gilded_rose = GildedRose("Conjured Mana Cake", 10, 5)
    gilded_rose.tick()

    assert 8 == gilded_rose.quality
    assert 4 == gilded_rose.days_remaining

def test_conjured_item_at_zero_quality():
    gilded_rose = GildedRose("Conjured Mana Cake", 0, 5)
    gilded_rose.tick()

    assert 0 == gilded_rose.quality
    assert 4 == gilded_rose.days_remaining

def test_conjured_item_on_sell_date():
    gilded_rose = GildedRose("Conjured Mana Cake", 10, 0)
    gilded_rose.tick()

    assert 6 == gilded_rose.quality
    assert -1 == gilded_rose.days_remaining

def test_conjured_item_on_sell_date_at_zero_quality():
    gilded_rose = GildedRose("Conjured Mana Cake", 0, 0)
    gilded_rose.tick()

    assert 0 == gilded_rose.quality
    assert -1 == gilded_rose.days_remaining

def test_conjured_item_after_sell_date():
    gilded_rose = GildedRose("Conjured Mana Cake", 10, -10)
    gilded_rose.tick()

    assert 6 == gilded_rose.quality
    assert -11 == gilded_rose.days_remaining

def test_conjured_item_after_sell_date_at_zero_quality():
    gilded_rose = GildedRose("Conjured Mana Cake", 0, -10)
    gilded_rose.tick()

    assert 0 == gilded_rose.quality
    assert -11 == gilded_rose.days_remaining
