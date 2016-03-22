# Let's mock some vending machine hardware!

This codebase is loosely based on the [vending machine kata](https://github.com/guyroyse/vending-machine-kata): accept coins as input and dispense products.

We've got a couple problems, though:

1. We're missing some test coverage around a couple key methods
2. We need to wire up some code for LEDs, but don't have access to the physical hardware yet.

## Get Started

1. Install dependencies: `~$ pip3 install -r requirements.txt`
2. Run tests: `~$ nosetests`

## Add Test Coverage

This legacy codebase has a few gaps in its test coverage, and we'd really like to make sure a few key scenarios are well-tested before the next big release.

You can view test coverage by running:

```
$ nosetests
...
$ open cover/index.html
```

### `input_coin`

- Write a test for `input_coin` to make sure `add_coins` is not called when an invalid coin is entered.
- Write a test for `input_coin` to make sure `add_coins` is called when a valid coin is entered
- Write a test for `input_coin` to make sure it handles empty strings correctly


### `can_purchase`

- Write a test for `can_purchase(selected_product='orange')` when fewer than 65 cents have been inserted
- Write a test for `can_purchase(selected_product='orange')` when exactly 65 cents have been inserted
- Write a test for `can_purchase(selected_product='orange')` when more than 65 cents have been inserted

## Test Against Hardware Interface

The UX department has determined that the machine should blink a green LED when vending an apple, to signify health and wellness.

- Write a test that verifies the green light blinks when purchasing an apple
- Add the implementation of the LED blinking feature
- Test it out with the real vending machine hardware!

## Extra Credit

There's plenty of refactoring work that can be done. And we've also heard the hardware team have installed a second `LED.RED_LIGHT` which might flash in different situations.
