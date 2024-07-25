from tabulate import tabulate

from aave_leveraging_calculator.constants import (  # isort: skip
    AAVE_LIQ_LTV,
    INITIAL_TOKEN_AMOUNT,
    MAX_PERCENTAGE_USAGE,
    TOKEN_CURRENT_PRICE,
    TOKEN_TARGET_PRICE,
    TOKEN_TICKER,
)


def main():
    loop_count = 0
    collateral_amount = INITIAL_TOKEN_AMOUNT * TOKEN_CURRENT_PRICE
    borrow_amount = 0
    max_collateral, max_borrow, loop_count = loop(
        collateral_amount, borrow_amount, loop_count
    )

    token_amount_supplied = max_collateral / TOKEN_CURRENT_PRICE
    token_liquidation_price = max_borrow / (token_amount_supplied * AAVE_LIQ_LTV)

    profits_target = (
        (TOKEN_TARGET_PRICE * token_amount_supplied) - max_borrow - collateral_amount
    )
    profits_target_percent = (
        ((TOKEN_TARGET_PRICE * token_amount_supplied) - max_borrow - collateral_amount)
        / collateral_amount
        * 100
    )

    print("\n")

    data = [
        ["Loop operations", loop_count],
        ["Max collateral", f"${max_collateral:.2f}"],
        ["Max borrow", f"${max_borrow:.2f}"],
        [f"{TOKEN_TICKER} supplied", f"{token_amount_supplied:.3f}"],
        [
            f"{TOKEN_TICKER} liquidation price",
            f"${token_liquidation_price:.2f}",
        ],
        [
            f"Profits on {TOKEN_TICKER} price = ${TOKEN_TARGET_PRICE:.2f}",
            f"${profits_target:.2f}",
        ],
        [
            f"% Profits on {TOKEN_TICKER} price = ${TOKEN_TARGET_PRICE:.2f}",
            f"{profits_target_percent:.2f}%",
        ],
    ]

    print(tabulate(data, headers=["Description", "Value"], tablefmt="grid"))


def loop(collateral_amount, borrow_amount, loop_count):
    value_to_borrow = max_value_to_borrow(collateral_amount, borrow_amount)
    if value_to_borrow == 0:
        return collateral_amount, borrow_amount, loop_count
    loop_count += 1
    new_borrow_amount = borrow_amount + value_to_borrow
    new_collateral_amount = collateral_amount + value_to_borrow
    return loop(new_collateral_amount, new_borrow_amount, loop_count)


def max_value_to_borrow(total_collateral: float, total_borrow: float) -> float:
    value_to_borrow = total_collateral * MAX_PERCENTAGE_USAGE - total_borrow
    if value_to_borrow < 0.02 * TOKEN_CURRENT_PRICE:
        return 0
    return value_to_borrow


if __name__ == "__main__":
    main()
